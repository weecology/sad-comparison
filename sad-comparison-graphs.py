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



# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('./sad-data/chapter1/SummarizedResults.sqlite')
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
fileName = "./sad-data/chapter1/total_wins.png"
plt.savefig(fileName, format="png" )
plt.close()

''' Extract number of wins for each model and dataset'''
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
plt.yticks(fontsize = 'small')
plt.ylabel( 'Number of Wins', fontsize = 'small')
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
plt.yticks(fontsize = 'small')
plt.ylabel( 'Number of Wins', fontsize = 'small' )
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
plt.yticks(fontsize = 'small')
plt.ylabel( 'Number of Wins', fontsize = 'small' )
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
plt.yticks(fontsize = 'small')
plt.ylabel( 'Number of Wins', fontsize = 'small' )
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
plt.yticks(fontsize = 'small')
plt.ylabel( 'Number of Wins', fontsize = 'small' )
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
plt.yticks(fontsize = 'small')
plt.ylabel( 'Number of Wins', fontsize = 'small' )
plt.xticks(x + width/2.0, labels, fontsize = 5.9  )
plt.xlabel( 'NABA' )

plt.tight_layout()

#Output figure
fileName = "./sad-data/chapter1/wins_by_dataset.png"
plt.savefig(fileName, format="png" )
plt.close()


'''AIC_c weight distributions graphs'''
# Make histogram
# Set up figure
AIC_c_weights = plt.figure()
# Extract AICc weights for each model.
#Truncated logseries
logseries = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name == 'Logseries' AND value_type =='AICc weight' AND value IS NOT NULL
                            ORDER BY value""")
logseries = cur.fetchall()

#Untruncated logseries
untruncated_logseries = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Untruncated logseries' AND value_type =='AICc weight' AND value IS NOT NULL
                            ORDER BY value""")
