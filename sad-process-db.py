""" Code to put results from sad-comparisons.py into database."""
from __future__ import division

import csv
import sys
import multiprocessing
import itertools
import os
import numpy as np
from math import log, exp
from scipy import stats
import sqlite3 as dbapi


# Function to import the AICc results.
def import_results(datafile):
    """Imports raw result .csv files in the form: site, S, N, logseries, logseries_untruncated, pln, negbin, geometric, zipf."""
    raw_results = np.genfromtxt(datafile, dtype = "S15, i8, i8, f8, f8, f8, f8, f8", skip_header = 1, 
                                names = ['site', 'S', 'N', 'logseries', 'pln', 'negbin', 'geometric','AICc_zipf'], delimiter = ",", missing_values = '', filling_values = '')
    return raw_results

# Function to determine the winning model for each site.
def winning_model(data_dir, dataset_name, results):
    # Open output files
    output_processed = csv.writer(open(data_dir + dataset_name + '_processed_results.csv','wb'))
    # Insert comment line
    output_processed.writerow(["# 0 = Logseries, 1 = Poisson lognormal, 2 = Negative binomial, 3 = Geometric series, 4 = Zipf distribution"])
    
    # Insert header
    output_processed.writerow(['dataset', 'site', 'S', 'N', "model_code", "model_name", "AICc_weight"])
   
    for site in results:
        site_results = site.tolist()
        site_ID = site_results[0]
        S = site_results[1]
        N = site_results[2]
        AICc_weights = site_results[3:]


        AICc_max_weight = max(AICc_weights) # This will return the actual AICc_weight of the winning model, given that the winning model is the one with the highest AICc weight.

        winning_model = AICc_weights.index(AICc_max_weight) # This will return the winning model, where the model is indicated by the index position
        
        if winning_model == 0:
            model_name = 'Logseries'
            
        elif winning_model == 1:
            model_name = 'Poisson lognormal'
            
        elif winning_model == 2:
            model_name = 'Negative binomial'
            
        elif winning_model == 3:
            model_name = 'Geometric series'
            
        else:
            model_name = 'Zipf distribution'

        # Format results for output
        processed_results = [[dataset_name] + [site_ID] + [S] + [N] + [winning_model] + [model_name] + [AICc_max_weight]]
        
                                        
        # Save results to a csv file:            
        output_processed.writerows(processed_results)
        
        # Save results to sqlite database      
        #Create database for simulated data """
        cur.execute("""CREATE TABLE IF NOT EXISTS ResultsWin
                       (dataset_code TEXT,
                        site TEXT,
                        S INTEGER,
                        N INTEGER,
                        model_code INTEGER,
                        model_name TEXT,
                        AICc_weight_model FLOAT)""")
           
        cur.executemany("""INSERT INTO ResultsWin VALUES(?,?,?,?,?,?,?)""", processed_results)
        con.commit()
        
    return processed_results
        
def process_results(data_dir, dataset_name, results, value_type):
    for site in results:
        site_results = site.tolist()
        site_ID = site_results[0]
        S = site_results[1]
        N = site_results[2]
        values = site_results[3:]
        counter = 0
        

        for index, value in enumerate(values):
            if index == 0:
                model_name = 'Logseries'
                processed_results = [[dataset_name] + [site_ID] + [S] + [N] + [index] + [model_name] + [value_type] + [value]]
            
            elif index == 1:
                model_name = 'Poisson lognormal'
                processed_results = [[dataset_name] + [site_ID] + [S] + [N] + [index] + [model_name] + [value_type] + [value]]
            
            elif index == 2:
                model_name = 'Negative binomial'
                processed_results = [[dataset_name] + [site_ID] + [S] + [N] + [index] + [model_name] + [value_type] + [value]]
            
            elif index == 3:
                model_name = 'Geometric series'
                processed_results = [[dataset_name] + [site_ID] + [S] + [N] + [index] + [model_name] + [value_type] + [value]]
                
            else:
                model_name = 'Zipf distribution'
                processed_results = [[dataset_name] + [site_ID] + [S] + [N] + [index] + [model_name] + [value_type] + [value]]

            # Save results to sqlite database      
            #Create database for simulated data """
            cur.execute("""CREATE TABLE IF NOT EXISTS RawResults
                       (dataset_code TEXT,
                        site TEXT,
                        S INTEGER,
                        N INTEGER,
                        model_code INTEGER,
                        model_name TEXT,
                        value_type TEXT,
                        value FLOAT)""")
           
            cur.executemany("""INSERT INTO RawResults VALUES(?,?,?,?,?,?,?,?)""", processed_results)
            con.commit()
        
    return processed_results   
# Set up analysis parameters
results_ext = '_dist_test.csv' # Extension for raw model AICc results files
likelihood_ext = '_likelihoods.csv' # Extension for raw model likelihood files
relative_ll_ext = '_relative_L.csv' # Extenstion for raw model relative likelihood files
database_name = input("Please provide the name of the output database. ")

data_dir = input("Please provide the path to the data directory. ")
if data_dir == None:
    data_dir == './sad-data/chapter1/' # path to data directory


datasets = input("Please provide a list of dataset ID codes. ")
if datasets == None:
    datasets == ['bbs', 'cbc', 'fia', 'gentry', 'mcdb', 'naba', 'Reptilia', 'Coleoptera', 'Arachnida', 'Amphibia', 'Actinopterygii'] # Dataset ID codes

# Asks for toggle variable so I don't have to rerun all the setup if it is already processed.
needs_processing = input("Data needs to be processed into an sqlite database, True or False?  ")  

# Starts actual processing for each set of results in turn.
if needs_processing == True:
    # Set up database capabilities 
    # Set up ability to query data
    database = data_dir + database_name
    con = dbapi.connect(database)
    cur = con.cursor()
    
    # Switch con data type to string
    con.text_factory = str
    drop_tables = input("Database needs to be rebuilt, True or False?  ")
    if drop_tables == True:
        cur.execute("""DROP TABLE IF EXISTS ResultsWin""")
        cur.execute("""DROP TABLE IF EXISTS RawResults""")
        con.commit()
        
        
    for dataset in datasets:
        datafile = data_dir + dataset + results_ext
        datafile2 = data_dir + dataset + likelihood_ext
        datafile3 = data_dir + dataset + relative_ll_ext
        
        raw_results = import_results(datafile) # Import AICc weight data
        
        raw_results_likelihood = import_results(datafile2) # Import log-likelihood data
        
        raw_results_relative_ll = import_results(datafile3) #Import relative likelihood data

        winning_model(data_dir, dataset, raw_results) # Finds the winning model for each site
        
        process_results(data_dir, dataset, raw_results, 'AICc weight') #Turns the raw results into a database.
        process_results(data_dir, dataset, raw_results_likelihood, 'likelihood') #Turns the raw results into a database.
        process_results(data_dir, dataset, raw_results_relative_ll, 'relative likelihood') #Turns the raw results into a database.
        
    
    #Close connection to database
    con.close()
    
    print("Database complete.")