import matplotlib
import random
from ftplib import FTP

ftp = FTP('ftp.ibiblio.org')

ftp.login()

print("connected")

ftp.cwd("pub/docs/books/gutenberg/") #change working directory

home = "/pub/docs/books/gutenberg/" #change working directory

print("home now")



print(ftp.nlst())

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
    
# =============================================================================
# 

def digger():
# THIS FUNCTION GETS A LIST OF THE FIRST 2 LAYERS OF DIRECTORIES
    counter = 0
    list_of_dirs = []
    second_list = []
    #uses the getdirs function to get the first layer
    list_of_dirs.extend(getdirs())

    print("LIST: ", list_of_dirs)
    
    if len(list_of_dirs) > 0:
        #first for loop gets the second layer
        for directory in list_of_dirs:

            ftp.cwd(directory) #cwd = change working directory

            second_list.append(ftp.pwd())
            for _dir in getdirs():

                final = str(ftp.pwd()) + "/" + str(_dir)

                second_list.append(final)


            counter += 1
            ftp.cwd("..")

    #once the first two layers are done the worm function starts to dig
    lista = worm(second_list)

            
    return lista

# =============================================================================
# 
# =============================================================================
def worm(_list):
    #this function is supposed to dig down 2 levels
    out_file = open("writingdirs.txt", "w")
    _list = _list
    idx = 0
#    idx = len(_list)
    final_list = []
    lenlist = len(_list)

    counter = 0
    extra = 0
    print("Worm Function")

    while counter < 1:

# This is like this because it would be nice to make it more efficient 
# And able to crawl the whole tree.

        try:
            if len(_list) > 1:
                counter += 1
                print(len(_list[-idx:]))
                for directory in _list:
                    #go in the X directory in the list
                    ftp.cwd(directory) #cwd = change working directory

                    for _dir in getdirs():
                        # for each directory in this new directory
                        # get the name of the new dirs and add them to the
                        # next ones to dig into
                        final = str(ftp.pwd()) + "/" + str(_dir)
 
                        print(final) #THSI IS THE PRINTED DIR
                        out_file.writelines(final + "\n")
                        if final not in final_list:
                            # if these dirs are not in the list of dirs to dig, add them
                            # otherwise skip them
                            final_list.append(final)
                            _list.append(final)
                            extra += 1
                    # go back to the previous dir in order to start again
                    ftp.cwd("..")
                idx = extra
            elif len(_list) > 100:
                break
            else:
                break
        except:
            continue

    out_file.close()
    return final_list


digger()


with open("writingdirs.txt", "r") as _dirs:
    _dirs = _dirs.readlines()

print(_dirs[:10])

for _dir in _dirs:
    try:
        _dir = _dir.rstrip()
        ftp.cwd(_dir)
        print(ftp.pwd())
        txtdownload()
        ftp.cwd(home)
    except:
        continue
    
