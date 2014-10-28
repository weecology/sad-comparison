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
mainfile = './sad-data/chapter2/UlrichOllik2003.csv'
maintype ='S15,S15,S15,S15,S15,i8,f8,i8,S15,S15,S15,S15,f8,S15,i8,S15,i8,S15,i8,S15,S15,S15,S15,S15,S15,S15,S15,S15' #datatype list 
abundancefile = './sad-data/chapter2/UlrichOllik2003_abundance.csv'
abundancetype = 'S15,S15,S15,S15,S15,f8,i8,i8'#datatype list 


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
