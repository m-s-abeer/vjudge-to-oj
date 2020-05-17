# vjudge-to-oj

Competitive programmers spend thousands of hours practicing programming problems and participating contests.
Vjudge has been an amazing platform for participating/hosting programming contests and problem-solving.

However, there can be scenarios where you'd like to add vjudge solutions to the actual judge profiles specifically.
I personally felt the need of it along with some of my friends and colleagues.
It's a tiresome job to submit all the solved problems of vjudge to the actual judge. This here is a small approach to get such works done easily.

Current solution will only work for UVa. With enough response or your contribution I hope to add some more judges as well. Huge thanks to @mehedi-shafi for contributing to all my fun projects.

Hope you enjoy. <3


<hr>


## How it should work:

0. Install all the dependencies and required packages and get the environment ready
1. Run main.py
2. Insert Vjudge handle and password
3. Insert Judge(UVa) handle and password
4. The program will automatically submit accepted solutions from vjudge one by one and store the accepted solutions to another folder when it get ac on judge as well
5. Show you the status report.(Not completely done yet)

* No checker added for UVa login status. Make sure you're using correct username and password.



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
