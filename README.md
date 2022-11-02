# vjudge-to-oj
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/m-s-abeer/vjudge-to-oj.svg)](https://github.com/m-s-abeer/vjudge-to-oj/blob/master/LICENSE)
[![GitHub forks](https://img.shields.io/github/forks/m-s-abeer/vjudge-to-oj.svg?style=social&label=Fork)](https://github.com/m-s-abeer/vjudge-to-oj)
[![GitHub stars](https://img.shields.io/github/stars/m-s-abeer/vjudge-to-oj.svg?style=social&label=Stars)](https://github.com/m-s-abeer/vjudge-to-oj)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fm-s-abeer%2Fvjudge-to-oj%2Fhit-counter&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

Competitive programmers spend thousands of hours practicing programming problems and participating contests.
Vjudge has been an amazing platform for participating/hosting programming contests and problem-solving.

However, there can be scenarios where you'd like to add vjudge solutions to the actual judge profiles specifically.
I personally felt the need of it along with some of my friends and colleagues.
It's a tiresome job to submit all the solved problems of vjudge to the actual judges. This here is a small approach to get such works done easily.

Current solution will only work for **UVa** and **CodeForces**. 
So far, it's pretty much stable and working just fine. It's roughly written and tested. But hey, it works!!!

With enough response and your contribution I hope to add some more judges here as well. Huge thanks to @mehedi-shafi for contributing to all my fun projects.

Let me know if you have any questions/suggestions/feedbacks or simply if you liked it.

Email: mahmudsajjad.abeer@gmail.com

Hope you enjoy. <3
<hr>

## Installation Guide:
1. Download/clone the repository from github.
  * If you have git write```git clone https://github.com/m-s-abeer/vjudge-to-oj.git``` opening cmd from the project directory.
  * Otherwise just download the repository normally.
1. Download python 3(version 3.7 or above preferred) or anaconda if you're comfortable with it. Direct python download link: https://www.python.org/downloads/.
1. If python package installer (pip) is working install the requirements. For that, get inside extracted project folder of "vjudge-to-oj"(i.e: `C:\projects\vjudge-to-oj\`), write `cmd` clearing the addressbar if you are on Windows OS.
1. Then write ```pip install -r requirements.txt``` on cmd. This should install most of the dependencies/packages.
1. That should do the work, check out the next section. Anywhere in the next section if it says a package is missing, try installing that package with pip from cmd. i.e: ```pip install foo-package-name```. Ignore this for now.

Here is an example for 2nd and 3rd step:
![3rd and 4th step](http://g.recordit.co/4yQY4rhqBS.gif)

## How it should work:

0. Install all the dependencies and required packages and get the environment ready(Explained above)
1. Open cmd inside project directory again and write ```python main.py```
2. Insert Vjudge handle and password when asked or change
```
vjUserName = input("Please enter your vjudge username: ")
vjPassword = input("Please enter your vjudge password: ")
```
to
```
vjUserName = "yourVjudgeHandle"
vjPassword = "yourVjudgePassword"
```
inside main.py in case you don't like writing your username and password everytime you run it.

3. Insert Judge(UVa, CodeForces) handle and password when asked or set it as mentioned above.
4. The program will automatically download your Accepted solutions from vjudge and then submit them one by one and store the submitted solutions to another folder(modules>Submitted>UVA>).
5. It'll show you the status report as it runs. It may look messy but it actually helps you see what's going on.

* Default parameters of uvaUser.submitAll() and cfUser.submitAll() function is ```submitAll(submitSolvedOnes = False, limitSubmissionCount = 10)```. Change as you need. In case anything goes wrong, close the command prompt.
  * If submitSolvedOnes is set to True, it'll submit the solution regardless of your solve status to actual judge.
  * limitSubmissionCount is set to 10 for safety. It means it will submit upto 10 solutions and then stop the program. Change as required.
* It can automatically detect languages(C, C/C++, Java, Python) But as there are two versions of C++(C++ and C++11) in UVa and vjudge doesn't export that information, it's only submitted to C++11. There's a work-around I guess but it would be more complex. At least a large portion of submissions would surely get AC.
* No login data is bypassed/redirected to anywhere else. Vjudge login data is stored inside "vjudge-to-oj>modules>cookies" this directory. You can empty that folder if you're concerned or have issues loggin in.

**Please don't run it when UVa, CodeForces is already busy and many submissions are already in queue. It's built only for personal uses. This program is in no way meant to hamper the solving environment of a judging platform.**
