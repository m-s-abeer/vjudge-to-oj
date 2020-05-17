from .submissions import Solution
from requests import session
from zipfile import ZipFile
import http.cookiejar
import mechanize
import shutil
import pickle
import os

path = os.path.dirname(__file__)

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
    # Browser

    def clearSolutions(self):
        solutionsDir = path + os.sep + "solutions"
        try:
            shutil.rmtree(solutionsDir)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))
        os.mkdir(solutionsDir)

    def __init__(self, username = "", password = ""):
        self.username = username
        self.password = password
        # self.login()
    
    # Thanks to Mehedi Imam Shafi for this Vjudge sign-in approach
    def login(self):
        payLoad = {
            'username': self.username,
            'password': self.password
        }
        user_data_path = path + os.sep + "cookies" + os.sep + f'{self.username}_login_session.dat'

        if os.path.exists(user_data_path):
            self.s = pickle.load(open(user_data_path, 'rb'))
        else:
            self.s = session()
            login_url = f"{self.rootUrl}{self.loginUrl}"
            r = self.s.post(login_url, data=payLoad)

            with open(user_data_path, 'wb') as file:
                pickle.dump(self.s, file)
            print(r.text, r)

        # print(s.cookies.get_dict())
    
    def downloadUrl(self, url, sess, save_path, chunk_size=128):
        r = sess.get(url, stream=True)
        with open(save_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)

    def downloadSubmissions(self):
        self.zipUrl = path + os.sep + "zip-files" + os.sep + self.username + '.zip'
        source_dowload_url = f"{self.rootUrl}{self.acSubmissionsUrl}"
        self.downloadUrl(source_dowload_url, self.s, self.zipUrl)

    def extractZip(self, sourcePath = ""):
        self.clearSolutions()
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
    username = str()
    password = str()
    extentionId = {
        "c" : "1",
        "java" : "2",
        "cpp" : "5",
        "c++" : "5",
        "py" : "6"
    }
    # Browser
    br = mechanize.Browser()

    def __init__(self, username = "", password = ""):

        self.username = username
        self.password = password

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
        self.login()
    
    def login(self):
        # The site we will navigate into, handling it's session
        self.br.open(self.loginURL)

        # View available forms
        # for f in self.br.forms():
        #     print(f)

        # Select the second (index one) form (the first form is a search query box)
        self.br.select_form(nr=0)

        # # User credentials
        self.br.form['username'] = self.username
        self.br.form['passwd'] = self.password

        # # Login
        res = self.br.submit()
        # print(res.geturl())
    
    def submitSolution(self, solution):
        
        self.br.open(self.submissionURL)
        # for f in br.forms():
        #     print(f)

        self.br.select_form(nr=1)
        self.br.form['localid'] = solution.problemId
        self.br.form.find_control(name="language").value = [self.extentionId[solution.solutionExt]]
        self.br.form.find_control(name="code").value = solution.solutionCode
        res = self.br.submit()
        submissionId = res.geturl().split('+')[-1]

        # then we should check if the verdict has been given
        # should check repeatedly delaying 5-10 secs and stop when a verdict is given
