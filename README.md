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

## Installation Guide:
Will be added soon

## How it should work:

0. Install all the dependencies and required packages and get the environment ready
1. Run main.py
2. Insert Vjudge handle and password
3. Insert Judge(UVa) handle and password
4. The program will automatically download your Accepted solutions from vjudge and then submit them one by one and store the accepted solutions to another folder(modules>Submitted>) while testing if it's already accepted in UVa or not.
5. Show you the status report.(Not completely done yet)

* As there are two versions of C++(C++ and C++11) in UVa and vjudge doesn't export that information, it's only submitted to C++11. There's a work-around I guess but it would be more complex. At least a large portion of submissions would surely get AC.
* Just FYI, none of the activities/data are tracked or bypassed to any other sources. But if you want to stay on the safe side, empty the cookies(used for reducing redundent login time) folder.
~~* Remember to test before using your main vjudge and uva accounts. I'll update this note if enough of you give positive feedbacks.~~
* Default parameters of uvaUser.submitAll() function is -> submitAll(submitSolvedOnes = False, limitSubmissionCount = 10). Change as you need.
* No checker added for UVa login status. Make sure you're using correct username and password.

<hr>
