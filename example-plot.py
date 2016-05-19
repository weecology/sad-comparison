from __future__ import division
import numpy as np
import macroeco_distributions as md
from scipy.stats import zipf
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline

# BBS
# fia site 14057000012
# Gentry site 95
ab_array = np.array([[1L, 4L, 2L, 17L, 23L, 1L, 7L, 2L, 5L, 1L, 5L, 2L, 4L, 13L,
1L, 4L, 7L, 11L, 12L, 2L, 1L, 17L, 35L, 16L, 88L, 10L, 2L, 1L,
15L, 52L, 10L, 1L, 1L, 14L, 1L, 1L, 9L, 2L, 17L, 105L, 9L, 7L,
45L, 14L, 2L, 7L, 24L, 15L, 4L, 2L, 3L, 9L, 7L, 10L, 3L, 29L,
1L, 2L, 7L, 11L, 9L, 5L, 22L, 2L, 27L, 14L, 1L, 2L, 11L, 4L,
21L, 114L, 22L, 44L, 9L, 5L, 2L, 2L, 6L, 16L, 10L],
              [2L, 1L, 1L, 2L, 1L, 2L, 1L, 5L, 1L, 1L, 1L, 4L, 7L, 2L, 1L,
2L, 1L, 3L, 5L, 1L, 1L],
             [4L, 22L, 7L, 12L, 2L, 6L, 2L, 15L, 5L, 6L, 1L, 3L, 1L, 2L,
3L, 6L, 1L, 3L, 2L, 3L, 9L, 5L, 8L, 2L, 5L, 1L, 5L, 7L, 4L, 1L,
4L, 3L, 4L, 1L, 2L, 3L, 11L, 5L, 7L, 3L, 1L, 2L, 1L, 1L, 1L,
4L, 1L, 1L, 9L, 3L, 8L, 3L, 2L, 10L, 4L, 14L, 4L, 2L, 3L, 1L,
1L, 8L]])

# rearranged from http://www.cookbook-r.com/Graphs/Colors_%28ggplot2%29/#a-colorblind-friendly-palette
colors = ["#F0E442", "#D55E00", "#E69F00", "#56B4E9", "#009E73", "#0072B2", "#999999", "#CC79A7"]

for i in range(3):
    ab = ab_array[i]

    x_values = np.array(range(max(ab) + 2)[1:])

    logser_p = md.logser_solver(ab)
    logser_values = md.trunc_logser.pmf(x_values, logser_p, upper_bound=float("inf"))
    lsll = md.logser_ll(ab, logser_p)

    nb_n, nb_p = md.nbinom_lower_trunc_solver(ab)
    nb_values = md.nbinom_lower_trunc.pmf(x_values, nb_n, nb_p)
    nbll = md.nbinom_lower_trunc_ll(ab, nb_n, nb_p)

    pln_mu, pln_sigma = md.pln_solver(ab)
    pln_values = md.pln.pmf(x_values, pln_mu, pln_sigma, lower_trunc=True)
    plnll = md.pln_ll(ab, pln_mu, pln_sigma)

    zipf_par = md.zipf_solver(ab)
    zipf_values = zipf.pmf(x_values, zipf_par)
    zll = md.zipf_ll(ab, zipf_par)

    ab_y = np.zeros(len(x_values) + 1)
    for i in range(len(ab)):
        ab_y[ab[i]] = ab_y[ab[i]] + 1/len(ab)

    fig= plt.figure(figsize=(12, 8), dpi=800)
    ax1 = fig.add_subplot(111)
    ax1.set_xlim([0,min(50, max(x_values))])
    #ax1.set_ylim([0,max(ab_y) * 1.25])

    plt.ylabel('frequency')
    plt.xlabel('abundance')

    # Width originally set at 12 when width was 50.
    # This should be the same proportional width
    width = 12 / min(50, max(x_values)) * 50

    ax1.vlines(x = x_values, ymin = [0], ymax = .0025, color = "#999999")
    ax1.vlines(x = x_values, ymin=[0], ymax=ab_y[1:], linewidth = width, color = "#999999")
    ax1.plot(x_values, logser_values, color = colors[1], label = "log-series: " + str(round(lsll)), linewidth = 1.5)
    ax1.plot(x_values, nb_values, color = colors[3], label = "negative binomial: " + str(round(nbll)), linewidth = 1.5)
    ax1.plot(x_values, pln_values, color = colors[7], label = "Poisson-lognormal: " + str(round(plnll)), linewidth = 1.5)
    ax1.plot(x_values, zipf_values, color = "k", label = "zipf: " + str(round(zll)), linewidth = 1.5)
    plt.legend(loc='upper right');
