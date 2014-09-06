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

from mpl_toolkits.axes_grid.inset_locator import inset_axes

# Function to import the AICc results.

def import_results(datafile):
    """Imports raw result .csv files in the form: site, S, N, AICc_logseries, AICc_logseries_untruncated, AICc_pln, AICc_negbin, AICc_geometric."""
    raw_results = np.genfromtxt(datafile, dtype = "S15,i8,i8, f10, f10, f10, f10, f10", skip_header = 1,
                      names = ['site', 'S', 'N', 'AICc_logseries', 'AICc_logseries_untruncated', 'AICc_pln', 'AICc_negbin', 'AICc_geometric'], delimiter = ",", missing_values = '', filling_values = '', )
    return raw_results

# Function to determine the winning model for each site.

# Function to make histograms.

# Set up analysis parameters
data_dir = './sad-data/' # path to data directory
results_ext = '_dist_test.csv' # Extension for raw species abundance files

datasets = ['bbs', 'cbc', 'fia', 'gentry', 'mcdb', 'naba'] # Dataset ID codes

# Starts actual processing for each set of results in turn.
for dataset in datasets:
    datafile = data_dir + dataset + results_ext
        
    raw_results = import_results(datafile) # Import data
      
    print(raw_results)  