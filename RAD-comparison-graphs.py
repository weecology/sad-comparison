""" Project code for graphing the results of the comparisions for species abundance distribution (SAD) models of the Ulrich and Ollik 2003 RAD data."""

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



# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('./sad-data/chapter2/UlrichOllik2003.sqlite')
cur = con.cursor()

# Switch con data type to string
con.text_factory = str

'''Summarize the number of wins for each model/dataset'''
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
#Output figure
fileName = "./sad-data/chapter2/total_wins.png"
plt.savefig(fileName, format="png" )
plt.close()

'''AIC_c weight distributions graphs'''
# Make histogram
# Set up figure
AIC_c_weights = plt.figure()
# Extract AICc weights for each model.
#Logseries
logseries = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name == 'Logseries' AND value_type =='AICc weight' AND value IS NOT NULL
                            ORDER BY value""")
logseries = cur.fetchall()


#Poisson lognormal
pln = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Poisson lognormal' AND value_type =='AICc weight' AND value IS NOT NULL
                            ORDER BY value""")
pln = cur.fetchall()
                              
#Negative binomial                            
neg_bin = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Negative binomial' AND value_type =='AICc weight' AND value IS NOT NULL
                            ORDER BY value""")
neg_bin = cur.fetchall()
                      
#Geometric series                            
geometric = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Geometric series' AND value_type =='AICc weight' AND value IS NOT NULL
                            ORDER BY value""")
geometric = cur.fetchall()

#Zipf distribution                           
zipf = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Zipf distribution' AND value_type =='AICc weight' AND value IS NOT NULL
                            ORDER BY value""")
zipf = cur.fetchall()
# Plot variables for weights
bins = 50
#Logseries
model0 = [ num for (s, num) in logseries ]
plt.hist(model0, bins, range = (0,1), facecolor = 'magenta', histtype="stepfilled", alpha=1, label = "Logseries")
#Poisson lognormal
model1 = [ num for (s, num) in pln]
plt.hist(model1, bins, range = (0,1), facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
#Negative binomial
model2 = [ num for (s, num) in neg_bin]
plt.hist(model2, bins, range = (0,1), facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
#Geometric series
model3 = [ num for (s, num) in geometric]
plt.hist(model3, bins, range = (0,1), facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
#Zipf distribution
model4 = [ num for (s, num) in zipf]
plt.hist(model4, bins, range = (0,1), facecolor = 'orange', histtype="stepfilled", alpha=.7, label = "Zipf")

plt.legend(loc = 'upper right', fontsize = 11)

plt.xlabel("AICc weights")
plt.ylabel("Frequency")

plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/AICc_weights.png"
plt.savefig(fileName, format="png" )
plt.close()


'''Plot weights for each model individually'''
bins = 50
#Logseries
plt.figure()
plt.hist(model0, bins, range = (0,1), facecolor = 'magenta', histtype="stepfilled", alpha=1, label = "Logseries")
plt.xlabel("Logseries AICc weights")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/Logseries_weights.png"
plt.savefig(fileName, format="png" )
plt.close()

#Poisson lognormal
plt.figure()
plt.hist(model1, bins, range = (0,1), facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
plt.xlabel("Poisson lognormal AICc weights")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/Poisson_lognormal_weights.png"
plt.savefig(fileName, format="png" )
plt.close()

#Negative binomial
plt.figure()
model2 = [ num for (s, num) in neg_bin]
plt.hist(model2, bins, range = (0,1), facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
plt.xlabel("Negative binomial AICc weights")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/Negative_binomial_weights.png"
plt.savefig(fileName, format="png" )
plt.close()

#Geometric series
plt.figure()
model3 = [ num for (s, num) in geometric]
plt.hist(model3, bins, range = (0,1), facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
plt.xlabel("Geometric AICc weights")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/Geometric_weights.png"
plt.savefig(fileName, format="png" )
plt.close()

#Zipf distribution
plt.figure()
model4 = [ num for (s, num) in zipf]
plt.hist(model4, bins, range = (0,1), facecolor = 'orange', histtype="stepfilled", alpha=.7, label = "Zipf")
plt.xlabel("Zipf distribution AICc weights")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/Zipf_weights.png"
plt.savefig(fileName, format="png" )
plt.close()


'''Likelihoods graph'''
# Make histogram
# Set up figure
l_likelihood = plt.figure()
# Extract log-likelihoods for each model.
#Logseries
ll_logseries = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name == 'Logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
ll_logseries = cur.fetchall()
#Poisson lognormal
ll_pln = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Poisson lognormal' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
ll_pln = cur.fetchall()                                             
#Negative binomial                            
ll_neg_bin = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Negative binomial' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
ll_neg_bin = cur.fetchall()                     
#Geometric series                            
ll_geometric = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Geometric series' AND value_type =='likelihood' AND value IS NOT NUll 
                            ORDER BY value""")
