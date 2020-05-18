import json
import requests

rootUVA = "https://uhunt.onlinejudge.org"
'''
uHunt Problem object:-
pid: problemId
num: problemNumber
title: problemTitle
'''
class ApiCaller:

    def getUvaProblemDataUsingProblemNumber(self, problemNumber):
        response = requests.get(rootUVA + f"/api/p/num/{problemNumber}")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None
    
    def getUvaProblemDataUsingProblemId(self, problemId):
        response = requests.get(rootUVA + f"/api/p/id/{problemId}")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None

    def getUvaProblemNumberFromProblemId(self, problemId):
        data = self.getUvaProblemDataUsingProblemId(problemId)
        if(data):
            return data['num']
    
    def getUvaIdFromUsername(self, username):
        response = requests.get(rootUVA + f"/api/uname2uid/{username}")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None

    def getUvaSolveData(self, userid):
        response = requests.get(rootUVA + f"/api/solved-bits/{userid}")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            # print(data)
            return data[0]['solved']
            # return data['solved']
        else:
            return None
