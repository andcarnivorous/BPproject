# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 14:28:56 2018

@author: Sa
"""

import re

def file_cleaner (_file):
    in_file = open(_file, encoding="utf-8", errors = "ignore")
    lines = in_file.read()
    regex = re.search("\*\*\*\n" , lines )
    print(regex)
    beginning,end = regex.span()
    lines = lines[end:]
    regex = re.search("\*\*\*\s.+\n", lines)
    print(regex)
    beginning,end = regex.span() # in between here is the wanted text 
    lines = lines[:beginning]
    
    to_write = open(_file , "w")
    to_write.write(lines)
    to_write.close()
    
    
    

