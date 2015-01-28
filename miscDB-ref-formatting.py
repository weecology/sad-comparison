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
    ref_entry = '@article{' + ref_num + ', title={' + title + '}, author={' + author + '}, journal={' + journal + '}, volume={' + volume + '}, number={' + number + '}, pages={' + pages + '}, year={' + year + '}, publisher={' + publisher + '}}'
    
    with open('./sad-data/chapter2/miscDB_refs.bib','w') as archive_file:
        refs = write(archive_file)
        refs.writelines(ref_entry)


# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('./sad-data/chapter2/misc.sqlite')
cur = con.cursor()
# Switch con data type to string
con.text_factory = str 
