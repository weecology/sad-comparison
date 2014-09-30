sad-comparison
==============

####Repository for comparisons among species abundance distribution (SAD) models.

#####Data:   
Community data the same as used in White EP, Thibault KM, Xiao X.  2012.  Characterizing species abundance distributions across taxa and ecosystems using a simple maximum entropy model. Ecology. 93(8):1772-1778.  Further details and scripts for data extraction and processing can be found in the GitHub repository for that paper at https://github.com/weecology/white-etal-2012-ecology

#####Python dependencies:  
METE: https://github.com/weecology/METE.git  
macroecotools: https://github.com/weecology/macroecotools.git  
matplotlib  
numpy  
scipy 

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
