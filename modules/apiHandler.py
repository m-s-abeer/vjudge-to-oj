import json
import requests

class ApiCaller:

    def getProblemData(self, problemNumber):
        response = requests.get("https://uhunt.onlinejudge.org/api/p/num/" + str(problemNumber))
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            return data
        else:
            return None
    
    def getProblemNameFromNumber(self, problemNumber):
        data = self.getProblemData(problemNumber)
        if(data):
            return data['title']
        else:
            return None