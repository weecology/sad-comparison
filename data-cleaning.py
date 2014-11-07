""" Script for cleaning up and querying the Ulrich and Ollik 2003 data """
import csv
import sys
import multiprocessing
import os
import numpy as np
import sqlite3 as dbapi

sys.float_info[2]

def import_data(datafile,datatype):
    """Imports raw species abundance .csv files in the form: Site, Year, Species, Abundance."""
    raw_data = np.genfromtxt(datafile, dtype = datatype, skip_header = 1,delimiter = ",",comments = "#")
    return raw_data

#Stuff data into a real database
data_dir = './sad-data/chapter2/'
mainfile = './sad-data/chapter2/UlrichOllik2003.csv'
maintype ='S50,S50,S50,S50,S50,i8,f8,i8,S50,S50,S50,S50,f8,S50,i8,S50,i8,S50,i8,S50,S50,S50,S50,S50,S50,S50,S50,S50' #datatype list 
abundancefile = './sad-data/chapter2/UlrichOllik2003_abundance.csv'
abundancetype = 'S50,S50,S50,S50,S50,f8,i8,i8'#datatype list 


# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('./sad-data/chapter2/UlrichOllik2003.sqlite')
cur = con.cursor()
    
# Switch con data type to string
con.text_factory = str    
cur.execute("""DROP TABLE IF EXISTS RADmain""")
cur.execute("""DROP TABLE IF EXISTS abundance""")
con.commit() 


# Import .csv files
abundance_table =import_data(abundancefile, abundancetype)
main_table = import_data(mainfile, maintype)

# Add abundance data
cur.execute("""CREATE TABLE IF NOT EXISTS RADmain
                       (Code TEXT,
                       Author TEXT,
                       Title TEXT,
                       Bibliographic_data TEXT,
                       Data_type TEXT,
                       Species_number INTEGER,
                       Individuals_number FLOAT,
                       Repetition_number INTEGER,
                       Data_quality TEXT,
                       Continent TEXT,
                       Zone TEXT,
                       Habitat_type TEXT,
                       Area FLOAT,
                       Guild TEXT,
                       Guild_compl INTEGER,
                       Taxon TEXT,
                       Taxon_compl INTEGER,
                       Trophic_level TEXT,
                       Trophic level_compl INTEGER,
                       Disturbance TEXT,
                       Stability TEXT,
                       Anthropopressure TEXT,
                       Habitat TEXT,
                       Fractalness TEXT,
                       Succession TEXT,
                       Taxonomic_level TEXT,
                       Scale TEXT,
                       Completeness TEXT)""")

cur.executemany("""INSERT INTO RADmain VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", main_table)
con.commit()

# Add abundance data
cur.execute("""CREATE TABLE IF NOT EXISTS abundance
                       (code TEXT,
                        file_number TEXT,
                        file_order TEXT,
                        dataset_ID TEXT,
                        species TEXT,
                        abundance FLOAT,
                        decimals INTEGER,
                        confidence INTEGER)""")

cur.executemany("""INSERT INTO abundance VALUES(?,?,?,?,?,?,?,?)""", abundance_table)
con.commit()

#Query for communities that are in the RAD main database and have integer abundances
integer_communities= cur.execute("""SELECT dataset_ID, confidence, species, abundance FROM abundance
                            WHERE decimals == 0 AND code IS NOT NUll
                            ORDER BY dataset_ID""")
integer_communities = cur.fetchall()

#Output abundances
output_integer_communities = csv.writer(open(data_dir + 'RAD2003int' + '_spab.csv','wb'))
output_integer_communities.writerow(['dataset_ID', 'confidence', 'species', 'abundance']) #Output header
for row in integer_communities:
    output_integer_communities.writerow(row)

print("Complete.")

#Close connection
con.close()

# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('path-to-retriever-data.sqlite')
cur = con.cursor()
# Switch con data type to string
con.text_factory = str 

#Query for communities that are in the misc main database and have integer abundances
#Query for taxa
taxa = cur.execute("""SELECT Class FROM main
                      ORDER BY Class""")
taxa = cur.fetchall()


communities= cur.execute("""SELECT Class, Site_ID, Citation, (Genus || Species) AS species, Abundance FROM abundance
                            WHERE Abundance IS NOT 0
                            ORDER BY Site_ID""")
communities = cur.fetchall()

for taxon in taxa:
    #Run through communities, pull out all data that matches the taxon and output as a .csv
    #Output abundances
    output_communities = csv.writer(open(data_dir + taxon + '_spab.csv','wb'))
    output_communities.writerow(['site_ID', 'citation', 'species', 'abundance']) #Output header
    for row in communities:
        if row[0] == taxon:
            output_communities.writerow(row[1:])    
    