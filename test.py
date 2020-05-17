# import os
# from modules.submissions import Submission
# from requests import session

# # Quick Submit Link: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25
# # Login Link: https://onlinejudge.org/
# # stackoverflow.com/questions/20039643/how-to-scrape-a-website-that-requires-login-first-with-python

# # rootDir = os.getcwd()
# # extractedDir = rootDir + os.sep + "files" + os.sep + "extracted"
# # problemDir = extractedDir + os.sep + "UVA" + os.sep + "104"

# # lol = Submission(problemDir, "UVA", "104")

# import mechanize
# from bs4 import BeautifulSoup
# import http.cookiejar

# # Browser
# br = mechanize.Browser()

# # Cookie Jar
# cj = http.cookiejar.LWPCookieJar()
# br.set_cookiejar(cj)

# # Browser options
# br.set_handle_equiv(True)
# br.set_handle_gzip(True)
# br.set_handle_redirect(True)
# br.set_handle_referer(True)
# br.set_handle_robots(False)
# br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# br.addheaders = [('User-agent', 'Chrome')]

# # The site we will navigate into, handling it's session
# br.open('https://onlinejudge.org/')

# # View available forms
# # for f in br.forms():
# #     print(f)

# # Select the second (index one) form (the first form is a search query box)
# br.select_form(nr=0)

# # # User credentials
# br.form['username'] = 'abeer6764'
# br.form['passwd'] = 'testpass'

# # # Login
# res = br.submit()
# # print(res.geturl())

# # with open('h.htm', "w") as f:
# #     f.write(res.read().decode("utf-8"))

# br.open('https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25')
# for f in br.forms():
#     print(f)

# br.select_form(nr=1)
# br.form['localid'] = "100"
# br.form.find_control(name="language").value = ["5"]
# br.form.find_control(name="code").value = "abc"
# res = br.submit()
# submissionId = res.geturl().split('+')[-1]
# # # print(h)
# # with open('h.htm', "w") as f:
# #     f.write(h.decode("utf-8"))

# # import time
# # from wrapt_timeout_decorator import *

# # @timeout(5)
# # def mytest(message):
# #     # this example does NOT work on windows, please check the section
# #     # "use with Windows" in the README.rst
# #     print(message)
# #     for i in range(1,10):
# #         time.sleep(1)
# #         print('{} seconds have passed'.format(i))

# # if __name__ == '__main__':
# #     mytest('starting')
# sys.path.append('modules')
# from modules.judges import Vjudge

# lol = Vjudge("abeer6764", "testpass")
# lol.login()
# lol.downloadSubmissions()
# lol.extractZip()