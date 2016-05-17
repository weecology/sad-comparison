from __future__ import division
import numpy as np
import macroeco_distributions as md
from scipy.stats import zipf
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline

ab = np.array([1L, 4L, 2L, 17L, 23L, 1L, 7L, 2L, 5L, 1L, 5L, 2L, 4L, 13L,
1L, 4L, 7L, 11L, 12L, 2L, 1L, 17L, 35L, 16L, 88L, 10L, 2L, 1L,
15L, 52L, 10L, 1L, 1L, 14L, 1L, 1L, 9L, 2L, 17L, 105L, 9L, 7L,
45L, 14L, 2L, 7L, 24L, 15L, 4L, 2L, 3L, 9L, 7L, 10L, 3L, 29L,
1L, 2L, 7L, 11L, 9L, 5L, 22L, 2L, 27L, 14L, 1L, 2L, 11L, 4L,
21L, 114L, 22L, 44L, 9L, 5L, 2L, 2L, 6L, 16L, 10L])
x_values = np.array(range(max(ab) + 5)[1:])

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

fig= plt.figure(figsize=(15, 10), dpi=800)
ax1 = fig.add_subplot(111)
ax1.set_xlim([0,50])
ax1.set_ylim([0,max(ab_y) * 1.25])

plt.ylabel('frequency')
plt.xlabel('abundance')

ax1.vlines(x = x_values, ymin = [0], ymax = .0025, color = "#999999")
ax1.vlines(x = x_values, ymin=[0], ymax=ab_y[1:], linewidth = 12, color = "#999999")
ax1.plot(x_values, logser_values, "k-", label = "log-series: " + str(round(lsll)), linewidth = 1.5)
ax1.plot(x_values, nb_values, "b-", label = "negative binomial: " + str(round(nbll)), linewidth = 1.5)
ax1.plot(x_values, pln_values, "r-", label = "Poisson-lognormal: " + str(round(plnll)), linewidth = 1.5)
ax1.plot(x_values, zipf_values, "m-", label = "zipf: " + str(round(zll)), linewidth = 1.5)
plt.legend(loc='upper right');

# Notes:  I'm only showing 1:50 on the x axis because letting the axis go out to 114 would only show 4 more points
#          but would take twice as much space.
#         Zipf spends too much probability mass at both extremes and not enough in the middle, where most of the
#          values are. It gets essentially no weight.
#         NB and PLN fit best, but only by 2 LL points. This isn't enough to overcome the AICc penalty relative
#          to log-series, which is always at least 2
