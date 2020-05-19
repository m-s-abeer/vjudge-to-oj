from .submissions import *
from .apiHandler import ApiCaller
from requests import session
from zipfile import ZipFile
import http.cookiejar
import mechanize
import shutil
import pickle
import time
import os

path = os.path.dirname(__file__)
apicaller = ApiCaller()

class Vjudge:
    judgeSlug = "Vjudge"
    rootUrl = "https://vjudge.net/"
    loginUrl = "/user/login/"
    allSubmissionsUrl = "/user/exportSource?minRunId=0&maxRunId=99999999&ac=false"
    acSubmissionsUrl = "/user/exportSource?minRunId=0&maxRunId=99999999&ac=true"
    username = str()
    password = str()
    zipUrl = str()
    s = session()
    loggedIn = False
    # Browser

    def clearSolutions(self):
        solutionsDir = path + os.sep + "solutions"
        try:
            shutil.rmtree(solutionsDir)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
            pass
        time.sleep(2)
        os.mkdir(solutionsDir)

    def __init__(self, username = "", password = ""):
        self.username = username
        self.password = password
        self.login()
    
    # Thanks to Mehedi Imam Shafi for this Vjudge sign-in approach
    def login(self):
        payLoad = {
            'username': self.username,
            'password': self.password
        }
        user_data_path = path + os.sep + "cookies" + os.sep + f'{self.username}_login_session.dat'

        if os.path.exists(user_data_path):
            self.s = pickle.load(open(user_data_path, 'rb'))
            self.loggedIn = True
            print("Logged in from cookies")
        else:
            self.s = session()
            login_url = f"{self.rootUrl}{self.loginUrl}"
            r = self.s.post(login_url, data=payLoad)
            if(r.text == "success"):
                with open(user_data_path, 'wb') as file:
                    pickle.dump(self.s, file)
                self.loggedIn = True
            else:
                print(r.text)
            # print(r.text, r)

        # print(s.cookies.get_dict())

    def downloadSubmissions(self):
        if(self.loggedIn == False):
            print("Sorry, can't download data. You are not logged into Vjudge.")
            return None
        self.zipUrl = path + os.sep + "zip-files" + os.sep + self.username + '.zip'
        if os.path.exists(self.zipUrl):
            os.remove(self.zipUrl)

        self.clearSolutions()
        source_dowload_url = f"{self.rootUrl}{self.acSubmissionsUrl}"
        self.downloadUrl(source_dowload_url, self.s, self.zipUrl)
        self.extractZip()
        print("Solutions downloaded and extracted.")
    
    def downloadUrl(self, url, sess, save_path, chunk_size=128):
        r = sess.get(url, stream=True)
        with open(save_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)

    def extractZip(self, sourcePath = ""):
        sourcePath = self.zipUrl if not sourcePath else sourcePath
        destinationPath = path + os.sep + "solutions"
        with ZipFile(sourcePath, 'r') as zipFile:
            zipFile.extractall(destinationPath)

