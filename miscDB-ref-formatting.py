""" Script for processing references for Baldridge 2012 database. """
import csv
import sys
import multiprocessing
import os
import numpy as np
import sqlite3 as dbapi
import re

sys.float_info[2]

#Make references
def bib_reference(ref_data):
    refs = open('./miscDB_refs.bib','w')
    
    for row in ref_data:
        ref_num = [ ref_id for (ref_id, article_title, authors, journal_name, issue, page_nums, yr) in row ]
        title = [ article_title for (ref_id, article_title, authors, journal_name, issue, page_nums, yr) in row ]
        author = [ authors for (ref_id, article_title, authors, journal_name, issue, page_nums, yr) in row ]
        journal = [ journal_name for (ref_id, article_title, authors, journal_name, issue, page_nums, yr) in row ]
        volume = [ issue for (ref_id, article_title, authors, journal_name, issue, page_nums, yr) in row ] 
        pages = [ page_nums for (ref_id, article_title, authors, journal_name, issue, page_nums, yr) in row ] 
        yr = [ yr for (ref_id, article_title, authors, journal_name, issue, page_nums, yr) in row ]
    
        #Format reference entry
        ref_entry = '@article{' + str(ref_num) + ',\n title={' + title + '},\n author={' + author + '},\n journal={' + journal + '},\n volume={' + volume + '},\n pages={' + pages + '},\n year={' + year + '}}\n'
    
        refs = open('./miscDB_refs.bib','w')
        refs.writelines(ref_entry)
        
    refs.close()



# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('./sad-data/chapter2/misc.sqlite')
cur = con.cursor()
# Switch con data type to string
con.text_factory = str 

# Extract reference data.
ref_data = cur.execute("""SELECT rowid AS ref_num, title, authors, journal, issue, pages, yr FROM
                            miscabundancedb_citations""")
ref_data = cur.fetchall()

references = bib_reference(ref_data)