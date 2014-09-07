""" Project code for graphing the results of the comparisions for species abundance distribution (SAD) models """

from __future__ import division

import csv
import sys
import multiprocessing
import itertools
import os
import matplotlib.pyplot as plt
import numpy as np
from math import log, exp
from scipy import stats
import sqlite3 as dbapi

from mpl_toolkits.axes_grid.inset_locator import inset_axes

# Function to import the AICc results.
def import_results(datafile):
    """Imports raw result .csv files in the form: site, S, N, AICc_logseries, AICc_logseries_untruncated, AICc_pln, AICc_negbin, AICc_geometric."""
    raw_results = np.genfromtxt(datafile, dtype = "S15, i8, i8, f8, f8, f8, f8, f8", skip_header = 1,
                      names = ['site', 'S', 'N', 'AICc_logseries', 'AICc_logseries_untruncated', 'AICc_pln', 'AICc_negbin', 'AICc_geometric'], delimiter = ",", missing_values = '', filling_values = '', )
    return raw_results

# Function to determine the winning model for each site.
def winning_model(data_dir, dataset_name, results):
    # Open output files
    output_processed = csv.writer(open(data_dir + dataset_name + '_processed_results.csv','wb'))
    # Insert comment line
    output_processed.writerow(["# 0 = Logseries, 1 = Untruncated logseries, 2 = Poisson lognormal, 3 = Negative binomial, 4 = Geometric series"])
    
    # Insert header
    output_processed.writerow(['dataset', 'site', 'S', 'N', "model_code", "AICc_weight_model"])
   
    for site in results:
        site_results = site.tolist()
        site_ID = site_results[0]
        S = site_results[1]
        N = site_results[2]
        AICc_weights = site_results[3:]


        AICc_min_weight = min(AICc_weights) # This will return the actual AICc_weight of the winning model, given that the winning model is the one with the lowest AICc weight.

        winning_model = AICc_weights.index(AICc_min_weight) # This will return the winning model, where the model is indicated by the index position
        # 0 = Logseries
        # 1 = Untruncated logseries
        # 2 = Poisson lognormal
        # 3 = Negative binomial
        # 4 = Geometric series

        # Format results for output
        processed_results = [[dataset_name] + [site_ID] + [S] + [N] + [winning_model] + [AICc_min_weight]]
        
                                        
        # Save results to a csv file:            
        output_processed.writerows(processed_results)
        
        # Save results to sqlite database
        # Set up database capabilities 
        # Set up ability to query data
        con = dbapi.connect('SummarizedResults.sqlite')
        cur = con.cursor()
        
        # Switch con data type to string
        con.text_factory = str
        
        #Create database for simulated data """
        cur.execute("""DROP TABLE IF EXISTS RawResults""")
        con.commit()          
        cur.execute("""CREATE TABLE IF NOT EXISTS RawResults
                        (dataset_code TEXT,
                         site TEXT,
                         S INTEGER,
                         N INTEGER,
                         model_code INTEGER, 
                         AICc_weight_model FLOAT)""")
           
        cur.executemany("""INSERT INTO RawResults VALUES(?,?,?,?,?,?)""", processed_results)
        con.commit()
        
        con.close()
        
        
    return processed_results
        
   
# Function to make histograms.

# Set up analysis parameters
data_dir = './sad-data/' # path to data directory
results_ext = '_dist_test.csv' # Extension for raw species abundance files

datasets = ['bbs', 'cbc', 'fia', 'gentry', 'mcdb', 'naba'] # Dataset ID codes

needs_processing = False # Toggle variable so I don't have to rerun all the setup if it is already processed. 

# Starts actual processing for each set of results in turn.
if needs_processing == True:
    for dataset in datasets:
        datafile = data_dir + dataset + results_ext
        
        raw_results = import_results(datafile) # Import data

        processed_results = winning_model(data_dir, dataset, raw_results) # Finds the winning model for each site

# Summarize the number of wins for each model/dataset
# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('SummarizedResults.sqlite')
cur = con.cursor()

# Switch con data type to string
con.text_factory = str
wins_by_dataset = cur.execute("""SELECT dataset_code, model_code, COUNT(model_code) AS total_wins FROM RawResults
                                 GROUP BY dataset_code, model_code""")
           
wins_by_dataset = cur.fetchall()

con.close()


print(wins_by_dataset)