'''

'''
class UVA:
    judgeSlug = "UVA"
    loginURL = "https://onlinejudge.org/"
    submissionURL = "https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25"
    localSubsURL = path + os.sep + "solutions" + os.sep + "UVA"
    username = str()
    password = str()
    userid = str()
    loggedIn = bool()
    extentionId = {
        "c" : "1",
        "java" : "2",
        "cpp" : "5",
        "c++" : "5",
        "py" : "6"
    }
    # Browser
    br = mechanize.Browser()
    solvedProblemIds = set()

    def __init__(self, username = "", password = ""):
        self.username = username
        self.password = password
        self.userid = apicaller.getUvaIdFromUsername(username)

        # Cookie Jar
        cj = http.cookiejar.LWPCookieJar()
        self.br.set_cookiejar(cj)

        # Browser options
        self.br.set_handle_equiv(True)
        self.br.set_handle_gzip(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(True)
        self.br.set_handle_robots(False)
        self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        self.br.addheaders = [('User-agent', 'Chrome')]
        if(self.login()):
            self.saveSolveData()
    
    def login(self):
        # The site we will navigate into, handling it's session
        self.br.open(self.loginURL)

        # View available forms
        # for f in self.br.forms():
        #     print(f)

        # Select the second (index one) form (the first form is a search query box)
        self.br.select_form(nr=0)
        self.loggedIn = True
        self.br.form['username'] = self.username
        self.br.form['passwd'] = self.password
        res = self.br.submit()
        if(res.geturl() == self.loginURL):
            print("Logged In Successfully")
            return True
        else:
            print("UVA: Sorry, wrong username/password. Please try again.")
            self.loggedIn = False
            return False
        return True

    '''
    saveSolveData
    Get The Bit-Encoded-Problem IDs that Has Been Solved by Some Authors
    URL : /api/solved-bits/{user-ids-csv}.

    Returns an array each contains: { uid:the-user-id, solved:[bit-encoded-solved-pids] }.

    The bit-encoded-solved-pids is an array where the ith bit of the jth element (0-based) represents whether the particular user has solved the problem with pid = (j*32)+i.
    '''
    def saveSolveData(self):
        solveData = apicaller.getUvaSolveData(self.userid)
        i = 0
        for x in solveData:
            for j in range(0, 32):
                if(((x>>j)&1) == 1):
                    self.solvedProblemIds.add(str(i*32+j))
            i = i+1
        print("Solved problems added to consideration")
        # print(sorted(self.solvedProblemIds))

    def isSolved(self, problemId):
        return (str(problemId) in self.solvedProblemIds)

    def submitAll(self, submitSolvedOnes = False, limitSubmissionCount = 10):
        if(self.loggedIn == False):
            print("Not logged into UVa. Can't submit.")            
            return None
        successfullySubmitted = 0
        for problemNumber in os.listdir(self.localSubsURL):
            problemLocalUrl = self.localSubsURL + os.sep + problemNumber
            problemDetails = apicaller.getUvaProblemDataUsingProblemNumberOffline(problemNumber)
            # print(problemNumber, problemDetails, type(problemDetails))
            if((submitSolvedOnes == True) or (self.isSolved(problemDetails[0]) == False)):
                problem = UvaProblem(problemLocalUrl, problemNumber)
                for solve, solveId in problem.solutions:
                    if(successfullySubmitted == limitSubmissionCount):
                        print("SubmissionLimitReached. Please run again")
                        return None
                    
                    print(solve)
                    print(f"Trying Problem: {solve}, {solveId}")
                    sid = str(self.submitSolution(solve))
                    while(str(sid) == ""):
                        print("Submission failed. Trying again after 2 secs.")
                        time.sleep(2)
                        sid = str(self.submitSolution(solve))
                    else:
                        print(f"Problem submitted: sid = {sid}")
                        problem.saveSolution(solveId, sid)
                        print()

                    successfullySubmitted  = successfullySubmitted + 1
                    # check verdict and verify
                    # timeout = 
                    # while(1)
            elif((submitSolvedOnes == False)):
                print(problemNumber + " - " + problemDetails[1] + " -> solved already")

        pass

# Specific Users' Submissions on Specific Problems
# Returns all the submissions of the users on specific problems.

# URL : /api/subs-pids/{user-ids-csv}/{pids-csv}/{min-subs-id}.

# The {user-ids-csv} is the user ids presented as comma-separated-values. Similarly, the {pids-csv} is the problem ids presented in comma-separated-values. The numbers in the both csvs are limited to 100 numbers. The {min-subs-id} is the minimum submission id to be returned (that is, to show all submissions set this value to zero, to see latest submissions, set it higher as appropriate).

# The result is a hash map with the key is the user id and the value is the submissions of that user that associated with one of the specified problem ids. The format of the submissions is identical with the above description.

# URL : /api/subs-nums/{user-ids-csv}/{nums-csv}/{min-subs-id}.

# This is exactly the same as before, except that the problems is given in problem numbers, not problem ids.
    
    def submitSolution(self, solution):
        self.br.open(self.submissionURL)
        # for f in br.forms():
        #     print(f)
        self.br.select_form(nr=1)
        self.br.form['localid'] = str(solution.problemNumber)
        self.br.form.find_control(name="language").value = [self.extentionId[solution.solutionExt]]
        self.br.form.find_control(name="code").value = solution.solutionCode
        res = self.br.submit()
        submissionId = res.geturl().split('+')[-1]
        return submissionId

        # then we should check if the verdict has been given
        # should check repeatedly delaying 5-10 secs and stop when a verdict is given
