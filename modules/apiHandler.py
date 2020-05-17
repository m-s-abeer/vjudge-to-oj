import json
import requests

rootUVA = "https://uhunt.onlinejudge.org"

class ApiCaller:

    def getProblemData(self, problemNumber):
        response = requests.get(rootUVA + f"/api/p/num/{problemNumber}")
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None
    
    def getUvaProblemData(self, problemNumber):
        data = self.getProblemData(problemNumber)
        if(data):
            return data
        else:
            return None
    
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
