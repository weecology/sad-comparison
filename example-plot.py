from __future__ import division
import numpy as np
import macroeco_distributions as md
from scipy.stats import zipf
import matplotlib
import matplotlib.pyplot as plt

ab = np.array([3L, 2L, 2L, 2L, 2L, 1L, 16L, 1L, 9L, 12L,
1L, 5L, 5L, 3L, 2L, 10L, 1L, 1L, 1L, 6L, 1L, 3L])
x_values = np.array(range(max(ab) + 2)[1:])

logser_p = md.logser_solver(ab)
logser_values = md.trunc_logser.pmf(x_values, logser_p, upper_bound=float("inf"))

nb_n, nb_p = md.nbinom_lower_trunc_solver(ab)
nb_values = md.nbinom_lower_trunc.pmf(x_values, nb_n, nb_p)

pln_mu, pln_sigma = md.pln_solver(ab)
pln_values = md.pln.pmf(x_values, pln_mu, pln_sigma, lower_trunc=True)

zipf_par = md.zipf_solver(ab)
zipf_values = zipf.pmf(x_values, zipf_par)

ab_y = np.zeros(len(x_values) + 1)
for i in range(len(ab)):
    ab_y[ab[i]] = ab_y[ab[i]] + 1/len(ab)

fig= plt.figure(figsize=(8, 6), dpi=400)
ax1 = fig.add_subplot(111)
ax1.set_xlim([0,max(x_values)])

plt.ylabel('frequency')
plt.xlabel('abundance')

ax1.vlines(x = x_values, ymin = [0], ymax = .0075, color = "#555555")
ax1.plot(x_values, logser_values, label = "log-series", linewidth = 1.5)
ax1.plot(x_values, nb_values, label = "negative binomial", linewidth = 1.5)
ax1.plot(x_values, pln_values, label = "Poisson-lognormal binomial", linewidth = 1.5)
ax1.plot(x_values, zipf_values, label = "zipf", linewidth = 1.5)
ax1.vlines(x = x_values, ymin=[0], ymax=ab_y[1:], linewidth = 1.5)
plt.legend(loc='upper right');
