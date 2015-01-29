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
    #Open output file
    refs = open('./miscDB_refs.bib','w')
    
    #Get parts of references sorted out
    ref_num = [ ref_id for (ref_id, article_title, authors, journal_name, issue, page_nums, yr) in ref_data ]
    title = [ article_title for (ref_id, article_title, authors, journal_name, issue, page_nums, yr) in ref_data ]
    author = [ authors for (ref_id, article_title, authors, journal_name, issue, page_nums, yr) in ref_data ]
    journal = [ journal_name for (ref_id, article_title, authors, journal_name, issue, page_nums, yr) in ref_data ]
    volume = [ issue for (ref_id, article_title, authors, journal_name, issue, page_nums, yr) in ref_data ] 
    pages = [ page_nums for (ref_id, article_title, authors, journal_name, issue, page_nums, yr) in ref_data ] 
    year = [ yr for (ref_id, article_title, authors, journal_name, issue, page_nums, yr) in ref_data ]
        
    for i, v in enumerate(ref_data):
        #Format reference entry
        ref_entry = '@article{' + str(ref_num[i] + ',\n title={' + title[i] + '},\n author={' + author[i] + '},\n journal={' + journal[i] + '},\n volume={' + str(volume[i]) + '},\n pages={' + str(pages[i]) + '},\n year={' + str(year[i]) + '}}\n'
        #Output reference entry
        print(ref_entry)
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