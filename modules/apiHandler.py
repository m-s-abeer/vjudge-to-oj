
import requests
import json
import os

path = os.path.dirname(__file__)
pidDataPath = str()
pnumDataPath = str()

rootUVA = "https://uhunt.onlinejudge.org"
'''
uHunt Problem object:-
pid: problemId
num: problemNumber
title: problemTitle
'''
class ApiCaller:

    pidData = {}
    pnumData = {}
    dataLoaded = True

    def __init__(self, loadOffline = True):
        if(loadOffline):
            if os.path.exists(pidDataPath):
                self.pidData = json.load(open(pidDataPath, 'r'))
            else:
                self.dataLoaded = False

            if os.path.exists(pnumDataPath):
                self.pnumData = json.load(open(pnumDataPath, 'r'))
            else:
                self.dataLoaded = False
        

    #Online
    def getUvaProblemDataUsingProblemNumber(self, problemNumber):
        response = requests.get(rootUVA + f"/api/p/num/{problemNumber}")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None
    
    def getUvaProblemDataUsingProblemNumberOffline(self, problemNumber):
        if(self.dataLoaded):
            return pnumData[str(problemNumber)]
        else:
            return getUvaProblemDataUsingProblemNumber(problemNumber)

    #Online
    def getUvaProblemDataUsingProblemId(self, problemId):
        response = requests.get(rootUVA + f"/api/p/id/{problemId}")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None

    def getUvaProblemDataUsingProblemIdOffline(self, problemNumber):
        if(self.dataLoaded):
            return pnumData[str(problemNumber)]
        else:
            return getUvaProblemDataUsingProblemId(problemNumber)

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
            
            pidDataPath = path + os.sep + "offline_problem_data" + os.sep + "pDataWithPid.json"
            pnumDataPath = path + os.sep + "offline_problem_data" + os.sep + "pDataWithPnum.json"
            with open(pidDataPath, "w") as outfile:  
                json.dump(problemListWithPid, outfile, indent=4) 
            with open(pnumDataPath, "w") as outfile:  
                json.dump(problemListWithPnum, outfile, indent=4)

            print(len(problemListWithPid), " problem data saved offline.")
            self.__init__()
        else:
            print("There's a problem. No problem data fetched.")