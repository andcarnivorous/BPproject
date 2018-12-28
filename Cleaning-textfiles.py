# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 13:09:38 2018

@author: Sa
"""

import re
import codecs
import os
in_files = os.listdir("C:/Users/Sa/Dropbox/Education/Premaster CIS/Basic Programming/python/Bp-project-text-files")
for _file in in_files:
    if _file.endswith(".txt"):
        
        text=codecs.open("C:/Users/Sa/Dropbox/Education/Premaster CIS/Basic Programming/python/Bp-project-text-files/"+_file , "r",encoding="utf-8",errors="ignore")
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
        
        text=codecs.open("C:/Users/Sa/Dropbox/Education/Premaster CIS/Basic Programming/python/Bp-project-text-files/"+_file , "r",encoding="utf-8",errors="ignore")
        text=text.read()
        if "Author:" not in text:
            print(_file)
            in_files.remove(_file)
print(len(in_files))
 
# =============================================================================
#                
# =============================================================================
for _file in in_files:
    if _file.endswith(".txt"):
        
        text=codecs.open("C:/Users/Sa/Dropbox/Education/Premaster CIS/Basic Programming/python/Bp-project-text-files/"+_file , "r",encoding="utf-8",errors="ignore")
        text=text.read()
        title = re.search(r"Title:([\.\w ]+)",text).group(1)
        #author = re.search(r"Author:([\.\w ]+)",text)
        print(title)
        file_name = title
        file_name = re.sub("[\. ,]+", "-", file_name)
        file_name = file_name + ".txt"
        print(file_name)
        try:
            os.rename("C:/Users/Sa/Dropbox/Education/Premaster CIS/Basic Programming/python/Bp-project-text-files/"+_file ,"C:/Users/Sa/Dropbox/Education/Premaster CIS/Basic Programming/python/Bp-project-text-files/"+file_name)
        except:
            print(_file , "this is a double")
            continue
 


