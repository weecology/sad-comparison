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

import mete # https://github.com/weecology/METE.git
import macroecotools # https://github.com/weecology/macroecotools.git
import macroeco_distributions as md

def import_abundance(datafile):
    """Imports raw species abundance .csv files in the form: Site, Year, Species, Abundance."""
    raw_data = np.genfromtxt(datafile, dtype = "S15,i8,S10,i8",
                      names = ['site','year','sp','ab'], delimiter = ",")
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
    Negative binomial (macroecotools/macroecodistributions)
    Generalized Yule (macroecotools/macroecodistributions)
    Geometric (macroecotools/macroecodistributions)
    
    
    Zipf (Power) distribution ()
    
    
    Neutral theory ()
    
    """
    usites = np.sort(list(set(raw_data["site"])))
    
    for site in usites:
        subsites = raw_data["site"][raw_data["site"] == site]        
        subabundance = raw_data["ab"][raw_data["site"] == site]
        N = sum(subabundance) # N = total abundance for a site
        S = len(subsites) # S = species richness at a site
        if S > cutoff:
            print("%s, Site %s, S=%s, N=%s" % (dataset_name, site, S, N))
            
            # Generate predicted values and p (e ** -beta) based on METE:
            mete_pred = mete.get_mete_rad(int(S), int(N))
            pred = np.array(mete_pred[0])
            p = mete_pred[1]
            p_untruncated = exp(-mete.get_beta(S, N, version='untruncated'))
            obsabundance = np.sort(subabundance)[::-1]
            
            # Calculate log-likelihoods of species abundance models:
            # Logseries
            L_logser = md.logser_ll(obsabundance, p) # Log-likelihood of truncated logseries
            L_logser_untruncated = md.logser_ll(obsabundance, p_untruncated) # Log-likelihood of untruncated logseries
            
            # Poisson lognormal
            mu, sigma = md.pln_solver(obsabundance)
            L_pln = md.pln_ll(obsabundance, mu,sigma) # Log-likelihood of Poisson lognormal
            
           
            # Negative binomial
            n0, p0 = md.negbin_solver(obsabundance)
            L_negbin = md.negbin_ll(obsabundance, n0, p0) # Log-likelihood of negative binomial
            
            # Generalized Yule
            list_obsabundance = obsabundance.tolist() # Yule solver uses list method incompatible with NumPy array.
            a, b = md.gen_yule_solver(list_obsabundance)
            L_gen_yule = md.gen_yule_ll(obsabundance, a, b)
            
            # Geometric series
            upper_bound = max(obsabundance)
            p = md.trunc_geom_solver(obsabundance, upper_bound)
            L_geometric = md.geom_ll(obsabundance, p) # Log-likelihood of geometric series            
            
            # Zipf distribution
            
            
            # Calculate Akaike weight of species abundance models:
            # Parameter k is the number of fitted parameters
            k1 = 1
            k2 = 2
            
            # Calculate AICc values
            AICc_logser = macroecotools.AICc(k2, L_logser, S) # AICc logseries
            AICc_logser_untruncated = macroecotools.AICc(k1, L_logser_untruncated, S) # AICc logseries untruncated
            AICc_pln = macroecotools.AICc(k2, L_pln, S) # AICc Poisson lognormal
            AICc_negbin = macroecotools.AICc(k2, L_negbin, S)# AICc negative binomial
            AICc_gen_yule = macroecotools.AICc(k2, L_gen_yule, S)
            AICc_geometric = macroecotools.AICc(k1, L_geometric, S) # AICc geometric series
            
            
            # Make list of AICc values
            AICc_list = [AICc_logser, AICc_logser_untruncated, AICc_pln, AICc_negbin, AICc_gen_yule, AICc_geometric]
            
            
            # Calulate AICc weight            
            weight = macroecotools.aic_weight(AICc_list, S, cutoff = 4)
                        
            
            # Format results for output
            results = ((np.column_stack((subsites, obsabundance, pred))))
            results2 = ((np.column_stack(([site, S, N, p] + weight.tolist()))))
                                         
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
    dataset_name = dataset
        
    raw_data = import_abundance(datafile) # Import data
    
    model_comparisons(raw_data, dataset_name, data_dir, cutoff = 9) # Run analyses on data