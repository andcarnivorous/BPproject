#import datacleaner
import matplotlib
import random
from ftplib import FTP

ftp = FTP('ftp.ibiblio.org')

ftp.login()

print("connected")

ftp.cwd("pub/docs/books/gutenberg/") #change working directory

home = "/pub/docs/books/gutenberg/" 

print("home now")

print(ftp.nlst())

#out_file = open("writingdirs.txt", "w")

# =============================================================================
# 
# =============================================================================
def handleDownload(block, fileToWrite):
    fileToWrite.write(block)


def txtdownload():
    for _file in ftp.nlst():
        if _file.endswith(".txt"):
            fileToWrite = open(_file, "wb")
            ftp.retrbinary("RETR %s" % _file, fileToWrite.write) #retrieve a copy of the file
            print("Writing: %s" % _file)
            fileToWrite.close()

def getdirs():
    list_dirs = []
    for _dir in ftp.nlst():
        if str(_dir).isdigit():
            list_dirs.append(_dir)

    return list_dirs
"""
dirs = []

for x in range(0,2):
    for y in range(0,10):
        for z in range(0,10):
            newdir = "/pub/docs/books/gutenberg/%s/%s/%s" % (x,y,z)
            dirs.append(newdir)

for _dir in dirs:
    try:
        ftp.cwd(_dir)
        dirs2 = getdirs()
        for _dir2 in dirs2:
            try:
                print(_dir2)
                final = str(ftp.pwd()) + "/" + str(_dir2)
                print(final)
                out_file.writelines(final + "\n")
            except:
                continue
        ftp.cwd(home)
    except:
        continue

out_file.close()
    
print("FINEE")
"""
with open("writingdirs.txt", "r") as _dirs:
    _dirs = _dirs.readlines()

print(_dirs[:10])

for _dir in _dirs[:200]:
    try:
        _dir = _dir.rstrip()
        ftp.cwd(_dir)
        print(ftp.pwd())
        txtdownload()
        ftp.cwd(home)
    except:
        continue
