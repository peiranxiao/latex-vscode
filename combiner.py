# -*- coding: utf-8 -*-
# This file combines all downloaded .bib and .bibtex files to a single .bib file (com.bib)

import glob
import os 

# set working dir
# cwd = r'E:\Documents\test'
# os.chdir(cwd)

files = glob.glob('*.bib')
files.extend(glob.glob('*.bibtex'))

with open('com.bib', 'w', encoding='utf-8') as result:
    for file in files:
        if len(file)<=12 | (sum(c.isdigit() for c in file)<=1): 
            continue # skip the combined file, usually with a shorter file name (<=12 incl. the extension ".bib")
        for line in open( file, 'r', encoding='utf-8'):
            if line == '\n': continue
            result.write( line )
        result.write('\n'*2)