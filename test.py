import os
from objects import Submission


rootDir = os.getcwd()
extractedDir = rootDir + os.sep + "files" + os.sep + "extracted"
problemDir = extractedDir + os.sep + "UVA" + os.sep + "104"

lol = Submission(problemDir, "UVA", "104")