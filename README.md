# vjudge-to-oj

Competitive programmers spend thousands of hours practicing programming problems and participating contests.
Vjudge has been an amazing platform for participating/hosting programming contests and problem-solving.

However, there can be scenarios where you'd like to add vjudge solutions to the actual judge profiles specifically.
I personally felt the need of it along with some of my friends and colleagues.
It's a tiresome job to submit all the solved problems of vjudge to the actual judge. This here is a small approach to get such works done easily.

Current solution will only work for UVa. It's roughly written and tested. But hey, it works!

With enough response and your contribution I hope to add some more judges here as well. Huge thanks to @mehedi-shafi for contributing to all my fun projects.

Let me know if you have any questions/suggestions/feedbacks or simply if you liked it.

Email: mahmudsajjad.abeer@gmail.com

Hope you enjoy. <3
<hr>


## How it should work:

0. Install all the dependencies and required packages and get the environment ready
1. Run main.py
2. Insert Vjudge handle and password
3. Insert Judge(UVa) handle and password
4. The program will automatically download your Accepted solutions from vjudge and then submit them one by one and store the accepted solutions to another folder(modules>Submitted>) while testing if it's already accepted in UVa or not.
5. Show you the status report.(Not completely done yet)

* Just FYI, none of the activities/data are tracked or bypassed to any other sources. But if you want to stay on the safe side, empty the zip-files and cookies(used for reducing redundent login time) folder.
* Remember to test before using your main vjudge and uva accounts. I'll update this note if enough of you give positive feedbacks.
* default parameters of submitAll() function is -> uvaUser.submitAll(submitSolvedOnes = False, limitSubmissionCount = 10). Change as you need.
* No checker added for UVa login status. Make sure you're using correct username and password.

<hr>

##### To-do for myself(basic version, UVa):

1. Being able to login to vjudge, download and extract all the submissions(Done)
2. Problem object sketch:(Done)
    1. judgeSlug(mapped from the folder name. i.e: Submissions>UVA)
    2. problemId(collected from subfolder of judge submissions. i.e: Submissions>UVA>104)
    3. problemName(collected from UVa api)
    4. Solutions
        1. Submission Code(all the files inside a problem id. i.e: Submissions>UVA>104>123124.cpp)
        2. Language(from solution extention. i.e: Submissions>UVA>104>1231123.cpp)
3. Being able to open login link in browser(Done)
4. Being able to write on submission link(Done)
5. Being able to press submit button automatically(Done)
6. Submitting all the solutions automatically(Done)
7. Store the submitted solution locally in a specific format("104 - Arbitrage.cpp")(Done)
8. Preparing status report
9. Checking if the problem is already solved on judge(Done)
10. verify if the submitted solutions got AC
