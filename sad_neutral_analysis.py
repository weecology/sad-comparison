"""Analysis code for SAD based evaluation of ecological neutral theory

Conducts analyses in Connolly et al. 2014 (in PNAS) using ~17,000 empirical SADS

"""

import os
import glob
import functools

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from mpl_toolkits.axes_grid.inset_locator import inset_axes
from mpl_toolkits.basemap import Basemap

from macroecotools import AICc, aic_weight
from sad_comparison_functions import get_par_multi_dists, get_loglik_multi_dists

def get_dataset_name(pathname):
    """Extract dataset name from file path

    Filenames are of the form dataset_*

    """
    filename = os.path.split(pathname)[-1]
    dataset = filename.split('_')[0]
    return dataset

def import_data(datasets, datadir):
    """Import data files from the ./data directory"""
    data = pd.DataFrame()
    for dataset in datasets:
        print "Importing {} data".format(dataset)
        datafile = os.path.join(datadir, dataset + '_spab.csv')
        new_data = pd.read_csv(datafile, comment='#', usecols=['site_ID', 'abundance'])
        new_data = new_data[new_data['abundance'] > 0]
        new_data.insert(0, 'dataset', dataset)
        data = data.append(new_data, ignore_index=True)
    return data

def import_latlong_data(input_filename, comments='#'):
    data = np.genfromtxt(input_filename, dtype = "f8,f8",
                         names = ['lat','long'], delimiter = ",")
    return data

def filter_data_minS(data, minS):
    """Only keep data with S>=minS for analysis"""
    return data.groupby(['dataset', 'site_ID']).filter(lambda x: len(x) >= minS)

def get_llik(abundances, dist):
    """Get the loglikelihood for a given distribution and set of data"""
    paras = get_par_multi_dists(abundances, dist)
    if paras:
        llik = get_loglik_multi_dists(abundances, dist, *paras)
    else:
        llik = None
    return llik

def get_pln_aicc_wgts(sads):
    """Get the AICc weight"""
    min_aiccs = sads[['negbin_aicc', 'pln_aicc']].min(axis=1)
    negbin_delta_aicc = sads['negbin_aicc'] - min_aiccs
    pln_delta_aicc = sads['pln_aicc'] - min_aiccs
    pln_rel_lik = np.exp(-(pln_delta_aicc) / 2)
    negbin_rel_lik = np.exp(-(negbin_delta_aicc) / 2)
    return pln_rel_lik / (pln_rel_lik + negbin_rel_lik)

get_negbin_llik = functools.partial(get_llik, dist='negbin')
get_pln_llik = functools.partial(get_llik, dist='pln')

if os.path.isfile('./sad-data/chapter3/distribution_data.csv'):
    sads = pd.read_csv('./sad-data/chapter3/distribution_data.csv')
else:
    datasets = ['Actinopterygii', 'Amphibia', 'Arachnida', 'bbs', 'cbc', 'Coleoptera',
                'fia', 'gentry', 'mcdb', 'naba', 'Reptilia']
    data = import_data(datasets, './sad-data/chapter3/')
    data = filter_data_minS(data, minS=5)

    data_by_dataset_site = data.groupby(['dataset', 'site_ID'])
    sads = data_by_dataset_site.count()
    sads.rename(columns={'abundance': 'richness'}, inplace=True)
    sads['distinct_ab_vals'] = data_by_dataset_site['abundance'].nunique()
    sads['negbin_llik'] = data_by_dataset_site.agg(get_negbin_llik)
    sads['pln_llik'] = data_by_dataset_site.agg(get_pln_llik)
    sads['negbin_aicc'] = AICc(k=2, L=sads['negbin_llik'], n=sads['richness'])
    sads['pln_aicc'] = AICc(k=2, L=sads['pln_llik'], n=sads['richness'])
    sads['pln_aicc_wgt'] = get_pln_aicc_wgts(sads)
    sads.reset_index(inplace=True)
    sads.to_csv('./sad-data/chapter3/distribution_data.csv', index=False)

# Create figure similar to figure 2b in the Connolly 2014 paper.
sads = sads.dropna()
sads['log_distinct_ab_vals'] = np.log(sads['distinct_ab_vals'])
sns.set_style("whitegrid")
ax = sns.lmplot('log_distinct_ab_vals', 'pln_aicc_wgt', data=sads, col='dataset', col_wrap=4,
                hue='dataset', fit_reg=False)
ax.set(xlabel="Distinct Abundance Values (log)", ylabel="AICc weight for log-normal")
ax.set(xlim=[np.log(5), np.log(300)], ylim=[0, 1])
xticks = [10, 20, 50, 100, 200]
ax.set(xticks=np.log(xticks))
ax.set(xticklabels=xticks)
ax.savefig('./sad-data/chapter3/distabclasses_vs_lognormwgt.png')
plt.close()

# Create figure showing average values for each datasets

sads_by_dataset = sads.groupby('dataset').mean().reset_index()
ax = sns.lmplot('log_distinct_ab_vals', 'pln_aicc_wgt', data=sads_by_dataset,
                hue='dataset', fit_reg=False, scatter_kws={"s": 60, "alpha": 1})
ax.set(xlabel="Distinct Abundance Values (log)", ylabel="AICc weight for log-normal")
ax.set(xlim=[np.log(5), np.log(300)], ylim=[0, 1])
xticks = [10, 20, 50, 100, 200]
ax.set(xticks=np.log(xticks))
ax.set(xticklabels=xticks)
ax.savefig('./sad-data/chapter3/avgvals_by_dataset.png')
plt.show()
plt.close()

#Mapping code modified from White et al. 2012
"""Generate a world map with sites color-coded by database"""
map = Basemap(projection='moll',lon_0=0,resolution='i') #Sets up map for Mollweide projection- chosen for equal area properties.

map.drawcoastlines(linewidth = .10)
map.fillcontinents(color='black',lake_color='white')

datasets = ['bbs', 'fia', 'gentry', 'mcdb'] # The rest of the data do not have lat-longs.
data_dir = './sad-data/chapter1/'
markers=['o','s','D','v']
markersizes=3
colors=["teal", "palegreen", "m", "gold"]


for i, dataset in enumerate(datasets):
    latlong_data = import_latlong_data(data_dir + dataset + '_lat_long.csv')
    lats = latlong_data["lat"]
    longs = latlong_data["long"]
    x,y = map(longs,lats)
    map.plot(x,y, ls='', marker=markers[i], markeredgecolor= colors[i],
    markeredgewidth=0.75, markersize=markersizes, fillstyle='none')
    

#Make legend
l1 = plt.scatter([],[], s=100, marker = 'o', facecolors='teal',  edgecolors='black')
l2 = plt.scatter([],[], s=100, marker = 's', facecolors='palegreen', edgecolors='black')
l3 = plt.scatter([],[], s=100, marker = 'D', facecolors='m', edgecolors='black')
l4 = plt.scatter([],[], s=100, marker = 'v', facecolors='gold', edgecolors='black')

labels = ["BBS", "FIA", "Gentry", "MCDB"]

leg = plt.legend([l1, l2, l3, l4], labels, frameon=False, fontsize=12, loc = 6, title='Datasets', scatterpoints = 1)
    
plt.savefig('./sad-data/chapter3/partial_sites_map.png', dpi=250, pad_inches=0)
plt.close()