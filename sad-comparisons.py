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

def model_comparisons(raw_data, dataset_name, data_dir = './data/', cutoff = 9):
    """ Uses raw species abundance data to compare predicted vs. empirical species abundance distributions (SAD) and output results in csv files. 
    
    Keyword arguments:
    raw_data: numpy structured array with 4 columns: 'site', 'year', 'sp' (species), 'ab' (abundance).
    dataset_name: short code to indicate the name of the dataset in the output file names.
    data_dir: directory in which to store results output.
    cutoff: minimum number of species required to run -1.
    
    SAD models and packages used:
    Poisson lognormal (macroecotools/macroecodistributions)
    Logseries (macroecotools/macroecodistributions)
    Geometric (macroecotools/macroecodistributions)
    Sugihara (macroeco/distributions)
    Negative binomial (macroeco/distributions)
    Maximum Entropy Theory of Ecology (METE) (METE)
    
    Neutral theory ()
    
    """


""" Function to see which predicted model fits best with the empirical data for each community. """

""" Plotting functions."""
