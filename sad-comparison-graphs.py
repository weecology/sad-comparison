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


        AICc_max_weight = max(AICc_weights) # This will return the actual AICc_weight of the winning model, given that the winning model is the one with the highest AICc weight.

        winning_model = AICc_weights.index(AICc_max_weight) # This will return the winning model, where the model is indicated by the index position
        
        if winning_model == 0:
            model_name = 'Logseries'
            
        elif winning_model == 1:
            model_name = 'Untruncated logseries'
            
        elif winning_model == 2:
            model_name = 'Poisson lognormal'
            
        elif winning_model == 3:
            model_name = 'Negative binomial'
            
        else:
            model_name = 'Geometric series'

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
        
def process_AICcs(data_dir, dataset_name, results):
    for site in results:
        site_results = site.tolist()
        site_ID = site_results[0]
        S = site_results[1]
        N = site_results[2]
        AICc_weights = site_results[3:]
        counter = 0
        

        for index, AICc_weight in enumerate(AICc_weights):
            if index == 0:
                model_name = 'Logseries'
                processed_results = [[dataset_name] + [site_ID] + [S] + [N] + [index] + [model_name] + [AICc_weight]]
            
            elif index == 1:
                model_name = 'Untruncated logseries'
                processed_results = [[dataset_name] + [site_ID] + [S] + [N] + [index] + [model_name] + [AICc_weight]]
            
            elif index == 2:
                model_name = 'Poisson lognormal'
                processed_results = [[dataset_name] + [site_ID] + [S] + [N] + [index] + [model_name] + [AICc_weight]]
            
            elif index == 3:
                model_name = 'Negative binomial'
                processed_results = [[dataset_name] + [site_ID] + [S] + [N] + [index] + [model_name] + [AICc_weight]]
            
            else:
                model_name = 'Geometric series'
                processed_results = [[dataset_name] + [site_ID] + [S] + [N] + [index] + [model_name] + [AICc_weight]]

            # Save results to sqlite database      
            #Create database for simulated data """
            cur.execute("""CREATE TABLE IF NOT EXISTS RawResults
                       (dataset_code TEXT,
                        site TEXT,
                        S INTEGER,
                        N INTEGER,
                        model_code INTEGER,
                        model_name TEXT,
                        AICc_weight_model FLOAT)""")
           
            cur.executemany("""INSERT INTO RawResults VALUES(?,?,?,?,?,?,?)""", processed_results)
            con.commit()
        
    return processed_results   
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
    con = dbapi.connect('./sad-data/SummarizedResults.sqlite')
    cur = con.cursor()
    
    # Switch con data type to string
    con.text_factory = str    
    cur.execute("""DROP TABLE IF EXISTS ResultsWin""")
    cur.execute("""DROP TABLE IF EXISTS RawResults""")
    con.commit() 
    for dataset in datasets:
        datafile = data_dir + dataset + results_ext
        
        raw_results = import_results(datafile) # Import data

        processed_results = winning_model(data_dir, dataset, raw_results) # Finds the winning model for each site
        
        process_AICcs(data_dir, dataset, raw_results) #Turns the raw results into a database.
    
    #Close connection to database
    con.close()    

# Summarize the number of wins for each model/dataset
# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('./sad-data/SummarizedResults.sqlite')
cur = con.cursor()

# Switch con data type to string
con.text_factory = str




# Make histogram
# Set up figure
total_wins_fig= plt.figure()

# Extract number of wins for all datasets combined.
total_wins = cur.execute("""SELECT model_name, COUNT(model_code) AS total_wins FROM ResultsWin
                            GROUP BY model_code""")

total_wins = cur.fetchall()


# Plot variables for total wins
N = len(total_wins)
x = np.arange(1, N+1)
y = [ num for (s, num) in total_wins ]
labels = [ s for (s, num) in total_wins ]
width = 1
bar1 = plt.bar( x, y, width, color="grey" )
plt.ylabel( 'Number of Wins' )
plt.xticks(x + width/2.0, labels, fontsize = 'small' )
plt.xlabel( 'Species abundance distribution models' )
plt.show()


#Output figure
fileName = "./sad-data/total_wins.png"
plt.savefig(fileName, format="png" )




# Extract number of wins for each model and dataset
# BBS
bbs_wins  = cur.execute("""SELECT model_name, COUNT(model_code) AS total_wins FROM ResultsWin
                                 WHERE dataset_code == 'bbs'
                                 GROUP BY model_code""")
           
bbs_wins = cur.fetchall()

#CBC
cbc_wins = g= cur.execute("""SELECT model_name, COUNT(model_code) AS total_wins FROM ResultsWin
                                 WHERE dataset_code == 'cbc'
                                 GROUP BY model_code""")
           
cbc_wins = cur.fetchall()

#FIA
fia_wins = cur.execute("""SELECT model_name, COUNT(model_code) AS total_wins FROM ResultsWin
                                 WHERE dataset_code == 'fia'
                                 GROUP BY model_code""")
           
fia_wins = cur.fetchall()

#Gentry
gentry_wins = cur.execute("""SELECT model_name, COUNT(model_code) AS total_wins FROM ResultsWin
                                 WHERE dataset_code == 'gentry'
                                 GROUP BY model_code""")
           
gentry_wins = cur.fetchall()

