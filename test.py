import os
from objects import Submission
from requests import session

# Quick Submit Link: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25
# Login Link: https://onlinejudge.org/
# stackoverflow.com/questions/20039643/how-to-scrape-a-website-that-requires-login-first-with-python

# rootDir = os.getcwd()
# extractedDir = rootDir + os.sep + "files" + os.sep + "extracted"
# problemDir = extractedDir + os.sep + "UVA" + os.sep + "104"

# lol = Submission(problemDir, "UVA", "104")

# payload = {
#     'action': 'Submit',
#     'mod_login_username': "abeer6764",
#     'mod_login_passwordtext': "testpass"
# }

# with session() as c:
#     tmp = c.post('https://onlinejudge.org/', data=payload)
#     response = c.get('https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25')
#     # print(response.headers)
#     # print(response.text)
#     with open('h.htm', "w") as f:
#         f.write(response.text)

##################################### Method 1
import mechanize
from bs4 import BeautifulSoup
import http.cookiejar

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = http.cookiejar.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
br.open('https://onlinejudge.org/')

# View available forms
# for f in br.forms():
#     print(f)

# Select the second (index one) form (the first form is a search query box)
br.select_form(nr=0)

# # User credentials
br.form['username'] = 'abeer6764'
br.form['passwd'] = 'testpass'

# # Login
res = br.submit()

h = br.open('https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=25').read()
# print(h)
with open('h.htm', "w") as f:
    f.write(h.decode("utf-8"))