from modules import judges
from modules.apiHandler import ApiCaller

'''
Refresh offline data
'''
# apicaller = ApiCaller()
# apicaller.refreshUvaProblemList() # run only if you think UVa has added new problems

# apicaller = ApiCaller()
# apicaller.refreshCfProblemList() # run only if you've solved from CF's newly added problems

# apicaller = ApiCaller()
# apicaller.refreshLojProblemList() # run only if you've solved from CF's newly added problems

'''
Vjudge Login
'''
vjUserName = input("Please enter your vjudge username: ")
vjPassword = input("Please enter your vjudge password: ")

vjudgeUser = judges.Vjudge(vjUserName, vjPassword)
vjudgeUser.downloadSubmissions()



'''
UVa Login
'''
UVaUserName = input("Please enter your UVa username: ")
UVaPassword = input("Please enter your UVa password: ")

uvaUser = judges.UVA(UVaUserName, UVaPassword)
uvaUser.submitAll(submitSolvedOnes = False, limitSubmissionCount = 10)



'''
CodeForces Login
'''
CfUserName = input("Please enter your CodeForces username: ")
CfPassword = input("Please enter your CodeForces password: ")

cfUser = judges.CF(CfUserName, CfPassword)
cfUser.submitAll(submitSolvedOnes = False, limitSubmissionCount = 10)


'''
LightOJ Login
'''
lojUser = judges.LOJ()
lojUser.submitAll(submitSolvedOnes = False, limitSubmissionCount = 10)


'''
SPOJ Login
'''
SpojUserName = input("Please enter your SPOJ username: ")
SpojPassword = input("Please enter your SPOJ password: ")

SpojUser = judges.SPOJ(SpojUserName, SpojPassword)
SpojUser.submitAll(submitSolvedOnes = False, limitSubmissionCount = 20)
