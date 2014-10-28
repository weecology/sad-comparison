""" Script for cleaning up and querying the Ulrich and Ollik 2003 data """
import csv
import sys
import multiprocessing
import os
import numpy as np
import sqlite3 as dbapi

sys.float_info[3]

def import_data(datafile):
    """Imports raw species abundance .csv files in the form: Site, Year, Species, Abundance."""
    raw_data = np.genfromtxt(datafile, delimiter = ",",comments = "#")
    return raw_data

#Stuff data into a real database
data_dir = './sad-data/chapter2/' # path to data directory
mainfile = './sad-data/chapter2/UlrichOllik2003.csv'
abundancefile = './sad-data/chapter2/UlrichOllik2003_abundance.csv'


# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('./sad-data/UlrichOllik2003.sqlite')
cur = con.cursor()
    
# Switch con data type to string
con.text_factory = str    
cur.execute("""DROP TABLE IF EXISTS RADmain""")
cur.execute("""DROP TABLE IF EXISTS abundance""")
con.commit() 


# Import .csv files
abundance_table =import_data(abundancefile)
main_table = import_data(mainfile)
print(abundance_table)

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
                        abundance FLOAT,
                        decimals INTEGER,
                        confidence INTEGER)""")
           
cur.executemany("""INSERT INTO abundance VALUES(?,?,?,?,?,?,?)""", abundance_table)
con.commit()
