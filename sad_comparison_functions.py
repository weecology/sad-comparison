"""Aggregated functions for the sad-comparison project"""
from __future__ import division
import numpy as np
import macroeco_distributions as md
import macroecotools
import scipy.stats.distributions as sd
import mete
import csv

# Define dictionary to match names to distributions
DIST_DIC = {'logser': sd.logser,
            'geom': sd.geom,
            'zipf': sd.zipf,
            'negbin': md.nbinom_lower_trunc,
            'pln': md.pln}

def import_abundance(datafile):
    """Imports raw species abundance .csv files in the form: Site, Year, Species, Abundance."""
    raw_data = np.genfromtxt(datafile, dtype = "S30,i8,S30,i8", names = ['site','year','sp','ab'], delimiter = ",",comments = "#")
    return raw_data

def get_par_multi_dists(ab, dist_name):
    """Returns the parameters given the observed abundances and the designated distribution."""
    if dist_name == 'logser':
        beta = mete.get_beta(len(ab), sum(ab), version = 'untruncated')
        par = np.exp(-beta)
    elif dist_name == 'pln':
        par = md.pln_solver(ab)
    elif dist_name == 'geom':
        par = len(ab) / sum(ab)
    elif dist_name == 'negbin':
        par = md.negbin_solver(ab)
        if np.isnan(par[0]):
            par = None
    elif dist_name == 'zipf':
        par = md.zipf_solver(ab)
    else: 
        print "Error: distribution not recognized."
        par = None    
    return par

def get_pred_iterative(cdf_obs, dist, *pars):
    """Function to get predicted abundances (reverse-sorted) for distributions with no analytical ppf."""
    cdf_obs = np.sort(cdf_obs)
    abundance  = list(np.empty([len(cdf_obs)]))
    j = 0
    cdf_cum = 0
    i = 1
    while j < len(cdf_obs):
        cdf_cum += dist.pmf(i, *pars)
        while cdf_cum >= cdf_obs[j]:
            abundance[j] = i
            j += 1
            if j == len(cdf_obs):
                abundance.reverse()
                return np.array(abundance)
        i += 1

def get_sample_multi_dists(S, dist_name, *pars):
    """Returns a random sample of length S from the designated distribution."""
    dist = DIST_DIC[dist_name]
    if dist_name == 'pln': pars += (True, )
    rand_smp = dist.rvs(*pars, size = S)
    return rand_smp

def get_pred_multi_dists(S, dist_name, pars):
    """Returns the predicted abundances given species richness, 
    
    the designated distribution, and the parameters.
    
    """
    cdf = (np.arange(1, S + 1) - 0.5) / S
    cdf = cdf[::-1]
    if dist_name == 'logser':
        pred = get_pred_iterative(cdf, sd.logser, pars)
    elif dist_name == 'pln':
        mu, sigma = pars
        pred = get_pred_iterative(cdf, md.pln, mu, sigma, True)
    elif dist_name == 'geom':
        pred = sd.geom.ppf(cdf, pars)
    elif dist_name == 'negbin':
        n, p = pars
        pred = get_pred_iterative(cdf, md.nbinom_lower_trunc, n, p)
    elif dist_name == 'zipf':
        pred = get_pred_iterative(cdf, sd.zipf, pars)
    else: 
        print "Error: distribution not recognized."
        pred = None
    return pred

def get_loglik_multi_dists(ab, dist_name, *pars):
    """Returns the log-likelihood given abundances, 
    
    the designated distribution, and the parameters.
    
    """
    dist = DIST_DIC[dist_name]
    if dist_name == 'pln': pars += (True,)
    loglik = sum(np.log(dist.pmf(ab, *pars)))
    return loglik

def get_ks_multi_dists(ab, dist_name, pars):
    """Returns the K-S statistic given abundances, 
    
    the designated distribution, and the parameters.
    
    """
    ab = sorted(ab)
    emp_cdf = (np.arange(1, len(ab) + 1) - 0.5) / len(ab)  
    dist = 0
    if dist_name == 'logser': dist = sd.logser
    elif dist_name == 'geom': dist = sd.geom
    elif dist_name == 'zipf': dist = sd.zipf
    if dist: # If one of the above three cases:
        ks = max(abs(emp_cdf - np.array([dist.cdf(x, pars) for x in ab])))
    else:
        if dist_name == 'negbin':
            n, p = pars
            ks = max(abs(emp_cdf - np.array([md.nbinom_lower_trunc.cdf(x, n, p) for x in ab])))
        elif dist_name == 'pln':
            mu, sigma = pars
            ks = max(abs(emp_cdf - np.array([md.pln.cdf(x, mu, sigma, True) for x in ab])))
    return ks
    
def get_obs_pred_multi_dists(dat_dir, file_name, dist_name, cutoff = 9):
    """Obtain obs-pred RADs for each site in each dataset and write to file."""
    out_write = open(dat_dir + file_name + '_' + dist_name + '_obs_pred.csv', 'wb')
    out = csv.writer(out_write)    
    dat = import_abundance(dat_dir + file_name + '_spab.csv')
    sites = np.unique(dat['site'])
    for site in sites:
        dat_site = dat[dat['site'] == site]
        obs_site = np.sort(dat_site['ab'])[::-1]
        if len(obs_site) > cutoff: 
            pars_dist_site = get_par_multi_dists(obs_site, dist_name)
            if pars_dist_site and (np.any(np.isnan(pars_dist_site)) == 0):  # The estimated parameters exist and are not NANs
                pred_dist_site = get_pred_multi_dists(len(obs_site), dist_name, pars_dist_site)
                results = np.zeros((len(obs_site), ), dtype = ('S30, i8, i8'))
                results['f0'] = np.array([site] * len(obs_site))
                results['f1'] = obs_site
                results['f2'] = pred_dist_site
                out.writerows(results)
    out_write.close()
            
def sim_stats(ab, dist_name, Nsim, test_stat):
    """Obtain Nsim abundance lists from the proposed distribution 
    
    and compare their fit with the empirical data (Connolly et al. 2009).
    Inputs:
    ab - list of empirical abundaces
    dist_name - name of the distribution under examination
    Nsim - number of simulated abundance lists
    test_stat - can be either log-likelihood ('loglik'), Kolmogorov-Smirnov statistic ('ks'), or R^2 ('r2')
    Output: 
    A list where the first element is the stat value for the empirical SAD and the remaining values are stats for the simulated SADs.
    
    """
    pars = get_par_multi_dists(ab, dist_name)
    if test_stat == 'loglik': test_func = get_loglik_multi_dists
    elif test_stat == 'ks': test_func = get_ks_multi_dists
    elif test_stat == 'r2': 
        def test_func(ab, dist_name, pars):
            pred = get_pred_multi_dists(len(ab), dist_name, pars)
            r2 = macroecotools.obs_pred_rsquare(sorted(ab, reverse = True), pred)
            return r2
    out_list = [test_func(ab, dist_name, pars)]
    for i in range(Nsim):
        sim_sad = get_sample_multi_dists(len(ab), dist_name, pars)
        out_list.append(test_func(sim_sad, dist_name, pars))
    return out_list
