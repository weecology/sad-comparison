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
        if ref_num[i] == None:
            item1 = ''
        else:    
            item1 = str(ref_num[i])
        if title[i] == None:
            item2 = ''
        else:
            item2 = title[i]
        if author[i] == None:
            item3 = ''
        else:
            item3 = author[i]
        if journal[i] == None:
            item4 = ''
        else:
            item4 = journal[i] 
        if volume[i] == None:
            item5 = ''
        else:    
            item5 = str(volume[i])
        if pages[i] == None:
            item6 = ''
        else:
            item6 = str(pages[i])
        if year[i] == None:
            item7 = ''
        else:
            item7 = str(year[i]) 
            
        #Format reference entry
        try:
            ref_entry = '@article{' + item1 + ',\n title={' + item2 + '},\n author={' + item3 + '},\n journal={' + item4 + '},\n volume={' + item5 + '},\n pages={' + item6 + '},\n year={' + item7 + '}}\n'
    
            refs.writelines(ref_entry)
        except:
            print('Incomplete reference')
        
        
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