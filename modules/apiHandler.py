
import requests
import json
import os

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

    def __init__(self, loadOffline = True):
        self.pidData = {}
        self.pnumData = {}
        self.uvaDataLoaded = False
        self.cfDataLoaded = False
        if(loadOffline):
            print("Loading offline problem data...")
            ### For UVa data loading
            self.uvaDataLoaded = True
            if os.path.exists(pidDataPath):
                self.pidData = list()
                leng = int(0)
                f = json.load(open(pidDataPath, 'r'))
                for pid, data in f.items():
                    d = [data['pnum'], data['title']]
                    tmp = int(pid)
                    while(leng<=tmp):
                        self.pidData.append([])
                        leng = leng + 1
                    else:
                        self.pidData[tmp] = d
            else:
                self.uvaDataLoaded = False

            if os.path.exists(pnumDataPath):
                self.pnumData = list()
                leng = int(0)
                f = json.load(open(pnumDataPath, 'r'))
                for pnum, data in f.items():
                    data = [data['pid'], data['title']]
                    tmp = int(pnum)
                    while(leng<=tmp):
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

    #Online
    def getUvaProblemDataUsingProblemNumber(self, problemNumber):
        response = requests.get(rootUVA + f"/api/p/num/{problemNumber}")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None
    
    def getUvaProblemDataUsingProblemNumberOffline(self, problemNumber):
        if(self.uvaDataLoaded):
            if(int(problemNumber) < len(self.pnumData)):
                return self.pnumData[int(problemNumber)]
            else:
                print(problemNumber, " doesn't exist")
                return None
        else:
            return self.getUvaProblemDataUsingProblemNumber(problemNumber)

    #Online
    def getUvaProblemDataUsingProblemId(self, problemId):
        response = requests.get(rootUVA + f"/api/p/id/{problemId}")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None

    def getUvaProblemDataUsingProblemIdOffline(self, problemId):
        if(self.uvaDataLoaded):
            if(int(problemId) < len(self.pidData)):
                return self.pidData[int(problemId)]
            else:
                print(problemId, " doesn't exist")
                return None
        else:
            return self.getUvaProblemDataUsingProblemId(problemId)

    #Online
    def getUvaProblemNumberFromProblemId(self, problemId):
        data = self.getUvaProblemDataUsingProblemId(problemId)
        if(data):
            return data['num']
        return None
    
    #Online
    def getUvaIdFromUsername(self, username):
        response = requests.get(rootUVA + f"/api/uname2uid/{username}")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None

    #Online
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
        if(data):
            problemListWithPid = dict()
            problemListWithPnum = dict()
            for x in data:
                problemListWithPid[str(x[0])] = {"pnum":str(x[1]), "title":str(x[2])}
                problemListWithPnum[str(x[1])] = {"pid":str(x[0]), "title":str(x[2])}
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
        response = requests.get("https://codeforces.com/api/user.status?handle="+username+"&from=1&count=1000000")
        if response.status_code == 200:
            print("CodeForces submissions received.")
            data = json.loads(response.content.decode('utf-8'))
            data = data['result']
            solves = set()
            for submission in data:
                verdict = submission['verdict']
                if(verdict == "OK"):
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
    def refreshCfProblemList(self):
        data = self.getCfProblemList()
        if(data):
            cfProblemList = dict()
            for x in data['result']['problems']:
                cfProblemList[str(x['contestId']) + str(x['index'])] = x['name']
            with open(cfDataPath, "w", encoding='utf8') as outfile:  
                json.dump(cfProblemList, outfile, indent=4, ensure_ascii=False)

            print(len(cfProblemList), " problem data saved offline.")
            self.__init__()
        else:
            print("There's a problem. No problem data fetched.")

    def getCodeForcesProblemDataUsingProblemNumber(self, problemNumber):
        if(self.cfDataLoaded):
            try:
                return [problemNumber, self.cfData[problemNumber]]
            except KeyError:
                self.refreshCfProblemList()
                return self.getCodeForcesProblemDataUsingProblemNumber(problemNumber)
        else:
            self.refreshCfProblemList()
            return self.getCodeForcesProblemDataUsingProblemNumber(problemNumber)

    def getCodeForcesLastSubmissionId(self, username):
        response = requests.get("https://codeforces.com/api/user.status?handle="+username+"&from=1&count=1")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            data = data['result'][0]['id']
            return data
        else:
            print("Could't get submission id. Please try this problem again later.")
            return ""