#MCDB
mcdb_wins = cur.execute("""SELECT model_name, COUNT(model_code) AS total_wins FROM ResultsWin
                                 WHERE dataset_code == 'mcdb'
                                 GROUP BY model_code""")
           
mcdb_wins = cur.fetchall()

#NABA
naba_wins = cur.execute("""SELECT model_name, COUNT(model_code) AS total_wins FROM ResultsWin
                                 WHERE dataset_code == 'naba'
                                 GROUP BY model_code""")
           
naba_wins = cur.fetchall()

# Make histogram
# Set up figure
wins_by_dataset_fig = plt.figure()


# Plot variables for bbs subplot
plt.subplot(3,2,1)
N = len(bbs_wins)
x = np.arange(1, N+1)
y = [ num for (s, num) in bbs_wins ]
labels = [ s for (s, num) in bbs_wins ]
width = 1
bar1 = plt.bar( x, y, width, color="red" )
plt.ylabel( 'Number of Wins' )
plt.xticks(x + width/2.0, labels, fontsize = 5.9 )
plt.xlabel( 'BBS' )


# Plot variables for cbc subplot
plt.subplot(3,2,2)
N = len(cbc_wins)
x = np.arange(1, N+1)
y = [ num for (s, num) in cbc_wins ]
labels = [ s for (s, num) in cbc_wins ]
width = 1
bar1 = plt.bar( x, y, width, color="orange" )
plt.ylabel( 'Number of Wins' )
plt.xticks(x + width/2.0, labels, fontsize = 5.9  )
plt.xlabel( 'CBC' )


# Plot variables for fia subplot
plt.subplot(3,2,3)
N = len(fia_wins)
x = np.arange(1, N+1)
y = [ num for (s, num) in fia_wins ]
labels = [ s for (s, num) in fia_wins ]
width = 1
bar1 = plt.bar( x, y, width, color="green" )
plt.ylabel( 'Number of Wins' )
plt.xticks(x + width/2.0, labels, fontsize = 5  )
plt.xlabel( 'FIA' )


# Plot variables for Gentry subplot
plt.subplot(3,2,4)
N = len(gentry_wins)
x = np.arange(1, N+1)
y = [ num for (s, num) in gentry_wins ]
labels = [ s for (s, num) in gentry_wins ]
width = 1
bar1 = plt.bar( x, y, width, color="olivedrab" )
plt.ylabel( 'Number of Wins' )
plt.xticks(x + width/2.0, labels, fontsize = 5.9  )
plt.xlabel( 'Gentry' )


# Plot variables for mcdb subplot
plt.subplot(3,2,5)
N = len(mcdb_wins)
x = np.arange(1, N+1)
y = [ num for (s, num) in mcdb_wins ]
labels = [ s for (s, num) in mcdb_wins ]
width = 1
bar1 = plt.bar( x, y, width, color="sienna" )
plt.ylabel( 'Number of Wins' )
plt.xticks(x + width/2.0, labels, fontsize = 5  )
plt.xlabel( 'MCDB' )



# Plot variables for NABA subplot
plt.subplot(3,2,6)
N = len(naba_wins)
x = np.arange(1, N+1)
y = [ num for (s, num) in naba_wins ]
labels = [ s for (s, num) in naba_wins ]
width = 1
bar1 = plt.bar( x, y, width, color="blue" )
plt.ylabel( 'Number of Wins' )
plt.xticks(x + width/2.0, labels, fontsize = 5.9  )
plt.xlabel( 'NABA' )

plt.tight_layout()
plt.show()



#Output figure
fileName = "./sad-data/wins_by_dataset.png"
plt.savefig(fileName, format="png" )



#AIC_c weight distributions graphs
# Make histogram
# Set up figure
AIC_c_weights = plt.figure()

# Extract AICc weights for each model.
logseries = cur.execute("""SELECT AICc_weight_model FROM RawResults
                            WHERE model_name == 'Logseries' AND AICc_weight_model IS NOT NULL
                            ORDER BY AICc_weight_model""")
logseries = cur.fetchall()


untruncated_logseries = cur.execute("""SELECT AICc_weight_model FROM RawResults
                            WHERE model_name =='Untruncated logseries'AND AICc_weight_model IS NOT NULL
                            ORDER BY AICc_weight_model""")
untruncated_logseries = cur.fetchall()


pln = cur.execute("""SELECT AICc_weight_model FROM RawResults
                            WHERE model_name =='Poisson lognormal'AND AICc_weight_model IS NOT NULL
                            ORDER BY AICc_weight_model""")
pln = cur.fetchall()                            
                     
                            
                            
neg_bin = cur.execute("""SELECT AICc_weight_model FROM RawResults
                            WHERE model_name =='Negative binomial'AND AICc_weight_model IS NOT NULL
                            ORDER BY AICc_weight_model""")
neg_bin = cur.fetchall()

                      
                            
geometric = cur.execute("""SELECT AICc_weight_model FROM RawResults
                            WHERE model_name =='Geometric series'AND AICc_weight_model IS NOT NULL
                            ORDER BY AICc_weight_model""")
geometric = cur.fetchall()

# Plot variables for weights
N = len(logseries)
x = range( N )
width = 1
plt.bar( x, logseries, width, color="gray" )

plt.tight_layout()
plt.show()

#Output figure
fileName = "./sad-data/AICc_weights.png"
plt.savefig(fileName, format="png" )


# Close connection
con.close()

