""" Script for graphing the Baldridge 2012 MiscDB for publication. """
import csv
import sys
import multiprocessing
import os
import numpy as np
import sqlite3 as dbapi
import re
import matplotlib.pyplot as plt
import numpy as np

sys.float_info[2]

# Function for bar graphing
def bar_graph(filename, data, ylabel_name, xlabel_name):
    N = len(data)
    x = np.arange(1, N+1)
    y = [ num for (s, num) in data ]
    labels = [ s for (s, num) in data ]
    width = 1
    bar1 = plt.bar( x, y, width, color="grey" )
    plt.ylabel(ylabel_name  )
    plt.xticks(x + width/2.0, labels, fontsize = 'small' )
    plt.xlabel( xlabel_name)
    #Output figure
    plt.savefig(filename, format="png" )
    plt.close()    

# Set up database capabilities 
# Set up ability to query data
con = dbapi.connect('./sad-data/chapter2/misc.sqlite')
cur = con.cursor()
# Switch con data type to string
con.text_factory = str 

#Count the number of sites for each biogeographic region
bioregions = cur.execute("""SELECT DISTINCT(biogeographic_region) AS region, COUNT(site_id) AS sites FROM
                            miscabundancedb_sites
                            GROUP BY region""")
bioregions = cur.fetchall()
#Make bar graph of sites per biogeographic region
bioregions_graph = './sad-data/chapter2/bioregions.png'
ylabel_name = "Number of sites"
xlabel_name = "Biogeographic regions"
bar_graph(bioregions_graph, bioregions, ylabel_name, xlabel_name)

#Count the number of individuals for each taxon
num_taxa = cur.execute("""SELECT DISTINCT(class) AS class, COUNT(species) AS count_individuals FROM
                            miscabundancedb_main
                            GROUP BY class""")
num_taxa = cur.fetchall()
#Make bar graph of number of individuals for each taxon
taxa_graph = './sad-data/chapter2/num_taxa.png'
ylabel_name = "Total individuals"
xlabel_name = "Class"
bar_graph(taxa_graph, num_taxa, ylabel_name, xlabel_name)

#Count the number of sites for each taxon
sites_taxa = cur.execute("""SELECT DISTINCT(class) AS class, COUNT(DISTINCT(site_id)) AS sites FROM
                            miscabundancedb_main
                            GROUP BY class""")
sites_taxa = cur.fetchall()
#Make bar graph of number of sites for each taxon
taxa_sites_graph = './sad-data/chapter2/taxa_sites.png'
ylabel_name = "Number of sites"
xlabel_name = "Class"
bar_graph(taxa_sites_graph, sites_taxa, ylabel_name, xlabel_name)


#Close connection
con.close()

