#import datacleaner
import matplotlib
import random
from ftplib import FTP

# =============================================================================
# Define functions
# =============================================================================

def handleDownload(block, fileToWrite):
    # callback handler for the ftp.retrbinary function
    fileToWrite.write(block) 


def txtdownload():
    for _file in ftp.nlst():
        # for each txt file in the directory, create a file with the same name and copy the contents locally.
        if _file.endswith(".txt"):
            fileToWrite = open(_file, "wb")
            ftp.retrbinary("RETR %s" % _file, fileToWrite.write) #retrieve a copy of the file
            print("Writing: %s" % _file)
            fileToWrite.close()

def getdirs():
    list_dirs = []
    for _dir in ftp.nlst():
        # for all files in the directory, if that whole filename can be converted to a digit, it is a dir.
        if str(_dir).isdigit():
            list_dirs.append(_dir)

    return list_dirs

# =============================================================================
# this first section establishes the connection with the Gutenberg's ftp server
# =============================================================================
print("Connecting...")

ftp = FTP('ftp.ibiblio.org')

ftp.login()

print("Connected")

ftp.cwd("pub/docs/books/gutenberg/") #change working directory

home = "/pub/docs/books/gutenberg/" 

print("Home directory now")


out_file = open("writingdirs.txt", "w") # File where to save the directories for later use.

# =============================================================================
# 
# =============================================================================

dirs = []

for x in range(1,6):
    # Creates the list of base directories in the ftp Gutenberg server to then dig into.
    # range can go from 1 to 10 in all these 3 layers
    for y in range(0,10):
        for z in range(0,10):
            newdir = "/pub/docs/books/gutenberg/%s/%s/%s" % (x,y,z)
            dirs.append(newdir)

for _dir in dirs:
    # for each directory in the ones listed, if it exists, go into it, go one level deeper
    try:
        ftp.cwd(_dir)
        dirs2 = getdirs()
        for _dir2 in dirs2:
            try:
                #if these directories exist, write them in the directory list txt file
                print(_dir2)
                final = str(ftp.pwd()) + "/" + str(_dir2)
                print(final)
                out_file.writelines(final + "\n")
            except:
                continue
        ftp.cwd(home)
    except:
        continue

# close the directory list txt file
out_file.close()
    
print("Got all directories")
print("Starting to find and download books now...\n")

with open("writingdirs.txt", "r") as _dirs:
    _dirs = _dirs.readlines()

for _dir in _dirs:
    #for each directory saved in the txt file, go in that directory and download all the txt files.
    try:
        _dir = _dir.rstrip()
        ftp.cwd(_dir)
        print(ftp.pwd())
        txtdownload()
        ftp.cwd(home)
    except:
        continue
