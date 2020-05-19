from modules import judges

vjUserName = input("Please enter your vjudge username: ")
vjPassword = input("Please enter your vjudge password: ")

vjudgeUser = judges.Vjudge(vjUserName, vjPassword)
vjudgeUser.downloadSubmissions()

UVaUserName = input("Please enter your UVa username: ")
UVaPassword = input("Please enter your UVa password: ")

# apicaller.refreshUvaProblemList() # run only if you think UVa has added new problems

uvaUser = judges.UVA(UVaUserName, UVaPassword)
uvaUser.submitAll(submitSolvedOnes = False, limitSubmissionCount = 10)

