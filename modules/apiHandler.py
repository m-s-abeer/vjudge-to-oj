import requests
import json
import os
import bs4
import numpy as np

path = os.path.dirname(__file__)
pidDataPath = path + os.sep + "offline_problem_data" + os.sep + "pDataWithPid.json"
pnumDataPath = path + os.sep + "offline_problem_data" + os.sep + "pDataWithPnum.json"
cfDataPath = path + os.sep + "offline_problem_data" + os.sep + "cfProblemData.json"

rootUVA = "https://uhunt.onlinejudge.org"
rootCF = "https://codeforces.com/"

'''
uHunt Problem object:-
pid: problemId
num: problemNumber
title: problemTitle
'''


class ApiCaller:
    pidData = {}
    pnumData = {}
    uvaDataLoaded = bool()
    cfData = {}
    cfDataLoaded = bool()

    def __init__(self, loadOffline=True):
        self.pidData = {}
        self.pnumData = {}
        self.uvaDataLoaded = False
        self.cfDataLoaded = False
        if (loadOffline):
            print("Loading offline problem data...")
            ### For UVa data loading
            self.uvaDataLoaded = True
            if os.path.exists(pidDataPath):
                self.pidData = list()
                leng = int(0)
                f = json.load(open(pidDataPath, 'r', encoding='utf-8'))
                for pid, data in f.items():
                    d = [data['pnum'], data['title']]
                    tmp = int(pid)
                    while (leng <= tmp):
                        self.pidData.append([])
                        leng = leng + 1
                    else:
                        self.pidData[tmp] = d
            else:
                self.uvaDataLoaded = False

            if os.path.exists(pnumDataPath):
                self.pnumData = list()
                leng = int(0)
                f = json.load(open(pnumDataPath, 'r', encoding='utf-8'))
                for pnum, data in f.items():
                    data = [data['pid'], data['title']]
                    tmp = int(pnum)
                    while (leng <= tmp):
                        self.pnumData.append([])
                        leng = leng + 1
                    else:
                        self.pnumData[tmp] = data
            else:
                self.uvaDataLoaded = False
            print("UVa Problem Data Loaded.")

            ### For CodeForces data loading
            self.cfDataLoaded = True
            if os.path.exists(cfDataPath):
                self.cfData = dict()
                f = json.load(open(cfDataPath, 'r', encoding='utf-8'))
                for pid, pname in f.items():
                    self.cfData[pid] = pname
            else:
                self.cfDataLoaded = False
            print("CodeForces Problem Data Loaded.")

    def printProgressBar(self, iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
        # Print New Line on Complete
        if iteration == total:
            print()

    # Online
    def getUvaProblemDataUsingProblemNumber(self, problemNumber):
        response = requests.get(rootUVA + f"/api/p/num/{problemNumber}")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None

    def getUvaProblemDataUsingProblemNumberOffline(self, problemNumber):
        if (self.uvaDataLoaded):
            if (int(problemNumber) < len(self.pnumData)):
                return self.pnumData[int(problemNumber)]
            else:
                print(problemNumber, " doesn't exist")
                return None
        else:
            return self.getUvaProblemDataUsingProblemNumber(problemNumber)

    # Online
    def getUvaProblemDataUsingProblemId(self, problemId):
        response = requests.get(rootUVA + f"/api/p/id/{problemId}")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None

    def getUvaProblemDataUsingProblemIdOffline(self, problemId):
        if (self.uvaDataLoaded):
            if (int(problemId) < len(self.pidData)):
                return self.pidData[int(problemId)]
            else:
                print(problemId, " doesn't exist")
                return None
        else:
            return self.getUvaProblemDataUsingProblemId(problemId)

    # Online
    def getUvaProblemNumberFromProblemId(self, problemId):
        data = self.getUvaProblemDataUsingProblemId(problemId)
        if (data):
            return data['num']
        return None

    # Online
    def getUvaIdFromUsername(self, username):
        response = requests.get(rootUVA + f"/api/uname2uid/{username}")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None

    # Online
    def getUvaSolveData(self, userid):
        response = requests.get(rootUVA + f"/api/solved-bits/{userid}")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            # print(data)
            print(f"Solve data of {userid} fetched from uHunt")
            return data[0]['solved']
            # return data['solved']
        else:
            return None

    def getUvaProblemList(self):
        response = requests.get(rootUVA + "/api/p")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None

    def refreshUvaProblemList(self):
        data = self.getUvaProblemList()
        if (data):
            problemListWithPid = dict()
            problemListWithPnum = dict()
            for x in data:
                problemListWithPid[str(x[0])] = {"pnum": str(x[1]), "title": str(x[2])}
                problemListWithPnum[str(x[1])] = {"pid": str(x[0]), "title": str(x[2])}
            with open(pidDataPath, "w") as outfile:
                json.dump(problemListWithPid, outfile, indent=4)
            with open(pnumDataPath, "w") as outfile:
                json.dump(problemListWithPnum, outfile, indent=4)

            print(len(problemListWithPid), " problem data saved offline.")
            self.__init__()
        else:
            print("There's a problem. No problem data fetched.")

    # Online
    def getCfSolveData(self, username):
        print("Requesting submissions for: " + username)
        response = requests.get("https://codeforces.com/api/user.status?handle=" + username + "&from=1&count=1000000")
        if response.status_code == 200:
            print("CodeForces submissions received.")
            data = json.loads(response.content.decode('utf-8'))
            data = data['result']
            solves = set()
            for submission in data:
                verdict = submission['verdict']
                if (verdict == "OK"):
                    if submission['problem'].get('contestId'):
                        contestId = submission['problem']['contestId']
                        problemId = submission['problem']['index']
                        solves.add(str(contestId) + str(problemId))
            return solves
        else:
            print("Couldn't fetch submissions.")
            return None

    # Online
    def getCfProblemList(self):
        print("Fetching CodeForces Problem List.")
        response = requests.get(rootCF + "/api/problemset.problems")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None

    # Online
    def getCfGymContestList(self):
        print("Fetching CodeForces Gym Contest List.")
        previousContestId = -1
        currentContestId = 0
        isLastPage = False

        contestList = set()
        for page in range(100):
            pageURL = 'https://codeforces.com/gyms/page/' + str(page+1) + '?searchByProblem=false'
            pageRowdata = requests.get(pageURL)
            soup = bs4.BeautifulSoup(pageRowdata.text, "lxml")

            rowCount = 0
            for tr_tag in soup.find_all('tr'):
                for td_tag in tr_tag.find_all('td', attrs={'class': 'state'}):
                    for a_tag in td_tag.find_all('a'):
                        each_a = a_tag['href'].split('/')
                        contestID = each_a[2]
                        if(rowCount == 0):
                            currentContestId = contestID
                            rowCount += 1
                            if currentContestId == previousContestId:
                                isLastPage = True
                                break

                        contestList.add(contestID)
                        previousContestId = currentContestId

                if isLastPage:
                    break

            if isLastPage:
                break

        return contestList

    # Online
    def getCfGymProblemList(self):
        contestList = self.getCfGymContestList()
        print("Fetching CodeForces Gym Problem List (This may take upto 20 minutes)")
        numberOfContest  = len(contestList)
        self.printProgressBar(0, numberOfContest, prefix='Progress:', suffix='Complete', length=50)  # Initializing Progress Bar

        contestNumber=0
        skipped = 0
        problemList = dict()
        for contestID in contestList:
            contestNumber +=1
            contestProblemListPageURL = 'https://codeforces.com/gym/' + contestID
            try:
                pageRowData = requests.get(contestProblemListPageURL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0'})

                soup = bs4.BeautifulSoup(pageRowData.text, "lxml")
                for div in soup.find_all('div', attrs={'style': 'float: left;'}):
                    for a_tag in div.find_all('a'):
                        href = a_tag['href'].split('/')
                        problemID = href[2] + href[4]
                        problemName = a_tag.get_text()
                        problemList[problemID] = problemName
                        # print(problemID)
            except requests.exceptions.ConnectionError:
                print('Network connection failed on contest ' + contestID + '. Check your internet connection. Trying next contest.')
                skipped += 1
            except TimeoutError:
                print('Timeout on contest ' + contestID + ', trying next contest.')
                skipped += 1

            self.printProgressBar(contestNumber, numberOfContest, prefix='Progress:', suffix='Complete', length=50)

        print(skipped, ' CF Gym contest skipped.')

        return problemList

    def refreshCfProblemList(self):
        data = self.getCfProblemList()
        gymProblemList = self.getCfGymProblemList()
        if (data):
            cfProblemList = dict()
            for problem in data['result']['problems']:
                cfProblemList[str(problem['contestId']) + str(problem['index'])] = problem['name']
            for problem in gymProblemList:
                cfProblemList[problem] = gymProblemList[problem]
            with open(cfDataPath, "w", encoding='utf8') as outfile:
                json.dump(cfProblemList, outfile, indent=4, ensure_ascii=False)

            print(len(cfProblemList), " CF problem data saved offline.")
            self.__init__()
        else:
            print("There's a problem. No problem data fetched.")

    def getCodeForcesProblemDataUsingProblemNumber(self, problemNumber):
        if (self.cfDataLoaded):
            try:
                return [problemNumber, self.cfData[problemNumber]]
            except KeyError:
                print(
                    "Problem ID not found from CF. Try refreshing CF problem list from main.py once. Otherwise, it may be an issue of problem id of concurrent contest problems.")
                return [problemNumber, "No name from CF api list"]
        else:
            self.refreshCfProblemList()
            return self.getCodeForcesProblemDataUsingProblemNumber(problemNumber)

    def getCodeForcesLastSubmissionId(self, username):
        response = requests.get("https://codeforces.com/api/user.status?handle=" + username + "&from=1&count=1")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            data = data['result'][0]['id']
            return data
        else:
            print("Could't get submission id. Please try this problem again later.")
            return ""

    # Online
    def getSPOJSolveData(self, username):
        """
            This will be use in retrive already solved problem list of user in Spoj
        """
        start = 0  # We want to check from very last submission
        self.submissions = []
        previous_Submission_ID = -1
        current_Submission_ID = 0

        isLastPage = False

        # We assuming an user has at most 1000 page of submission on spoj (a single page has 20 submission history)
        for page in range(1000):
            url = "https://www.spoj.com/status/" + username + "/all/start=" + str(start)

            start += 20  # Spoj show 20 submission list in a single page

            pageData = requests.get(url)

            soup = bs4.BeautifulSoup(pageData.text, "lxml")
            table_body = soup.find("tbody")

            # Check if the page retrieved has no submissions
            if len(table_body) == 1:
                return self.submissions

            rowCnt = 0
            for row in table_body:
                if isinstance(row, bs4.element.Tag):
                    if rowCnt == 0:
                        current_Submission_ID = row.contents[1].contents[0]

                        # if we reached the last submission before page 1000 then it showing same submission of last valid page
                        # we want to ignore them and break the loop
                        if current_Submission_ID == previous_Submission_ID:
                            isLastPage = True
                            break

                    rowCnt += 1
                    previous_Submission_ID = current_Submission_ID

                    # Problem Name/URL
                    uri = row.contents[5].contents[0]

                    problem_id = uri["href"].split('/')
                    problem_id = problem_id[2]
                    # Problem Status
                    status = str(row.contents[6])
                    if status.__contains__("accepted"):
                        self.submissions.append(problem_id)

            if isLastPage:
                break
        self.submissions = np.unique(self.submissions)
        # print(self.submissions)
        return self.submissions
