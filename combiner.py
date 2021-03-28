# -*- coding: utf-8 -*-

# This file combines all downloaded .bib and .bibtex files to a single .bib file (com.bib)

import csv
import glob
files = glob.glob('*.bib')
files.extend(glob.glob('*.bibtex'))
with open('com.bib', 'w') as result:
    for file in files:
        if len(file)<=12: continue # skip the combined file, usually with a shorter file name (<=12 incl. extension)
        for line in open( file, 'r' ):
            if line != '\n':
                result.write( line )
        result.write('\n'*2)
