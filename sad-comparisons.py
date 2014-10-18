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

import sys # Fix for the -inf problem
sys.float_info[3]

def import_abundance(datafile):
    """Imports raw species abundance .csv files in the form: Site, Year, Species, Abundance."""
    raw_data = np.genfromtxt(datafile, dtype = "S15,i8,S10,i8", names = ['site','year','sp','ab'], delimiter = ",",comments = "#")
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
    Geometric series (macroecotools/macroecodistributions)

    Neutral theory: Neutral theory predicts the negative binomial distribution (Connolly et al. 2014. Commonness and rarity in the marine biosphere. PNAS 111: 8524-8529. http://www.pnas.org/content/111/23/8524.abstract
    
    """
    usites = np.sort(list(set(raw_data["site"])))
    
    # Open output files
    output1 = csv.writer(open(data_dir + dataset_name + '_obs_pred.csv','wb'))
    output2 = csv.writer(open(data_dir + dataset_name + '_dist_test.csv','wb'))
    output3 = csv.writer(open(data_dir + dataset_name + '_likelihoods.csv','wb'))
    output4 = csv.writer(open(data_dir + dataset_name + '_relative_L.csv','wb'))
    
    # Insert header
    output1.writerow(['site', 'observed', 'predicted'])
    output2.writerow(['site', 'S', 'N', 'AICc_logseries', 'AICc_logseries_untruncated', 'AICc_pln', 'AICc_negbin', 'AICc_geometric'])
    output3.writerow(['site', 'S', 'N', 'likelihood_logseries', 'likelihood_logseries_untruncated', 'likelihood_pln', 'likelihood_negbin', 'likelihood_geometric'])
    output4.writerow(['site', 'S', 'N', 'relative_ll_logseries', 'relative_ll_logseries_untruncated', 'relative_ll_pln', 'relative_ll_negbin', 'relative_ll_geometric'])
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
            
            # Calculate Akaike weight of species abundance models:
            # Parameter k is the number of fitted parameters
            k1 = 1
            k2 = 2            
            
            # Calculate log-likelihoods of species abundance models and calculate AICc values:
            # Logseries
            L_logser = md.logser_ll(obsabundance, p) # Log-likelihood of truncated logseries
            L_logser_untruncated = md.logser_ll(obsabundance, p_untruncated) # Log-likelihood of untruncated logseries
            AICc_logser = macroecotools.AICc(k2, L_logser, S) # AICc logseries
            AICc_logser_untruncated = macroecotools.AICc(k1, L_logser_untruncated, S) # AICc logseries untruncated
            relative_ll_logser = macroecotools.AICc(k1, L_logser, S) # Relative likelihood truncated logseries
            relative_ll_logser_untruncated = macroecotools.AICc(k1, L_logser_untruncated, S)# Relative likelihood untruncated logseries
            
            #Start making AICc list
            AICc_list = [AICc_logser, AICc_logser_untruncated]
            likelihood_list = [L_logser, L_logser_untruncated]
            relative_likelihood_list = [relative_ll_logser, relative_ll_logser_untruncated]
          
            
            # Poisson lognormal
            mu, sigma = md.pln_solver(obsabundance)
            L_pln = md.pln_ll(obsabundance, mu,sigma) # Log-likelihood of Poisson lognormal
            if np.isinf(L_pln):
                pln_blank = 1  # The Poisson lognormal returned -inf
                
            if L_pln > 0:
                pln_blank = 1  # The Poisson lognormal returned a log-likelihood greater than 1

            else:
                AICc_pln = macroecotools.AICc(k2, L_pln, S) # AICc Poisson lognormal
                relative_ll_pln = macroecotools.AICc(k1, L_pln, S) #Relative likelihood, Poisson lognormal
                # Add to AICc list
                AICc_list = AICc_list + [AICc_pln]
                pln_blank = 0
                likelihood_list = likelihood_list +  [L_pln]
                relative_likelihood_list = relative_likelihood_list + [relative_ll_pln]
       
            # Negative binomial
            n0, p0 = md.negbin_solver(obsabundance)
            L_negbin = md.negbin_ll(obsabundance, n0, p0) # Log-likelihood of negative binomial
            if np.isnan(L_negbin):
                negbin_blank = 1 # The negative binomial distribution sometimes fails to come to a solution before the maximum number of iterations.
                
            elif np.isinf(L_negbin):
                negbin_blank = 1 # The negative binomial distribution returned -inf            
                
            else:
                AICc_negbin = macroecotools.AICc(k2, L_negbin, S)# AICc negative binomial
                relative_ll_negbin = macroecotools.AICc(k1, L_negbin, S) # Relative log-likelihood of negative binomial
                # Add to AICc list
                AICc_list = AICc_list + [AICc_negbin]
                negbin_blank = 0
                likelihood_list = likelihood_list +  [L_negbin]
                relative_likelihood_list = relative_likelihood_list + [relative_ll_negbin]
                

            # Geometric series
            p = md.trunc_geom_solver(obsabundance, N) # For the upper bound, we are using the total community abundance
            L_geometric = md.geom_ll(obsabundance, p) # Log-likelihood of geometric series
            AICc_geometric = macroecotools.AICc(k1, L_geometric, S) # AICc geometric series
            relative_ll_geometric = macroecotools.AICc(k1, L_geometric, S) # Relative log-likelihood of geometric series
            # Add to AICc list
            AICc_list = AICc_list + [AICc_geometric]
            likelihood_list = likelihood_list +  [L_geometric]
            relative_likelihood_list = relative_likelihood_list + [relative_ll_geometric]
            
            # Calculate AICc weight            
            weight = macroecotools.aic_weight(AICc_list, S, cutoff = 4)
            
            #Calculate relative likelihood
            relative_likelihoods = macroecotools.aic_weight(relative_likelihood_list, S, cutoff = 4)
            
            # Convert weight to list
            weights_output = weight.tolist()
            
            #Convert relative likelihoods to list
            relative_likelihoods_output = relative_likelihoods.tolist() 
            
            # Inserts a blank in the output if the Poisson lognormal returned -inf or a positive likelihood
            if pln_blank == 1:
                weights_output.insert(2, '')
                likelihood_list.insert(2, '')
                relative_likelihoods_output.insert(2, '')
            
            # Inserts a blank in the output if the negative binomial exceeded the max number of iterations
            if negbin_blank == 1:
                weights_output.insert(3, '')
                likelihood_list.insert(3, '')
                relative_likelihoods_output.insert(3, '')
                                    
            # Format results for output
            results = ((np.column_stack((subsites, obsabundance, pred))))
            for weight in weights_output:
                results2 = [[site, S, N] + weights_output]
            results3 = [[site, S, N] + likelihood_list]
            results4 = [[site, S, N] + relative_likelihoods_output]

                                            
            # Save results to a csv file:            
            output1.writerows(results)
            output2.writerows(results2)
            output3.writerows(results3)
            output4.writerows(results4)


""" Function to see which predicted model fits best with the empirical data for each community. """

""" Plotting functions."""

# Set up analysis parameters
data_dir = './sad-data/' # path to data directory
analysis_ext = '_spab.csv' # Extension for raw species abundance files

datasets = ['bbs', 'cbc', 'fia', 'gentry', 'mcdb', 'naba'] # Dataset ID code


# Starts actual analyses for each dataset in turn.
for dataset in datasets:
    datafile = data_dir + dataset + analysis_ext
        
    raw_data = import_abundance(datafile) # Import data

    model_comparisons(raw_data, dataset, data_dir, cutoff = 9) # Run analyses on data

