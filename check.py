from __future__ import print_function
import os


datasets = ['bbs', 'mcdb']

print('checking outputs:\n')

for dataset in datasets:
    os.system('Rscript check-outputs.R ' + dataset)


print('\nchecking likelihood consistency:\n')

for dataset in datasets:
    os.system('Rscript check-likelihood-consistency.R ' + dataset)
