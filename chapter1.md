#Chapter 1

# Introduction
Very important first sentence.
###Proliferation of SAD models, no agreement about winners. (citations galore)



Statistical descriptions of SAD distributions, vs. process based.
Thingies in a process based model of species abundance distributions (SADs) provide a predicted form of a distribution, based on an assumption that the thingies that make the form of the distribution are biologically meaningful.  However, some species abundance distribution models are purely statistical descriptions of the shape of the distribution.  While the goal of a process based model is to identify pattern generating mechanisms, process based models can share the same forms as other process based models, or a purely statistical description of the abundance distribution.  Because of the model overlap, it can be difficult to identify potential mechanisms with any degree of certainty (if two models have an identical form, it is impossible to say which model is 'correct').

### Set up process and non process based model overlap (same form)


###No difference between models?  Maybe, but...

Because of the difficulty involved in distinguishing between models, some have suggested that there is effectively no difference between models.  While there have been some studies that compete species abundance distribution models against one another, (citations including the Ulrich one) there has not yet been a comprehensive comparison across models using the most rigorous statistical approaches, large datasets, or across multiple taxonomic groups.

###No comprehensive comparision across models using the most rigorous statistical approaches, large datasets (plus across taxonomic groups).


# Methods
###Data, (from White et al 2012, minus the broken Gentry site 102 or something like that).
I used the data from White et al. 2012 for the analyses, but removed site 102 from the Gentry data set, due to a previously unidentified flaw in that site (one species had a decimal rather than integer abundance).  Total number of communities, four taxonomic groups over six large datasets.

####BBS
The North American Breeding Bird Survey (BBS) is a publicly available dataset, etc. etc.  available <link to BBS data> (BBS,
Sauer et al. 2011). Number of sites.
####CBC
The Christmas Bird Count (CBC) is conducted by volunteers, etc. not publicly available, MOU, (citation). Number of sites.
####Gentry
The something Gentry tree data (Gentry) information about Gentry data (citation). Number of sites.
####FIA
The Forest Inventory Analysis (FIA) information, etc. (citation). Number of sites.
####MCDB
The Mammal Community Database (MCDB) publicly available at Ecological Archives <link> (MCDB, Thibault et al. 2011). Number of sites.
####NABA    
The North American Butterfly Association data (NABA) is conducted by volunteers, details, not publicly available, MOU, (NABA, North American Butterfly Association 2009). Number of sites.

###Likelihood based statistical comparison (White et al 2008, Edwards et al 2007, 2008)
I used a maximum likelihood approach because it is the best one for model comparison (citations).
Used AICc (citations).
Packages used to do analysis.


###Model selection (justification of why we chose those, justification for neutral theory, Neutral theory predicts the negative binomial distribution (Connolly et al. 2014.)
List of models used, packages used to implement code

McGill (2007) classified models into several different families.  I attempted to test models from each of the separate families, excluding the population dynamic family and the spatial distribution of individuals family (McGill 2007), as these were not appropriate for testing with these data in this framework.  I had initially tried to test the generalized Yule model (branching process family), but this model proved difficult to fit to empirical data and failed to converge to a solution for many of the communities, so it was excluded from the final analyses.

Ethan's paper about discrete distributions being better finds that discrete approximations are more appropriate choices for model selection that continuous version of the distribution.

I tested the following distributions with the following packages: 

Might make this into a table, like the infamous Table 2.

Maximum Entropy Theory of Ecology (METE) <(METE)https://github.com/weecology/METE.git>
Logseries (macroecotools/macroeco_distributions)<https://github.com/weecology/macroecotools.git>
Untruncated logseries (macroecotools/macroeco_distributions)<https://github.com/weecology/macroecotools.git>
Poisson lognormal (macroecotools/macroeco_distributions)<https://github.com/weecology/macroecotools.git>
Negative binomial (macroecotools/macroeco_distributions)<https://github.com/weecology/macroecotools.git>
Geometric series (macroecotools/macroeco_distributions)<https://github.com/weecology/macroecotools.git> 




###Link to code.
Code neccessary to duplicate analyses is available at <https://github.com/weecology/sad-comparison>. The majority of the raw data neccessary to duplicate the analyses are provided in the sad-data folder in the GitHub repository; however, the CBC datasets and NABA datasets are not publicly available and were not included.


# Results
The untruncated logseries had the best model fit in the majority of cases, for all datasets combined (Figure 1).  However, the pattern varied for each dataset individually.  For the BBS, CBC, FIA, MCDB, and NABA data, the untruncated logseries provided the best fit, while the Poisson lognormal provided the best model fit for the Gentry data, with the untruncated logseries coming in a close second (Figure 2).  The truncated logseries performed the worst for all datasets (Figure 1), and was never the best fit for the BBS, CBC, Gentry, and NABA datasets (Figure 2).  The negative binomial distribution failed to fit a small number of sites (get actual numbers).

The actual distribution of AICc weights varied with each model.  The peaks of the AICc weights tended to overlap for the logseries, negative binomial, and Poisson lognormal (Figure 3), although the Poisson lognormal had an additional smaller peak around 1, indicating that it had very good model fit in the cases where it was the winning model (Figure 3).  The majority of the AICc weights for the geometric series were near zero (Figure 3).

Assorted colorful graphs (check Post-It notes).

# Discussion

Statistical difference vs. biological relevance (i.e., is there enough difference that we can distinguish between possible mechanisms)

Different processes can generate identical models. (expansion of point from introduction)

Paragraph on the Ulrich paper. (limitations of their approach)

# References
Connolly et al. 2014. Commonness and rarity in the marine biosphere. PNAS 111: 8524-8529.

###Data
North American Butterfly Association 2009. Butterfly Count Data, 2009.
Sauer, J. R., J. E. Hines, J. E. Fallon, K. L. Pardieck, D. J. Ziolkowski, Jr., and Link, W. A. 2011. The
North American Breeding Bird Survey, Results and Analysis 1966 - 2010. Version 12.07.2011
USGS Patuxent Wildlife Research Center, Laurel, MD
Thibault, K.M., Supp, S.R., Giffin, M., White, E.P, and Ernest, S.K.M. 2011. Species composition and
abundance of mammalian communities. Ecology 92: 2316.
Woudenberg, S.W., et al. 2010. The forest inventory and analysis database: database description and users
guide version 4.0 for phase 2. Gen. Tech. Rep. RMRS-GTR-245. Fort Collins, CO: U.S.
Department of Agriculture, Forest Service, Rocky Mountain Research Station. 336 p.






