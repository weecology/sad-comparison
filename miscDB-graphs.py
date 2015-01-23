""" Script for graphing the Baldridge 2012 MiscDB for publication. """
import csv
import sys
import multiprocessing
import os
import numpy as np
import sqlite3 as dbapi
import re
import matplotlib.pyplot as plt
import numpy as np

sys.float_info[2]

# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('./sad-data/chapter2/misc.sqlite')
cur = con.cursor()
# Switch con data type to string
con.text_factory = str 

#Count the number of sites for each biogeographic region
bioregions = cur.execute("""SELECT DISTINCT(biogeographic_region) AS region, COUNT(site_id) AS sites FROM
                            miscabundancedb_sites
                            GROUP BY region""")
bioregions = cur.fetchall()

#Make bar graph of sites per biogeographic region

#Close connection
con.close()

