""" Project code for graphing the results of the comparisions for species abundance distribution (SAD) models """

from __future__ import division

import csv
import sys
import multiprocessing
import itertools
import os
import matplotlib.pyplot as plt
import colorsys
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
        #Create database for simulated data """
        cur.execute("""CREATE TABLE IF NOT EXISTS RawResults
                       (dataset_code TEXT,
                        site TEXT,
                        S INTEGER,
                        N INTEGER,
                        model_code INTEGER, 
                        AICc_weight_model FLOAT)""")
           
        cur.executemany("""INSERT INTO RawResults VALUES(?,?,?,?,?,?)""", processed_results)
        con.commit()
        
    return processed_results
        
   
# Format output for graphing
def graphing_subsets(dataset, wins_by_dataset):
    models_list = []
    wins_count = []
    for win in wins_by_dataset:
        if win[0] == dataset:
            models_list.append(win[1])
            wins_count.append(win[2])     
    
    return models_list, wins_count


# Set up analysis parameters
data_dir = './sad-data/' # path to data directory
results_ext = '_dist_test.csv' # Extension for raw species abundance files

datasets = ['bbs', 'cbc', 'fia', 'gentry', 'mcdb', 'naba'] # Dataset ID codes

# Asks for toggle variable so I don't have to rerun all the setup if it is already processed.
needs_processing = input("Data needs to be processed into an sqlite database, True or False?  ")  
needs_processing = False # THIS LINE IS TEMPORARY AND NEEDS TO BE DELETED IN THE FINAL PRODUCT.

# Starts actual processing for each set of results in turn.
if needs_processing == True:
    # Set up database capabilities 
    # Set up ability to query data
    con = dbapi.connect('SummarizedResults.sqlite')
    cur = con.cursor()
    
    # Switch con data type to string
    con.text_factory = str    
    cur.execute("""DROP TABLE IF EXISTS RawResults""")
    con.commit()      
    for dataset in datasets:
        datafile = data_dir + dataset + results_ext
        
        raw_results = import_results(datafile) # Import data

        processed_results = winning_model(data_dir, dataset, raw_results) # Finds the winning model for each site
    
    #Close connection to database
    con.close()    

# Summarize the number of wins for each model/dataset
# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('SummarizedResults.sqlite')
cur = con.cursor()

# Switch con data type to string
con.text_factory = str

# Extract number of wins for each model and dataset
wins_by_dataset = cur.execute("""SELECT dataset_code, model_code, COUNT(model_code) AS total_wins FROM RawResults
                                 GROUP BY dataset_code, model_code""")
           
wins_by_dataset = cur.fetchall()

# Extract number of wins for all datasets combined.
total_wins = cur.execute("""SELECT model_code, COUNT(model_code) AS total_wins FROM RawResults
                            GROUP BY model_code""")

total_wins = cur.fetchall()


# Close connection
con.close()


# Make histogram
# Set up figure
fig1 = plt.figure()
ax = fig1.add_subplot(111)


# Plot variables
N = len(total_wins)
x = np.arange(1, N+1)
y = [ num for (s, num) in total_wins ]
labels = [ s for (s, num) in total_wins ]
width = 1
bar1 = plt.bar( x, y, width, color="y" )
plt.ylabel( 'Number of Wins' )
plt.xticks(x + width/2.0, labels )
plt.xlabel( 'Model ID' )
plt.show()


##Extract data by dataset
#bbs_models, bbs_wins = graphing_subsets('bbs', wins_by_dataset)
#cbc_models, cbc_wins = graphing_subsets('cbc', wins_by_dataset)
#fia_models, fia_wins = graphing_subsets('fia', wins_by_dataset)
#gentry_models, gentry_wins = graphing_subsets('gentry', wins_by_dataset)
#mcdb_models, mcdb_wins = graphing_subsets('mcdb', wins_by_dataset)
#naba_models, naba_wins = graphing_subsets('naba', wins_by_dataset)

## Create bars
#bbs_bars = ax.bar(ind, bbs_wins, width, color = 'black')
#cbc_bars = ax.bar(ind+width, cbc_wins, width, color = 'gray')
#fia_bars = ax.bar(ind+width+width, fia_wins, width, color = 'darkgreen')
#gentry_bars = ax.bar(ind+width+width+width, gentry_wins, width, color = 'limegreen')
#mcdb_bars = ax.bar(ind+width+width+width+width, mcdb_wins, width, color = 'sienna')
#naba_bars = ax.bar(ind+width+width+width+width+width, naba_wins, width, color = 'goldenrod')



