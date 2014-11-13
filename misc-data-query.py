""" Script for querying the Baldridge 2012 MiscDB. """
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

#Query for communities that are in the misc main database and have integer abundances
#Query for taxa
taxa = cur.execute("""SELECT DISTINCT Class FROM miscabundancedb_main
                      WHERE Class IS NOT 'Chondrichthyes' AND Class IS NOT 'Aves'
                      ORDER BY Class""") #Excludes Chondrichthyes because that class has too few species. (2, for 2 sites), and Aves, because it has no integer abundance data."
taxa = cur.fetchall()


communities= cur.execute("""SELECT Class, Site_ID, Citation, (Genus ||" "|| Species) AS species, Abundance FROM
                            miscabundancedb_main
                            WHERE Abundance IS NOT NULL AND Abundance IS NOT 0
                            ORDER BY Site_ID""")
communities = cur.fetchall()

#Close connection
con.close()

for taxa_class in taxa:
    taxon_str = str(taxa_class)
    taxon = findall(r"\'([A-Za-z]+)\'", taxon_str) #Strips out just the taxon name
    #Run through communities, pull out all data that matches the taxon and output as a .csv
    #Output abundances
    output_file = './sad-data/chapter1/' + taxon[0] + '_spab.csv'
    with open(output_file,'wb') as archive_file:
        output_communities = csv.writer(archive_file)
        output_communities.writerow(['site_ID', 'citation', 'species', 'abundance']) #Output header
        for row in communities:
            if row[0] == taxon[0]:
                output_communities.writerow(row[1:])    
    
print("Complete.")
    