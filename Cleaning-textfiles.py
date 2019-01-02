# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 13:09:38 2018

@author: Sa
"""

import re
import os
import filecleaner

# =============================================================================
# Define functions
# =============================================================================

def name_builder(_text):

    # find the title and author line and return them.
    title = re.search(r"Title:(.+)",_text).group(1)
    author = re.search(r"Author:(.+)",_text).group(1)
    
    print(title)
    print(author)
    return title,author

# =============================================================================
#                 
# =============================================================================

# Create the folders for man and women authors if they are not there.
if "Men" not in os.listdir():
    os.mkdir("Men")
if "Women" not in os.listdir():
    os.mkdir("Women")

in_files = os.listdir()
for _file in in_files:
    # find all the books, consider them only if they are in English
    if _file.endswith(".txt"):
        
        text= open(_file , "r",encoding="utf-8",errors="ignore")
        text=text.read()
        if "Language: English" not in text:
            print(_file)
            in_files.remove(_file)

for _file in in_files:
    if _file.endswith(".txt"):
        # of all the English books, consider only them that provide title and author formatted this way.
        text= open(_file , "r",encoding="utf-8",errors="ignore")
        text=text.read()
        if "Author:" not in text or "Title:" not in text:
            print(_file)
            in_files.remove(_file)

# =============================================================================
#                
# =============================================================================

for _file in in_files:

    if _file.endswith(".txt"):
        # Rename each file that made the selection as "author-book-title.txt"
        text= open(_file , "r",encoding="utf-8",errors="ignore")
        text= text.read()
        try:
            title, author = name_builder(text)
        except:
            continue

        file_name = author + title
        file_name = file_name.lstrip()
        file_name = re.sub("[\. ,\r]+", "-", file_name)
        file_name = re.sub("[\. ,\s\r]+", "-", file_name)
        file_name = file_name + ".txt"
        print(file_name)
            
        try:
            os.rename(_file ,file_name)
        except:
            print(_file , "this is a double")
            continue

# =============================================================================
# Put books in the Men or Women folder based on author's first name
# =============================================================================

#these are the txt files containing lists of first names.
with open("male_names.txt", "r") as malenames:
    malenames = malenames.readlines()

malenames = [name.lower().rstrip() for name in malenames]

with open("female_names.txt", "r") as femalenames:
    femalenames = femalenames.readlines()

femalenames = [name.lower().rstrip() for name in femalenames]

nono_files = ["male_names.txt","female_names.txt"]


for _file in os.listdir():
    # for each txt file in the folder, check if the first name is in either name list
    # if so, move the file into the corresponding dir.
    if _file.endswith(".txt") and _file not in nono_files:
        index = _file.find("-")
        print(_file[:index])
        if _file[:index].lower() in femalenames:
            print("Female! ", _file[:index])
            os.rename(_file,"./Women/"+_file)

        elif _file[:index].lower() in malenames:
            print("Male!", _file[:index])
            os.rename(_file,"./Men/"+_file)

            
os.chdir("Women")

# use the file cleaner to delete the first and last part of the books which usually contain metadata and info
# that might create bias in the machine.

for book in os.listdir():
    try:
        print(book)
        filecleaner.file_cleaner(book)
    except:
        continue

os.chdir("..")

os.chdir("Men")

for book in os.listdir():
    try:
        print(book)
        
        filecleaner.file_cleaner(book)
    except:
        continue
            
os.chdir("..")
