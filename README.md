# vjudge-to-uva

How it should work:
1. Export all your submissions from vjudge profile
2. Copy the zip folder of your submissions to users folder. i.e: msabeer-ac.zip to users>msabeer-ac.zip
3. Run the program
4. Login to your UVa when asked

To-do:
1. Being able to read all the submissions
2. Submission object:
    1. judgeSlug(mapped from the folder name. i.e: Submissions>UVA)
    2. problemId(collected from subfolder of judge submissions. i.e: Submissions>UVA>104)
    3. problemName(collected from UVa api)
    4. Solutions
        1. Submission Code(all the files inside a problem id. i.e: Submissions>UVA>104>123124.cpp)
        2. Language mapping(from solution extention. i.e: Submissions>UVA>104>1231123.cpp)
3. Being able to open login link in browser
4. Being able to write on submission link
5. Being able to press submit button automatically
6. Store the submitted solution locally in a specific format("104 - Arbitrage.cpp") and verify if it got AC