# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 13:09:38 2018

@author: Sa
"""

import re
import codecs
import os
import filecleaner

in_files = os.listdir()
for _file in in_files:
    if _file.endswith(".txt"):
        
        text=codecs.open(_file , "r",encoding="utf-8",errors="ignore")
        text=text.read()
        if "Language: English" not in text:
            print(_file)
            in_files.remove(_file)

print(len(in_files))

# =============================================================================
#                 
# =============================================================================

for _file in in_files:
    if _file.endswith(".txt"):
        
        text=codecs.open(_file , "r",encoding="utf-8",errors="ignore")
        text=text.read()
        if "Author:" not in text or "Title:" not in text:
            print(_file)
            in_files.remove(_file)

print(len(in_files))

# =============================================================================
#                
# =============================================================================

def name_builder(_text):

    title = re.search(r"Title:(.+)",_text).group(1)
    author = re.search(r"Author:(.+)",_text).group(1)
    print(title)
    print(author)
    return title,author

for _file in in_files:

    if _file.endswith(".txt"):
        text=codecs.open(_file , "r",encoding="utf-8",errors="ignore")
        text=text.read()
        title, author = name_builder(text)

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
### COMMENT UNTIL HERE

with open("male_names.txt", "r") as malenames:
    malenames = malenames.readlines()

malenames = [name.rstrip() for name in malenames]

with open("female_names.txt", "r") as femalenames:
    femalenames = femalenames.readlines()

femalenames = [name.rstrip() for name in femalenames]

print(femalenames)

nono_files = ["male_names.txt","female_names.txt"]


counter = 0
for _file in os.listdir():
    if _file.endswith(".txt") and _file not in nono_files:
        index = _file.find("-")
        if _file[:index] in femalenames:
            print("Female! ", _file[:index])
            os.rename(_file,"./Women/"+_file)
            counter += 1
        elif _file[:index] in malenames:
            counter += 1
            os.rename(_file,"./Men/"+_file)
            print("Male!", _file[:index])
            
os.chdir("Women")

for book in os.listdir():
    try:
        print(book)
        
        filecleaner.file_cleaner(book)
        count+=1
    except:
        continue

os.chdir("..")

os.chdir("Men")

for book in os.listdir():
    try:
        print(book)
        
        filecleaner.file_cleaner(book)
        count+=1
    except:
        continue
            
os.chdir("..")
