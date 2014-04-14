""" Project code for performing comparisons of assorted species abundance distribution (SAD) models """

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

import mete
import macroecotools
import macroeco_distributions as md

def import_abundance(datafile, comments = '#'):
    """Imports raw species abundance .csv files in the form: Site, Year, Species, Abundance."""
    raw_data = np.genfromtxt(datafile, dtype = "S15,i8,S10,i8",
                      names = ['site','year','sp','ab'], 
                      delimiter = ",")
return raw_data

def model_comparisons(raw_data, dataset_name, data_dir, cutoff = 9):
    """ Uses raw species abundance data to compare predicted vs. empirical species abundance distributions (SAD) and output results in csv files. 
    
    Keyword arguments:
    raw_data: numpy structured array with 4 columns: 'site', 'year', 'sp' (species), 'ab' (abundance).
    dataset_name: short code to indicate the name of the dataset in the output file names.
    data_dir: directory in which to store results output.
    cutoff: minimum number of species required to run -1.
    
    SAD models and packages used:
    Maximum Entropy Theory of Ecology (METE) (METE)
    
    Logseries (macroecotools/macroecodistributions)
    Poisson lognormal (macroecotools/macroecodistributions)
    Geometric (macroecotools/macroecodistributions)
    Sugihara (macroeco/distributions)
    Negative binomial (macroeco/distributions)
    
    
    Neutral theory ()
    
    """
    usites = np.sort(list(set(raw_data["site"])))
    
    for i in range(0, len(usites)):
        subsites = raw_data["site"][raw_data["site"] == usites[i]]        
        subabundance = raw_data["ab"][raw_data["site"] == usites[i]]
        N = sum(subabundance) # N = total abundance for a site
        S = len(subsites) # S = species richness at a site
        if S > cutoff:
            print("%s, Site %s, S=%s, N=%s" % (dataset_name, i, S, N))
            
            # Generate predicted values and p (e ** -beta) based on METE:
            mete_pred = mete.get_mete_rad(int(S), int(N))
            pred = np.array(mete_pred[0])
            p = mete_pred[1]
            p_untruncated = exp(-mete.get_beta(S, N, version='untruncated'))
            obsabundance = np.sort(subabundance)[::-1]
            
            # Calculate Akaike weight of log-series:
            L_logser = md.logser_ll(obsab, p)
            L_logser_untruncated = md.logser_ll(obsab, p_untruncated)
            mu, sigma = md.pln_solver(obsab)
            L_pln = md.pln_ll(mu,sigma,obsab)        
            k1 = 1
            k2 = 2    
            AICc_logser = macroecotools.AICc(k1, L_logser, S)
            AICc_logser_untruncated = macroecotools.AICc(k1, L_logser_untruncated, S)
            AICc_pln = macroecotools.AICc(k2, L_pln, S)
            weight = macroecotools.aic_weight(AICc_logser, AICc_pln, S, cutoff = 4)
            weight_untruncated = macroecotools.aic_weight(AICc_logser_untruncated,
                                                     AICc_pln, S, cutoff = 4)
            
            # Format results for output
            results = ((np.column_stack((subsites, obsab, pred))))
            results2 = ((np.column_stack((np.array(usites[i], dtype='S20'),
                                                   S, N, p, weight,
                                                   p_untruncated,
                                                   weight_untruncated))))
            
            # Save results to a csv file:
            output1 = csv.writer(open(data_dir + dataset_name + '_obs_pred.csv','wb'))
            output2 = csv.writer(open(data_dir + dataset_name + '_dist_test.csv','wb'))   
            
            output1.writerows(results)
            output2.writerows(results2)

""" Function to see which predicted model fits best with the empirical data for each community. """

""" Plotting functions."""

# Set up analysis parameters
data_dir = './sad-data/' # path to data directory
analysis_ext = '_spab.csv' # Extension for raw species abundance files
testing_ext = '_spab_testing.csv'

datasets = ['bbs', 'cbc', 'fia', 'gentry', 'mcdb', 'naba'] # Dataset ID codes

# Starts actual analyses for each dataset in turn.
for dataset in datasets:
    datafile = data_dir + dataset + testing_ext
    dataset_name == dataset
    
    
    raw_data = import_abundance(datafile, comments = '#') # Import data
    
    model_comparisons(raw_data, dataset_name, data_dir, cutoff = 9) # Run analyses on data