import os
from zipfile import ZipFile

rootDir = os.getcwd()

# Extracting user submissions
zipDir = rootDir + os.sep + "files" + os.sep + "zip-files"
extractedDir = rootDir + os.sep + "files" + os.sep + "extracted"

def extractZip(sourcePath, destinationPath, folderName = ""):
    with ZipFile(sourcePath, 'r') as zipFile:
        zipFile.extractall(destinationPath + os.sep + folderName)

listOfZips = os.listdir(zipDir)
for zipName in listOfZips:
    # folderName = zipName.split('.')[0]
    extractZip(zipDir + os.sep + zipName, extractedDir + os.sep)
    
    break # for now, it will run for single zip only


