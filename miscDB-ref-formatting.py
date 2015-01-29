""" Script for processing references for Baldridge 2012 database. """
import csv
import sys
import multiprocessing
import os
import numpy as np
import sqlite3 as dbapi
import re

sys.float_info[2]

#Make reference
def bib_reference(ref_num, title, author, journal, volume, number, pages, year, publisher):
    ref_entry = '@article{' + str(ref_num) + ',\n title={' + title + '},\n author={' + author + '},\n journal={' + journal + '},\n volume={' + volume + '},\n number={' + number + '},\n pages={' + pages + '},\n year={' + year + '},\n publisher={' + publisher + '}}\n'
    
    refs = open('./miscDB_refs.bib','w')
    refs.writelines(ref_entry)
    refs.close()
    ref_num += 1
    return ref_num


# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('./sad-data/chapter2/misc.sqlite')
cur = con.cursor()
# Switch con data type to string
con.text_factory = str 

# Set up parameters
ref_num = 1

reference = bib_reference(ref_num, 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test')