from modules import judges
from modules.apiHandler import ApiCaller
from environ import VJ_USER, VJ_PASS, UVA_USER, UVA_PASS, CF_USER, CF_PASS, SPOJ_USER, SPOJ_PASS, \
    REFRESH_OFFLINE_PROBLEM_DATA, SUBMISSION_LIMIT
from environ import USE_VJ, USE_UVA, USE_CF, USE_SPOJ, USE_LOJ

'''
Refresh offline data
'''
if REFRESH_OFFLINE_PROBLEM_DATA is True:
    apicaller = ApiCaller()
    apicaller.refreshUvaProblemList() # run only if you think UVa has added new problems

    apicaller = ApiCaller()
    apicaller.refreshCfProblemList() # run only if you've solved from CF's newly added problems

    apicaller = ApiCaller()
    apicaller.refreshLojProblemList() # run only if you've solved from CF's newly added problems

'''
Vjudge Login
'''
if USE_VJ is True:
    vjudgeUser = judges.Vjudge(VJ_USER, VJ_PASS)
    vjudgeUser.downloadSubmissions()

'''
UVa Login
'''
if USE_UVA is True:
    uvaUser = judges.UVA(UVA_USER, UVA_PASS)
    uvaUser.submitAll(submitSolvedOnes=False, limitSubmissionCount=SUBMISSION_LIMIT)

'''
CodeForces Login
'''
if USE_CF is True:
    cfUser = judges.CF(CF_USER, CF_PASS)
    cfUser.submitAll(submitSolvedOnes=False, limitSubmissionCount=SUBMISSION_LIMIT)

'''
LightOJ Login
'''
if USE_LOJ is True:
    lojUser = judges.LOJ()
    lojUser.submitAll(submitSolvedOnes=False, limitSubmissionCount=SUBMISSION_LIMIT)

'''
SPOJ Login
'''
if USE_SPOJ is True:
    SpojUser = judges.SPOJ(SPOJ_USER, SPOJ_PASS)
    SpojUser.submitAll(submitSolvedOnes=False, limitSubmissionCount=SUBMISSION_LIMIT)
