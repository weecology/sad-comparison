""" Script for processing references for Baldridge 2012 database. """
import csv
import sys
import multiprocessing
import os
import numpy as np
import sqlite3 as dbapi
import re

sys.float_info[2]

# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('./sad-data/chapter2/misc.sqlite')
cur = con.cursor()
# Switch con data type to string
con.text_factory = str 

#Setup output file
refs_file = './sad-data/chapter2/miscDB_refs.bib'

with open(refs_file,'wb') as archive_file:
    refs = csv.writer(archive_file)