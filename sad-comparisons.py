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
   
    
    Neutral theory: Neutral theory predicts the negative binomial distribution (Connolly et al. 2014. Commonness and rarity in the marine biosphere. PNAS 111: 8524-8529. http://www.pnas.org/content/111/23/8524.abstract
    
    """
    usites = np.sort(list(set(raw_data["site"])))
    
    # Open output files
    output1 = csv.writer(open(data_dir + dataset_name + '_obs_pred.csv','wb'))
    output2 = csv.writer(open(data_dir + dataset_name + '_dist_test.csv','wb')) 
    
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
            print('METE predicted')
            
            # Calculate log-likelihoods of species abundance models:
            # Logseries
            L_logser = md.logser_ll(obsabundance, p) # Log-likelihood of truncated logseries
            print('Truncated logseries predicted')
            L_logser_untruncated = md.logser_ll(obsabundance, p_untruncated) # Log-likelihood of untruncated logseries
            print('Untruncated logseries predicted')
            
            # Poisson lognormal
            mu, sigma = md.pln_solver(obsabundance)
            L_pln = md.pln_ll(obsabundance, mu,sigma) # Log-likelihood of Poisson lognormal
            print('Poisson lognormal predicted')
            
           
            # Negative binomial
            n0, p0 = md.negbin_solver(obsabundance)
            L_negbin = md.negbin_ll(obsabundance, n0, p0) # Log-likelihood of negative binomial
            print('Negative binomial predicted ' + str(L_negbin))
            
            # Generalized Yule
            list_obsabundance = obsabundance.tolist() # Yule solver uses list method incompatible with NumPy array.
            a, b = md.gen_yule_solver(list_obsabundance)
            L_gen_yule = md.gen_yule_ll(obsabundance, a, b)
            print('Generalized Yule predicted')

            
            # Calculate Akaike weight of species abundance models:
            # Parameter k is the number of fitted parameters
            k1 = 1
            k2 = 2
            
            # Calculate AICc values
            AICc_logser = macroecotools.AICc(k2, L_logser, S) # AICc logseries
            print("AICc truncated logseries: " + str(AICc_logser))
            AICc_logser_untruncated = macroecotools.AICc(k1, L_logser_untruncated, S) # AICc logseries untruncated
            print("AICc untruncated logseries calculated: " + str(AICc_logser_untruncated))
            AICc_pln = macroecotools.AICc(k2, L_pln, S) # AICc Poisson lognormal
            print("AICc Poisson lognormal calculated: " + str(AICc_pln))
            AICc_negbin = macroecotools.AICc(k2, L_negbin, S)# AICc negative binomial
            print("AICc negative binomial calculated: " + str(AICc_negbin))
            AICc_gen_yule = macroecotools.AICc(k2, L_gen_yule, S)# AICc generalized Yule
            print("AICc generalized Yule calculated: " + str(AICc_gen_yule))
                        
            
            # Make list of AICc values
            AICc_list = [AICc_logser, AICc_logser_untruncated, AICc_pln, AICc_negbin, AICc_gen_yule]
            print("AICc values collected")
            
            
            # Calulate AICc weight            
            weight = macroecotools.aic_weight(AICc_list, S, cutoff = 4)
            # Convert weight to list
            weights_output = weight.tolist()
            print("AICc weights calculated" + str(weights_output))
                                    
            # Format results for output
            results = ((np.column_stack((subsites, obsabundance, pred))))
            print("Predicted results ready for output.")
            results2 = [[site, S, N] + weights_output]
            print("AICc results ready for output: " + str(results2))
                                            
            # Save results to a csv file:            
            output1.writerows(results)
            output2.writerows(results2)
            print("Results output")



""" Function to see which predicted model fits best with the empirical data for each community. """

""" Plotting functions."""

# Set up analysis parameters
data_dir = './sad-data/' # path to data directory
analysis_ext = '_spab.csv' # Extension for raw species abundance files
testing_ext = '_spab_testing.csv'

datasets = ['naba', 'bbs', 'gentry', 'cbc'] # Dataset ID codes

# Starts actual analyses for each dataset in turn.
for dataset in datasets:
    datafile = data_dir + dataset + testing_ext
        
    raw_data = import_abundance(datafile) # Import data
    print("Dataset imported sucessfully.")
    
    model_comparisons(raw_data, dataset, data_dir, cutoff = 9) # Run analyses on data
    print("Dataset analysis complete.")