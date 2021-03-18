import bs4
import requests
import numpy

class ScraperCaller:

    def printProgressBar(self, iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):  # Progress bar loader
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
        # Print New Line on Complete
        if iteration == total:
            print()

    # Online
    def getCfGymContestList(self):    # Scrapping because CF has no API for Gym contest
        print("Fetching CodeForces Gym Contest List.")
        previousContestId = -1
        currentContestId = 0
        isLastPage = False  # We will break if we reached last page before 100 number page

        contestList = set()
        for page in range(100):     # We are assuming CF has at most 100 page of contest list
            pageURL = 'https://codeforces.com/gyms/page/' + str(page+1) + '?searchByProblem=false'
            pageRawdata = requests.get(pageURL)
            soup = bs4.BeautifulSoup(pageRawdata.text, "lxml")

            rowCount = 0
            for tr_tag in soup.find_all('tr'):              # Finding all 'tr' in page raw data
                for td_tag in tr_tag.find_all('td', attrs={'class': 'state'}):        # Finding all 'td' which has 'state' class in each 'tr'
                    for a_tag in td_tag.find_all('a'):          # finding all link in each selected 'td'
                        each_a = a_tag['href'].split('/')
                        contestID = each_a[2]
                        if(rowCount == 0):
                            currentContestId = contestID
                            rowCount += 1
                            if currentContestId == previousContestId:     # If reached last page of contest list we need to break the loop
                                isLastPage = True
                                break

                        contestList.add(contestID)
                        previousContestId = currentContestId            # Updating previous contest id with current contest id

                if isLastPage:
                    break

            if isLastPage:
                break

        return contestList

    # Online
    def getCfGymProblemList(self):  # scrapping because CF has no API for Gym Problem data
        contestList = self.getCfGymContestList()   # We need gym contest list for find all gym problem data
        print("Fetching CodeForces Gym Problem List (This may take upto 20 minutes):")
        numberOfContest  = len(contestList)
        self.printProgressBar(0, numberOfContest, prefix='Progress:', suffix='Complete', length=50)  # Initializing Progress Bar

        contestNumber=0
        skipped = 0         # a counter variable, if any contest skipped for some error then it will be updated
        problemList = dict()
        for contestID in contestList:
            contestNumber += 1
            contestProblemListPageURL = 'https://codeforces.com/gym/' + contestID
            try:
                pageRowData = requests.get(contestProblemListPageURL, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0'})

                soup = bs4.BeautifulSoup(pageRowData.text, "lxml")
                for div in soup.find_all('div', attrs={'style': 'float: left;'}):    # Finding a specific 'div' which has inline style css withh attribute float: left
                    for a_tag in div.find_all('a'):  # Finding all link in each selected 'div'
                        href = a_tag['href'].split('/')
                        problemID = href[2] + href[4]
                        problemName = a_tag.get_text()
                        problemList[problemID] = problemName
                        # print(problemID)
            except requests.exceptions.ConnectionError:
                print('Network connection failed on contest ' + contestID + '. Check your internet connection. Trying next contest.')
                skipped += 1
            except TimeoutError:
                print('Timeout on contest ' + contestID + ', trying next contest.')
                skipped += 1

            self.printProgressBar(contestNumber, numberOfContest, prefix='Progress:', suffix='Complete', length=50)         # Updating progress Bar

        if skipped > 0:
            print(skipped, ' CF Gym contest skipped.')

        return problemList

    # Online
    def getSPOJSolveData(self, username):
        """
            This will be use in retrive already solved problem list of user in Spoj
        """
        start = 0  # We want to check from very last submission
        self.submissions = []
        previous_Submission_ID = -1
        current_Submission_ID = 0

        isLastPage = False

        # We assuming an user has at most 1000 page of submission on spoj (a single page has 20 submission history)
        for page in range(1000):
            url = "https://www.spoj.com/status/" + username + "/all/start=" + str(start)

            start += 20  # Spoj show 20 submission list in a single page

            pageData = requests.get(url)

            soup = bs4.BeautifulSoup(pageData.text, "lxml")
            table_body = soup.find("tbody")

            # Check if the page retrieved has no submissions
            if len(table_body) == 1:
                return self.submissions

            rowCnt = 0
            for row in table_body:
                if isinstance(row, bs4.element.Tag):
                    if rowCnt == 0:
                        current_Submission_ID = row.contents[1].contents[0]

                        # if we reached the last submission before page 1000 then it showing same submission of last valid page
                        # we want to ignore them and break the loop
                        if current_Submission_ID == previous_Submission_ID:
                            isLastPage = True
                            break

                    rowCnt += 1
                    previous_Submission_ID = current_Submission_ID

                    # Problem Name/URL
                    uri = row.contents[5].contents[0]

                    problem_id = uri["href"].split('/')
                    problem_id = problem_id[2]
                    # Problem Status
                    status = str(row.contents[6])
                    if status.__contains__("accepted"):
                        self.submissions.append(problem_id)

            if isLastPage:
                break
        self.submissions = numpy.unique(self.submissions)
        # print(self.submissions)
        return self.submissions

