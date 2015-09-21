"""Export data in proper format for Connolly"""

import os

import pandas as pd

def import_data(datasets, datadir):
    """Import data files from the ./data directory"""
    data = pd.DataFrame()
    for dataset in datasets:
        print "Importing {} data".format(dataset)
        datafile = os.path.join(datadir, dataset + '_spab.csv')
        new_data = pd.read_csv(datafile, comment='#', usecols=['site_ID', 'species', 'abundance'])
        new_data = new_data[new_data['abundance'] > 0]
        new_data.insert(0, 'dataset', dataset)
        data = data.append(new_data, ignore_index=True)
    return data

def filter_data_minS(data, minS):
    """Only keep data with S>=minS for analysis"""
    return data.groupby(['dataset', 'site_ID']).filter(lambda x: len(x) >= minS)


datasets = ['Actinopterygii', 'Amphibia', 'Arachnida', 'bbs', 'cbc', 'Coleoptera',
            'fia', 'gentry', 'mcdb', 'naba', 'Reptilia']
data = import_data(datasets, './sad-data/chapter3/')
data = filter_data_minS(data, minS=5)
data_by_dataset = data.groupby(['dataset'])
for dataset, dataset_data in data_by_dataset:
    dataset_dedupped = dataset_data.drop_duplicates()
    if len(dataset_data) != len(dataset_dedupped):
        print("{} had {} duplicate site-species-abundance combinations out of {} records".format(dataset, len(dataset_data) - len(dataset_dedupped), len(dataset_data)))
        dataset_data = dataset_dedupped
    try:
        pivoted_data = dataset_data.pivot(index='species', columns='site_ID', values='abundance')
        pivoted_data.to_csv('./sad-data/chapter3/connolly_data/{}_pivoted_spab.csv'.format(dataset), float_format='%.0f')
    except ValueError:
        print("{} had duplicate site-species combinations".format(dataset))
