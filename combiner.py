# -*- coding: utf-8 -*-
import csv
import glob
files = glob.glob('*.bib')
files.extend(glob.glob('*.bibtex'))
with open('com.bib', 'w') as result:
    for file in files:
        if len(file)<=12: continue
        for line in open( file, 'r' ):
            if line != '\n':
                result.write( line )
        result.write('\n'*2)