ll_geometric = cur.fetchall()
#Zipf distribution
ll_zipf = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Zipf distribution' AND value_type =='likelihood' AND value IS NOT NUll 
                            ORDER BY value""")
ll_zipf = cur.fetchall()


# Plot variables for combined likelihoods graph
#Zipf distribution
ll_model5 = [ num for (s, num) in ll_zipf]
plt.hist(ll_model5, bins = range(-750, 0, 10), facecolor = 'orange', histtype="stepfilled", alpha=.7, label = "Zipf distribution")
#Geometric series
ll_model4 = [ num for (s, num) in ll_geometric]
plt.hist(ll_model4, bins = range(-750, 0, 10), facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
#Negative binomial
ll_model3 = [ num for (s, num) in ll_neg_bin]
plt.hist(ll_model3, bins = range(-750, 0, 10), facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
#Poisson lognormal
ll_model2 = [ num for (s, num) in ll_pln]
plt.hist(ll_model2, bins = range(-750, 0, 10), facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
#Logseries
ll_model0 = [ num for (s, num) in ll_logseries ]
plt.hist(ll_model0, bins = range(-750, 0, 10), facecolor = 'magenta', histtype="stepfilled", alpha=.4, label = "Logseries")

plt.legend(loc = 'upper left', fontsize = 11)
plt.xlabel("Log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

''' Plot likelihoods for each model individually'''
#Logseries
plt.figure()
plt.hist(ll_model0, bins = range(-750, 0, 10), facecolor = 'magenta', histtype="stepfilled", alpha=1, label = "Logseries")
plt.xlabel("Logseries log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/logseries_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

#Poisson lognormal
plt.figure()
plt.hist(ll_model2, bins = range(-750, 0, 10), facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
plt.xlabel("Poisson lognormal log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/pln_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

#Negative binomial
plt.figure()
plt.hist(ll_model3, bins = range(-750, 0, 10), facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
plt.xlabel("Negative binomial log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/neg_bin_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

#Geometric
plt.figure()
plt.hist(ll_model4, bins = range(-750, 0, 10), facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
plt.xlabel("Geometric log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/geometric_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

#Zipf distribution
plt.figure()
plt.hist(ll_model5, bins = range(-750, 0, 10), facecolor = 'orange', histtype="stepfilled", alpha=.7, label = "Zipf distribution")
plt.xlabel("Zipf distribution log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/Zipf_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

'''Relative likelihoods graph'''
# Make histogram
# Set up figure
relative_likelihood = plt.figure()
# Extract relative likelihoods for each model.
#Logseries
relative_logseries = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name == 'Logseries' AND value_type =='relative likelihood' AND value IS NOT NUll
                            ORDER BY value""")
relative_logseries = cur.fetchall()
#Poisson lognormal
relative_pln = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Poisson lognormal' AND value_type =='relative likelihood' AND value IS NOT NUll
                            ORDER BY value""")
relative_pln = cur.fetchall()                        
#Negative binomial                            
relative_neg_bin = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Negative binomial' AND value_type =='relative likelihood' AND value IS NOT NUll
                            ORDER BY value""")
relative_neg_bin = cur.fetchall()
#Geometric series                           
relative_geometric = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Geometric series' AND value_type =='relative likelihood' AND value IS NOT NUll 
                            ORDER BY value""")
relative_geometric = cur.fetchall()
#Zipf distribution                         
relative_zipf = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Zipf distribution' AND value_type =='relative likelihood' AND value IS NOT NUll 
                            ORDER BY value""")
relative_zipf = cur.fetchall()

# Plot variables for relative likelihoods combined graph
plt.figure()
bins = 50
#Zipf distribution
relative_model5 = [ num for (s, num) in relative_zipf]
plt.hist(relative_model5, bins, range = [0,1], facecolor = 'orange', histtype="stepfilled", alpha=.7, label = "Zipf distribution")
#Geometric series
relative_model4 = [ num for (s, num) in relative_geometric]
plt.hist(relative_model4, bins, range = [0,1], facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
#Negative binomial
relative_model3 = [ num for (s, num) in relative_neg_bin]
plt.hist(relative_model3, bins, range = [0,1], facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
#Poisson lognormal
relative_model2 = [ num for (s, num) in relative_pln]
plt.hist(relative_model2, bins, range = [0,1], facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
#Logseries
relative_model0 = [ num for (s, num) in relative_logseries ]
plt.hist(relative_model0, bins, range = [0,1], facecolor = 'magenta', histtype="stepfilled", alpha=.4, label = "Logseries")

plt.legend(loc = 'upper right', fontsize = 11)
plt.xlabel("Relative likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/relative_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

''' Plot relative likelihoods for each model individually'''
#Logseries
plt.figure()
plt.hist(relative_model0, bins, range = [0,1], facecolor = 'magenta', histtype="stepfilled", alpha=1, label = "Logseries")
plt.xlabel("Logseries relative likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/logseries_relative.png"
plt.savefig(fileName, format="png" )
plt.close()


#Poisson lognormal
plt.figure()
plt.hist(relative_model2, bins, range = [0,1], facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
plt.xlabel("Poisson lognormal relative likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/pln_relative.png"
plt.savefig(fileName, format="png" )
plt.close()

#Negative binomial
plt.figure()
plt.hist(relative_model3, bins, range = [0,1], facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
plt.xlabel("Negative binomial relative likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/neg_bin_relative.png"
plt.savefig(fileName, format="png" )
plt.close()

#Geometric
plt.figure()
plt.hist(relative_model4, bins, range = [0,1], facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
plt.xlabel("Geometric relative likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/geometric_relative.png"
plt.savefig(fileName, format="png" )
plt.close()

#Zipf
plt.figure()
plt.hist(relative_model5, bins, range = [0,1], facecolor = 'orange', histtype="stepfilled", alpha=.7, label = "Geometric")
plt.xlabel("Zipf distribution")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter2/zipf_relative.png"
plt.savefig(fileName, format="png" )
plt.close()

# Close connection
con.close()




