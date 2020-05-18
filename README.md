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
1. Download/clone the repository from github.
  * If you have git write "git clone https://github.com/M-S-Abeer/vjudge-to-oj.git" opening cmd from the project directory.
  * Otherwise just download the repository normally.
2. Download python 3(version 3.7 or above preferred) or anaconda if you're comfortable with it. Direct python download link: https://www.python.org/downloads/.
3. If python package installer (pip) is working install the requirements. For that, open CLI/cmd/powershell inside "vjudge-to-oj" folder and run "pip install -r requirements.txt". This should install most of the dependencies/packages.
4. That should do the work, check out the next section. If it says a package is missing, try installing it with pip from cmd. i.e: "pip install package-name".

## How it should work:

0. Install all the dependencies and required packages and get the environment ready(Explained above)
1. Open cmd inside project directory and write "python main.py"
2. Insert Vjudge handle and password when asked
3. Insert Judge(UVa) handle and password when asked
4. The program will automatically download your Accepted solutions from vjudge and then submit them one by one and store the accepted solutions to another folder(modules>Submitted>UVA>) while testing if it's already accepted in UVa or not.
5. It'll show you the status report as it runs.

* Default parameters of uvaUser.submitAll() function is -> submitAll(submitSolvedOnes = False, limitSubmissionCount = 10). Change as you need. In case anything goes wrong, close the command prompt.
  * If submitSolvedOnes is set to True, it'll submit the solution regardless of your solve status to actual judge.
  * limitSubmissionCount is set to 10 for safety. It means it will submit upto 10 solutions and then stop the program. Change as required.
* It can automatically detect languages(C, C/C++, Java, Python) But as there are two versions of C++(C++ and C++11) in UVa and vjudge doesn't export that information, it's only submitted to C++11. There's a work-around I guess but it would be more complex. At least a large portion of submissions would surely get AC.
* Just FYI, none of the activities/data are tracked or bypassed to any other sources. But if you want to stay on the safe side, empty the cookies(used for reducing redundent login time) folder.
~~* Remember to test before using your main vjudge and uva accounts. I'll update this note if enough of you give positive feedbacks.~~
* No checker added for UVa login status. Make sure you're using correct username and password.
