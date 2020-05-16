import apiHandler
import os

apicaller = apiHandler.ApiCaller()

class Submission:
    # 1. judgeSlug(mapped from the folder name. i.e: Submissions>UVA)
    # 2. problemId(collected from subfolder of judge submissions. i.e: Submissions>UVA>104)
    # 3. problemName(collected from UVa api)
    # 4. Solutions
    #     1. Submission Code(all the files inside a problem id. i.e: Submissions>UVA>104>123124.cpp)
    #     2. Language mapping(from solution extention. i.e: Submissions>UVA>104>1231123.cpp)

    judgeSlug = str()
    problemId = str()
    problemName = str()
    solutions = list()

    def __init__(self, problemDir, judgeSlug = "UVA", problemId = ""):
        self.judgeSlug = judgeSlug
        self.problemId = problemId
        self.problemName = apicaller.getProblemNameFromNumber(problemId)
        print(problemDir)
        for subName in os.listdir(problemDir):
            self.solutions.append(Solution(problemDir + os.sep + subName))

    def getName(self):
        return self.judgeSlug + " - " + self.problemName

    def __str__(self):
        return self.judgeSlug + " - " + self.problemName + str(self.solutions.len)

class Solution:
    solutionCode = str()
    solutionExt = str()

    def __init__(self, submissionDir):
        self.solutionExt = submissionDir.split('.')[-1]
        print(submissionDir)
        with open(submissionDir, 'r') as code:
            self.solutionCode = code.read()