untruncated_logseries = cur.fetchall()

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
# Plot variables for weights
bins = 50
#Truncated logseries
model0 = [ num for (s, num) in logseries ]
plt.hist(model0, bins, range = (0,1), facecolor = 'magenta', histtype="stepfilled", alpha=1, label = "Truncated logseries")
#Untruncated logseries
model1 = [ num for (s, num) in untruncated_logseries]
plt.hist(model1, bins, range = (0,1), facecolor = 'orange', histtype="stepfilled", alpha=.7, label = "Untruncated logseries")
#Poisson lognormal
model2 = [ num for (s, num) in pln]
plt.hist(model2, bins, range = (0,1), facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
#Negative binomial
model3 = [ num for (s, num) in neg_bin]
plt.hist(model3, bins, range = (0,1), facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
#Geometric series
model4 = [ num for (s, num) in geometric]
plt.hist(model4, bins, range = (0,1), facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")

plt.legend(loc = 'upper right', fontsize = 11)

plt.xlabel("AICc weights")
plt.ylabel("Frequency")

plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/AICc_weights.png"
plt.savefig(fileName, format="png" )
plt.close()


'''Plot weights for each model individually'''
bins = 50
# Truncated logseries
plt.figure()
plt.hist(model0, bins, range = (0,1), facecolor = 'magenta', histtype="stepfilled", alpha=1, label = "Truncated logseries")
plt.xlabel("Truncated logseries AICc weights")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/Truncated_logseries_weights.png"
plt.savefig(fileName, format="png" )
plt.close()

#Untruncated logseries
plt.figure()
plt.hist(model1, bins, range = (0,1), facecolor = 'orange', histtype="stepfilled", alpha=.7, label = "Untruncated logseries")
plt.xlabel("Untruncated logseries AICc weights")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/Untruncated_logseries_weights.png"
plt.savefig(fileName, format="png" )
plt.close()

#Poisson lognormal
plt.figure()
plt.hist(model2, bins, range = (0,1), facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
plt.xlabel("Poisson lognormal AICc weights")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/Poisson_lognormal_weights.png"
plt.savefig(fileName, format="png" )
plt.close()

#Negative binomial
plt.figure()
model3 = [ num for (s, num) in neg_bin]
plt.hist(model3, bins, range = (0,1), facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
plt.xlabel("Negative binomial AICc weights")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/Negative_binomial_weights.png"
plt.savefig(fileName, format="png" )
plt.close()

#Geometric series
plt.figure()
model4 = [ num for (s, num) in geometric]
plt.hist(model4, bins, range = (0,1), facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
plt.xlabel("Geometric AICc weights")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/Geometric_weights.png"
plt.savefig(fileName, format="png" )
plt.close()


'''Likelihoods graph'''
# Make histogram
# Set up figure
l_likelihood = plt.figure()
# Extract log-likelihoods for each model.
#Truncated logseries
ll_logseries = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name == 'Logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
ll_logseries = cur.fetchall()

#Untruncated logseries
ll_untruncated_logseries = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Untruncated logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
ll_untruncated_logseries = cur.fetchall()

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


# Plot variables for combined likelihoods graph
#Geometric series
ll_model4 = [ num for (s, num) in ll_geometric]
plt.hist(ll_model4, bins = range(-750, 0, 10), facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
#Negative binomial
ll_model3 = [ num for (s, num) in ll_neg_bin]
plt.hist(ll_model3, bins = range(-750, 0, 10), facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
#Poisson lognormal
ll_model2 = [ num for (s, num) in ll_pln]
plt.hist(ll_model2, bins = range(-750, 0, 10), facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
#Untruncated logseries
ll_model1 = [ num for (s, num) in ll_untruncated_logseries]
plt.hist(ll_model1, bins = range(-750, 0, 10), facecolor = 'orange', histtype="stepfilled", alpha=.5, label = "Untruncated logseries")
#Truncated logseries
ll_model0 = [ num for (s, num) in ll_logseries ]
plt.hist(ll_model0, bins = range(-750, 0, 10), facecolor = 'magenta', histtype="stepfilled", alpha=.4, label = "Truncated logseries")

plt.legend(loc = 'upper left', fontsize = 11)
plt.xlabel("Log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

''' Plot likelihoods for each model individually'''
#Truncated logseries
plt.figure()
plt.hist(ll_model0, bins = range(-750, 0, 10), facecolor = 'magenta', histtype="stepfilled", alpha=1, label = "Truncated logseries")
plt.xlabel("Truncated logseries log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/truncated_logseries_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()


#Untruncated logseries
plt.figure()
plt.hist(ll_model1, bins = range(-750, 0, 10), facecolor = 'orange', histtype="stepfilled", alpha=.7, label = "Untruncated logseries")
plt.xlabel("Untruncated logseries log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/untruncated_logseries_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

#Poisson lognormal
plt.figure()
plt.hist(ll_model2, bins = range(-750, 0, 10), facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
plt.xlabel("Poisson lognormal log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/pln_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

#Negative binomial
plt.figure()
plt.hist(ll_model3, bins = range(-750, 0, 10), facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
plt.xlabel("Negative binomial log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/neg_bin_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

#Geometric
plt.figure()
plt.hist(ll_model4, bins = range(-750, 0, 10), facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
plt.xlabel("Geometric log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/geometric_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

'''Plot likelihoods by dataset and model'''
# BBS
#BBS truncated logseries
bbs_ll_logser = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'bbs' AND model_name == 'Logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
bbs_ll_logser = cur.fetchall()
#BBS untruncated logseries
bbs_ll_untruncated_logser = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'bbs' AND model_name == 'Untruncated logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
bbs_ll_untruncated_logser = cur.fetchall()
#BBS Poisson lognormal
bbs_ll_pln = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'bbs' AND model_name == 'Poisson lognormal' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
bbs_ll_pln = cur.fetchall()
#BBS negative binomial
bbs_ll_neg_bin = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'bbs' AND model_name == 'Negative binomial' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
bbs_ll_neg_bin = cur.fetchall()
#BBS geometric
bbs_ll_geometric = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'bbs' AND model_name == 'Untruncated logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
bbs_ll_geometric = cur.fetchall()

# Plot variables for BBS combined likelihoods graph
plt.figure()
#Geometric series
bbs_ll_model4 = [ num for (s, num) in bbs_ll_geometric]
plt.hist(bbs_ll_model4, bins = range(-750, 0, 10), facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
#Negative binomial
bbs_ll_model3 = [ num for (s, num) in bbs_ll_neg_bin]
plt.hist(bbs_ll_model3, bins = range(-750, 0, 10), facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
#Poisson lognormal
bbs_ll_model2 = [ num for (s, num) in bbs_ll_pln]
plt.hist(bbs_ll_model2, bins = range(-750, 0, 10), facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
#Untruncated logseries
bbs_ll_model1 = [ num for (s, num) in bbs_ll_untruncated_logser]
plt.hist(bbs_ll_model1, bins = range(-750, 0, 10), facecolor = 'orange', histtype="stepfilled", alpha=.5, label = "Untruncated logseries")
#Truncated logseries
bbs_ll_model0 = [ num for (s, num) in bbs_ll_logser]
plt.hist(bbs_ll_model0, bins = range(-750, 0, 10), facecolor = 'magenta', histtype="stepfilled", alpha=.4, label = "Truncated logseries")

plt.legend(loc = 'upper left', fontsize = 11)
plt.xlabel("BBS log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/bbs_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

# CBC
plt.figure()
#CBC truncated logseries
cbc_ll_logser = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'cbc' AND model_name == 'Logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
cbc_ll_logser = cur.fetchall()
#CBC untruncated logseries
cbc_ll_untruncated_logser = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'cbc' AND model_name == 'Untruncated logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
cbc_ll_untruncated_logser = cur.fetchall()
#CBC Poisson lognormal
cbc_ll_pln = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'cbc' AND model_name == 'Poisson lognormal' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
cbc_ll_pln = cur.fetchall()
#CBC negative binomial
cbc_ll_neg_bin = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'cbc' AND model_name == 'Negative binomial' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
cbc_ll_neg_bin = cur.fetchall()
#CBC geometric
cbc_ll_geometric = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'cbc' AND model_name == 'Untruncated logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
cbc_ll_geometric = cur.fetchall()

# Plot variables for CBC combined likelihoods graph
plt.figure()
#Geometric series
cbc_ll_model4 = [ num for (s, num) in cbc_ll_geometric]
plt.hist(cbc_ll_model4, bins = range(-750, 0, 10), facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
#Negative binomial
cbc_ll_model3 = [ num for (s, num) in cbc_ll_neg_bin]
plt.hist(cbc_ll_model3, bins = range(-750, 0, 10), facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
#Poisson lognormal
cbc_ll_model2 = [ num for (s, num) in cbc_ll_pln]
plt.hist(cbc_ll_model2, bins = range(-750, 0, 10), facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
#Untruncated logseries
cbc_ll_model1 = [ num for (s, num) in cbc_ll_untruncated_logser]
plt.hist(cbc_ll_model1, bins = range(-750, 0, 10), facecolor = 'orange', histtype="stepfilled", alpha=.5, label = "Untruncated logseries")
#Truncated logseries
cbc_ll_model0 = [ num for (s, num) in cbc_ll_logser]
plt.hist(cbc_ll_model0, bins = range(-750, 0, 10), facecolor = 'magenta', histtype="stepfilled", alpha=.4, label = "Truncated logseries")

plt.legend(loc = 'upper left', fontsize = 11)
plt.xlabel("CBC log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/cbc_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

# FIA
#FIA truncated logseries
fia_ll_logser = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'fia' AND model_name == 'Logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
fia_ll_logser = cur.fetchall()
#FIA untruncated logseries
fia_ll_untruncated_logser = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'fia' AND model_name == 'Untruncated logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
fia_ll_untruncated_logser = cur.fetchall()
#FIA Poisson lognormal
fia_ll_pln = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'fia' AND model_name == 'Poisson lognormal' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
fia_ll_pln = cur.fetchall()
#FIA negative binomial
fia_ll_neg_bin = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'fia' AND model_name == 'Negative binomial' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
fia_ll_neg_bin = cur.fetchall()
#FIA geometric
fia_ll_geometric = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'fia' AND model_name == 'Untruncated logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
fia_ll_geometric = cur.fetchall()

# Plot variables for FIA combined likelihoods graph
plt.figure()
#Geometric series
fia_ll_model4 = [ num for (s, num) in fia_ll_geometric]
plt.hist(fia_ll_model4, bins = range(-750, 0, 10), facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
#Negative binomial
fia_ll_model3 = [ num for (s, num) in fia_ll_neg_bin]
plt.hist(fia_ll_model3, bins = range(-750, 0, 10), facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
#Poisson lognormal
fia_ll_model2 = [ num for (s, num) in fia_ll_pln]
plt.hist(fia_ll_model2, bins = range(-750, 0, 10), facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
#Untruncated logseries
fia_ll_model1 = [ num for (s, num) in fia_ll_untruncated_logser]
plt.hist(bbs_ll_model1, bins = range(-750, 0, 10), facecolor = 'orange', histtype="stepfilled", alpha=.5, label = "Untruncated logseries")
#Truncated logseries
fia_ll_model0 = [ num for (s, num) in fia_ll_logser]
plt.hist(fia_ll_model0, bins = range(-750, 0, 10), facecolor = 'magenta', histtype="stepfilled", alpha=.4, label = "Truncated logseries")

plt.legend(loc = 'upper left', fontsize = 11)
plt.xlabel("FIA log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/fia_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()


# Gentry
#Gentry truncated logseries
gentry_ll_logser = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'gentry' AND model_name == 'Logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
gentry_ll_logser = cur.fetchall()
#Gentry untruncated logseries
gentry_ll_untruncated_logser = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'gentry' AND model_name == 'Untruncated logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
gentry_ll_untruncated_logser = cur.fetchall()
#Gentry Poisson lognormal
gentry_ll_pln = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'gentry' AND model_name == 'Poisson lognormal' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
gentry_ll_pln = cur.fetchall()
#CBC negative binomial
gentry_ll_neg_bin = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'gentry' AND model_name == 'Negative binomial' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
gentry_ll_neg_bin = cur.fetchall()
#Gentry geometric
gentry_ll_geometric = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'gentry' AND model_name == 'Untruncated logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
gentry_ll_geometric = cur.fetchall()

# Plot variables for Gentry combined likelihoods graph
plt.figure()
#Geometric series
gentry_ll_model4 = [ num for (s, num) in gentry_ll_geometric]
plt.hist(gentry_ll_model4, bins = range(-750, 0, 10), facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
#Negative binomial
gentry_ll_model3 = [ num for (s, num) in gentry_ll_neg_bin]
plt.hist(gentry_ll_model3, bins = range(-750, 0, 10), facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
#Poisson lognormal
gentry_ll_model2 = [ num for (s, num) in gentry_ll_pln]
plt.hist(gentry_ll_model2, bins = range(-750, 0, 10), facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
#Untruncated logseries
gentry_ll_model1 = [ num for (s, num) in gentry_ll_untruncated_logser]
plt.hist(gentry_ll_model1, bins = range(-750, 0, 10), facecolor = 'orange', histtype="stepfilled", alpha=.5, label = "Untruncated logseries")
#Truncated logseries
gentry_ll_model0 = [ num for (s, num) in gentry_ll_logser]
plt.hist(gentry_ll_model0, bins = range(-750, 0, 10), facecolor = 'magenta', histtype="stepfilled", alpha=.4, label = "Truncated logseries")

plt.legend(loc = 'upper left', fontsize = 11)
plt.xlabel("Gentry log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/gentry_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()


# MCDB
#MCDB truncated logseries
mcdb_ll_logser = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'mcdb' AND model_name == 'Logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
mcdb_ll_logser = cur.fetchall()
#MCDB untruncated logseries
mcdb_ll_untruncated_logser = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'mcdb' AND model_name == 'Untruncated logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
mcdb_ll_untruncated_logser = cur.fetchall()
#MCDB Poisson lognormal
mcdb_ll_pln = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'mcdb' AND model_name == 'Poisson lognormal' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
mcdb_ll_pln = cur.fetchall()
#MCDB  negative binomial
mcdb_ll_neg_bin = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'mcdb' AND model_name == 'Negative binomial' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
mcdb_ll_neg_bin = cur.fetchall()
#MCDB  geometric
mcdb_ll_geometric = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'mcdb' AND model_name == 'Untruncated logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
mcdb_ll_geometric = cur.fetchall()

# Plot variables for MCDB combined likelihoods graph
plt.figure()
#Geometric series
mcdb_ll_model4 = [ num for (s, num) in mcdb_ll_geometric]
plt.hist(mcdb_ll_model4, bins = range(-750, 0, 10), facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
#Negative binomial
mcdb_ll_model3 = [ num for (s, num) in mcdb_ll_neg_bin]
plt.hist(mcdb_ll_model3, bins = range(-750, 0, 10), facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
#Poisson lognormal
mcdb_ll_model2 = [ num for (s, num) in mcdb_ll_pln]
plt.hist(mcdb_ll_model2, bins = range(-750, 0, 10), facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
#Untruncated logseries
mcdb_ll_model1 = [ num for (s, num) in mcdb_ll_untruncated_logser]
plt.hist(mcdb_ll_model1, bins = range(-750, 0, 10), facecolor = 'orange', histtype="stepfilled", alpha=.5, label = "Untruncated logseries")
#Truncated logseries
mcdb_ll_model0 = [ num for (s, num) in mcdb_ll_logser]
plt.hist(mcdb_ll_model0, bins = range(-750, 0, 10), facecolor = 'magenta', histtype="stepfilled", alpha=.4, label = "Truncated logseries")

plt.legend(loc = 'upper left', fontsize = 11)
plt.xlabel("MCDB log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/mcdb_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

# NABA
#NABA truncated logseries
naba_ll_logser = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'naba' AND model_name == 'Logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
naba_ll_logser = cur.fetchall()
#NABA untruncated logseries
naba_ll_untruncated_logser = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'naba' AND model_name == 'Untruncated logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
naba_ll_untruncated_logser = cur.fetchall()
#NABA Poisson lognormal
naba_ll_pln = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'naba' AND model_name == 'Poisson lognormal' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
naba_ll_pln = cur.fetchall()
#NABA negative binomial
naba_ll_neg_bin = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'naba' AND model_name == 'Negative binomial' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
naba_ll_neg_bin = cur.fetchall()
#NABA geometric
naba_ll_geometric = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE dataset_code == 'naba' AND model_name == 'Untruncated logseries' AND value_type =='likelihood' AND value IS NOT NUll
                            ORDER BY value""")
naba_ll_geometric = cur.fetchall()

# Plot variables for NABA combined likelihoods graph
plt.figure()
#Geometric series
naba_ll_model4 = [ num for (s, num) in naba_ll_geometric]
plt.hist(naba_ll_model4, bins = range(-750, 0, 10), facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
#Negative binomial
naba_ll_model3 = [ num for (s, num) in naba_ll_neg_bin]
plt.hist(naba_ll_model3, bins = range(-750, 0, 10), facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
#Poisson lognormal
naba_ll_model2 = [ num for (s, num) in naba_ll_pln]
plt.hist(naba_ll_model2, bins = range(-750, 0, 10), facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
#Untruncated logseries
naba_ll_model1 = [ num for (s, num) in naba_ll_untruncated_logser]
plt.hist(naba_ll_model1, bins = range(-750, 0, 10), facecolor = 'orange', histtype="stepfilled", alpha=.5, label = "Untruncated logseries")
#Truncated logseries
naba_ll_model0 = [ num for (s, num) in naba_ll_logser]
plt.hist(naba_ll_model0, bins = range(-750, 0, 10), facecolor = 'magenta', histtype="stepfilled", alpha=.4, label = "Truncated logseries")


plt.legend(loc = 'upper left', fontsize = 11)
plt.xlabel("NABA log-likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/naba_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()


'''Relative likelihoods graph'''
# Make histogram
# Set up figure
relative_likelihood = plt.figure()
# Extract relative likelihoods for each model.
#Truncated logseries
relative_logseries = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name == 'Logseries' AND value_type =='relative likelihood' AND value IS NOT NUll
                            ORDER BY value""")
relative_logseries = cur.fetchall()

#Untruncated logseries
relative_untruncated_logseries = cur.execute("""SELECT model_name, value FROM RawResults
                            WHERE model_name =='Untruncated logseries' AND value_type =='relative likelihood' AND value IS NOT NUll
                            ORDER BY value""")
relative_untruncated_logseries = cur.fetchall()


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

# Plot variables for relative likelihoods combined graph
plt.figure()
bins = 50
#Geometric series
relative_model4 = [ num for (s, num) in relative_geometric]
plt.hist(relative_model4, bins, range = [0,1], facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
#Negative binomial
relative_model3 = [ num for (s, num) in relative_neg_bin]
plt.hist(relative_model3, bins, range = [0,1], facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
#Poisson lognormal
relative_model2 = [ num for (s, num) in relative_pln]
plt.hist(relative_model2, bins, range = [0,1], facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
#Untruncated lognormal
relative_model1 = [ num for (s, num) in relative_untruncated_logseries]
plt.hist(relative_model1, bins, range = [0,1], facecolor = 'orange', histtype="stepfilled", alpha=.5, label = "Untruncated logseries")
#Truncated logseries
relative_model0 = [ num for (s, num) in relative_logseries ]
plt.hist(relative_model0, bins, range = [0,1], facecolor = 'magenta', histtype="stepfilled", alpha=.4, label = "Truncated logseries")

plt.legend(loc = 'upper right', fontsize = 11)
plt.xlabel("Relative likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/relative_likelihoods.png"
plt.savefig(fileName, format="png" )
plt.close()

''' Plot relative likelihoods for each model individually'''
#Truncated logseries
plt.figure()
plt.hist(relative_model0, bins, range = [0,1], facecolor = 'magenta', histtype="stepfilled", alpha=1, label = "Truncated logseries")
plt.xlabel("Truncated logseries relative likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/truncated_logseries_relative.png"
plt.savefig(fileName, format="png" )
plt.close()


#Untruncated logseries
plt.figure()
plt.hist(relative_model1, bins, range = [0,1], facecolor = 'orange', histtype="stepfilled", alpha=.7, label = "Untruncated logseries")
plt.xlabel("Untruncated logseries relative likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/untruncated_logseries_relative.png"
plt.savefig(fileName, format="png" )
plt.close()

#Poisson lognormal
plt.figure()
plt.hist(relative_model2, bins, range = [0,1], facecolor = 'teal', histtype="stepfilled", alpha=.7, label = "Poisson lognormal")
plt.xlabel("Poisson lognormal relative likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/pln_relative.png"
plt.savefig(fileName, format="png" )
plt.close()

#Negative binomial
plt.figure()
plt.hist(relative_model3, bins, range = [0,1], facecolor = 'gray', histtype="stepfilled", alpha=.7, label = "Negative binomial")
plt.xlabel("Negative binomial relative likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/neg_bin_relative.png"
plt.savefig(fileName, format="png" )
plt.close()

#Geometric
plt.figure()
plt.hist(relative_model4, bins, range = [0,1], facecolor = 'olivedrab', histtype="stepfilled", alpha=.7, label = "Geometric")
plt.xlabel("Geometric relative likelihoods")
plt.ylabel("Frequency")
plt.tight_layout()
#Output figure
fileName = "./sad-data/chapter1/geometric_relative.png"
plt.savefig(fileName, format="png" )
plt.close()

# Close connection
con.close()