sad-comparison
==============

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.165832.svg)](https://doi.org/10.5281/zenodo.165832)

####Repository for comparisons among species abundance distribution (SAD) models.

#####Data:   
Community data the same as used in White EP, Thibault KM, Xiao X.  2012.  Characterizing species abundance distributions across taxa and ecosystems using a simple maximum entropy model. Ecology. 93(8):1772-1778.  Further details and scripts for data extraction and processing can be found in the GitHub repository for that paper at https://github.com/weecology/white-etal-2012-ecology
Additional community data for Actinopterygii, Reptilia, Coleoptera, Arachnida, and Amphibia were mined from the literature and are publicly available for import through the EcoData Retriever (https://github.com/weecology/retriever) or on figshare (Baldridge, Elita (2013): Community abundance data. figshare. http://dx.doi.org/10.6084/m9.figshare.769251)

. 

#####Python dependencies:  
METE: https://github.com/weecology/METE.git  
macroecotools: https://github.com/weecology/macroecotools.git  
matplotlib  
basemap for matplotlib: http://matplotlib.org/basemap/users/installing.html#installation
numpy    
scipy  
pandas  
seaborn   

The METE module and the macroecotools module can be installed from the command line (with appropriate permissions)  
git clone https://github.com/weecology/METE.git  
cd METE  
python setup.py install (sudo python setup.py install on Linux)  
cd ..  
git clone https://github.com/weecology/macroecotools.git  
cd macroecotools  
python setup.py install (with sudo for Linux)    


#####SAD models tested and packages used:  
Maximum Entropy Theory of Ecology (METE) (METE)  
Logseries (macroecotools/macroeco_distributions)  
Poisson lognormal (macroecotools/macroeco_distributions)  
Negative binomial (macroecotools/macroeco_distributions)  
Geometric series (macroecotools/macroeco_distributions)  

    
Neutral theory: Because neutral theory predicts the negative binomial distribution at the local scale (Connolly et al. 2014. Commonness and rarity in the marine biosphere. PNAS 111: 8524-8529. http://www.pnas.org/content/111/23/8524.abstract), we used the prediction for the negative binomial distribution (macroecotools/macroecodistributions) instead of fitting the neutral theory model directly.  The AICc for neutral theory was calculated with the appropriate number of parameters for neutral theory.

To reproduce the workflow and analyses in this repository, run:  
   
misc-data-query.py to extract the Baldridge 2013 data used in addition to the White 2012 data (Data were first imported into an sqlite database with the EcoData Retriever).  

AND  

sad-comparisons.py to perform the analyses  
  
sad-process-db.py to create a database from the analysis results from sad-comparisons.py  
  
sad-comparison-graphs.py to generate the figures

OR  

sad_neutral_analysis.py to perform the analysis and generate the figures.

