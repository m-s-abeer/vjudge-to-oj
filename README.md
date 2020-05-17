# vjudge-to-uva

How it should work:
1. Run main.py
2. Insert Vjudge handle and password
3. Insert Judge(UVa) handle and password
4. The program will automatically submit accepted solutions from vjudge one by one and store the accepted solutions to another folder when it get ac on judge as well
5. Show you the status report.

To-do:
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