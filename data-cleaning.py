""" Script for cleaning up and querying the Ulrich and Ollik 2003 data """
import csv
import sys
import multiprocessing
import os
import numpy as np
import sqlite3 as dbapi

#Stuff data into a real database
data_dir = './sad-data/chapter2' # path to data directory


# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('./sad-data/UlrichOllik2003.sqlite')
cur = con.cursor()
    
# Switch con data type to string
con.text_factory = str    
cur.execute("""DROP TABLE IF EXISTS summary""")
cur.execute("""DROP TABLE IF EXISTS abundance""")
con.commit() 