# vjudge-to-oj
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/m-s-abeer/vjudge-to-oj.svg)](https://github.com/m-s-abeer/vjudge-to-oj/blob/master/LICENSE)
[![GitHub forks](https://img.shields.io/github/forks/m-s-abeer/vjudge-to-oj.svg?style=social&label=Fork)](https://github.com/m-s-abeer/vjudge-to-oj)
[![GitHub stars](https://img.shields.io/github/stars/m-s-abeer/vjudge-to-oj.svg?style=social&label=Stars)](https://github.com/m-s-abeer/vjudge-to-oj)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fm-s-abeer%2Fvjudge-to-oj%2Fhit-counter&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

Competitive programmers spend hundreds and thousands of hours practicing programming problems and participating contests.
Vjudge has been an amazing platform for participating/hosting programming contests and problem-solving.

However, there can be scenarios where you'd like to add vjudge solutions to the actual judge profiles specifically.
I personally felt the need of it along with some of my friends and colleagues.
It's a tiresome job to submit all the solved problems of vjudge to the actual judges. This here is a small approach to get such works done easily.

Current solution will only work for **UVa**, **CodeForces**, **LightOj** and **SPOJ**. 
So far, it's pretty much stable and working just fine. It's roughly written and tested. But hey, it works!!!

With enough response and your contribution I hope to add some more judges here as well. Huge thanks to all who contributed so far to my fun projects.

Let me know if you have any questions/suggestions/feedbacks or simply if you liked it.

Email: mahmudsajjad.abeer@gmail.com

Hope you enjoy. <3
<hr>

## Installation Guide:
### With poetry(Easier):-
1. Download/clone the repository from github using git:-
   * Run `git clone https://github.com/m-s-abeer/vjudge-to-oj.git` from your cmd/terminal in your specified directory.
1. Download and install `python ^3.10` from here:- https://www.python.org/downloads/
1. Make sure you are using the desired python version by running `python --version`
1. Download and install `python-poetry`
   * Linux, MacOS, WSL:- `https://python-poetry.org/docs/#installing-with-the-official-installer`
   * Windows(powershell):- `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`
   * If none of the above worked or to know more:- https://python-poetry.org/docs/#installing-with-the-official-installer
1. Get inside project `vjudge-to-oj` and then write `poetry install` on cmd/terminal. This should install all the dependencies/packages.

### Without poetry:-
1. Download/clone the repository from github using git:-
   * Run `git clone https://github.com/m-s-abeer/vjudge-to-oj.git` from your cmd/terminal in your specified directory.
1. Download and install `python ^3.10` from here:- https://www.python.org/downloads/
1. Make sure you are using the desired python version by running `python --version`
1. Get inside project `vjudge-to-oj`
1. Write `python -m venv .venv` to create a python environment inside project. 
1. Write `source ./.venv/activate` for Linux, MacOS, WSL. For windows write `.\.venv\Scripts\activate` to activate the python environment
1. Run `pip install --upgrade pip` and then `pip install -r requirements.txt` to install all the dependencies/packages


## How it should work:
1. Complete the #installation-guide and run the following command inside project root from cmd/terminal to activate the environment:-
   * Poetry users: `poetry shell`
   * Linux, MacOS, WSL users: `source ./.venv/activate`
   * Windows users: `.\.venv\Scripts\activate`
2. Run `python main.py` from the project root
3. Set your Vjudge handle and password when asked. Or change the following code segment from `main.py` from
```
vjUserName = input("Please enter your vjudge username: ")
vjPassword = input("Please enter your vjudge password: ")
```
to
```
vjUserName = "yourVjudgeHandle"
vjPassword = "yourVjudgePassword"
```
in case you don't like writing your username and password everytime you run it.

4. Insert other judge handle and password(comment out those codes from `main.py` for the one's you don't need) when asked or set it as mentioned above. For LightOJ, you will require logging from a popup window as it has recaptcha.
5. The program will automatically download your Accepted solutions from vjudge and then submit them one by one and store the submitted solutions to another folder(modules>Submitted>UVA>).
6. It'll show you the status report as it runs. It may look messy, but it actually helps you see what's going on.
* Default parameters of uvaUser.submitAll() and cfUser.submitAll() function is ```submitAll(submitSolvedOnes = False, limitSubmissionCount = 10)```. Change as you need. In case anything goes wrong, close the command prompt.
  * If submitSolvedOnes is set to True, it'll submit the solution regardless of your solve status to actual judge.
  * limitSubmissionCount is set to 10 for safety. It means it will submit upto 10 solutions and then stop the program. Change as required.
* It can automatically detect languages(C, C/C++, Java, Python) But as there are two versions of C++(C++ and C++11) in UVa and vjudge doesn't export that information, it's only submitted to C++11. There's a work-around I guess but it would be more complex. At least a large portion of submissions would surely get AC.
* No login data is bypassed/redirected to anywhere else. Vjudge login data is stored inside "vjudge-to-oj>modules>cookies" this directory. You can empty that folder if you're concerned or have issues loggin in.

**N.B: Please don't run it when the corresponding judge is already busy and many submissions are already in queue. It's built only for personal uses. This program is in no way meant to hamper the solving environment of a judging platform.**
