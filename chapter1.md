#Chapter 1

# Introduction
Very important first sentence.
###Proliferation of SAD models, no agreement about winners. (citations galore)
A fundamental and ubiquitous ecological pattern is the presence of many rare species and few super abundant species within a community, forming a hollow curve distribution.  Because of the generality of this pattern, the species abundance distribution (SAD) has been one of the most widely studied patterns in ecology, leading to a proliferation of models that attempt to characterize the shape of the distribution and identify potential mechanisms for the pattern. The most recent comprehensive review and classification of species abundance distributions was given by McGill et al. 2007.




###Statistical descriptions of SAD distributions, vs. process based.
### Set up process and non process based model overlap (same form)  
There are two classes of species abundance distribution models, process based models, and non-process based models.  Constraints in a process based model of species abundance distributions (SADs) provide a predicted form of a distribution, based on an assumption that the constraints that produce the form of the distribution are biologically meaningful(relevant?).  However, non-process based species abundance distribution models are purely statistical descriptions of the shape of the distribution, and do not infer any biological meaning to the constraints of the distribution.  While the goal of a process based model is to identify pattern generating mechanisms, process based models can share the same forms as other process based or non-process based species abundance distribution models.  Because of the overlap between/among models, it can be difficult to identify potential mechanisms with any degree of certainty (if two models have an identical form, it is impossible to say which model is 'correct').  

###No difference between models?  Maybe, but...

Some have suggested that there is effectively no difference between models because of the difficulty involved in distinguishing between models (citations).  While there have been some studies that compete species abundance distribution models against one another, (citations including the Ulrich one) there has not yet been a comprehensive comparison across models using the most rigorous statistical approaches, large datasets, or across multiple taxonomic groups.  One of the McGill papers provides a conceptual framework for rigorous testing of alternative species distribution models. Details to follow.  One of the things is likelihoods, another of the things is multiple datasets. 


###No comprehensive comparision across models using the most rigorous statistical approaches, large datasets (plus across taxonomic groups).


# Methods
###Data, (from White et al 2012, minus the broken Gentry site 102 or something like that).
I used the following datasets analyzed by White et al. 2012 to test the performance of five species abundance distribution models.  

####BBS
The North American Breeding Bird Survey (BBS) is a publicly available dataset, etc. etc.  available <link to BBS data> (BBS;
Sauer et al. 2011). Number of sites.
####CBC
The Christmas Bird Count (CBC) is conducted by volunteers, etc. not publicly available, MOU, (CBC; National Audubon Society 2002). Number of sites.
####Gentry
The Alwyn Gentry’s Forest Transect dataset (Gentry) information about Gentry data (Gentry; Phillips and
Miller 2002). Number of sites.
####FIA
The Forest Inventory Analysis (FIA) information, etc. (FIA; USDA Forest Service 2010). Number of sites.
####MCDB
The Mammal Community Database (MCDB) publicly available at Ecological Archives <link> (MCDB, Thibault et al. 2011). Number of sites.
####NABA    
The North American Butterfly Count data (NABA) is conducted by volunteers, details, not publicly available, MOU, (NABA; North American Butterfly Association 2009). Number of sites.

Gentry site 102 was culled from the dataset due to a previously unidentified flaw in that site (one species had a decimal rather than integer abundance).  In total, I used data for 15,847 communities across four taxonomic groups over six large datasets.  The data have a North American bias, as the BBS, CBC, and FIA data are restricted to North America.

A small percentage of sites in the FIA dataset blew up on the negative binomial and the Poisson lognormal and one site in the MCDB blew up on the Poisson lognormal.  All other model/data combinations seemingly fit correctly for everything. 

###Likelihood based statistical comparison (White et al 2008, Edwards et al 2007, 2008)
I used a maximum likelihood approach because it is the best one for model comparison (citations).
Used AICc (citations).
Packages used to do analysis.
(macroecotools/macroeco_distributions)<https://github.com/weecology/macroecotools.git>
Also compared multiple datasets for multiple models because more rigorous (McGill et al. 2007)


###Model selection (justification of why we chose those, justification for neutral theory, Neutral theory predicts the negative binomial distribution (Connolly et al. 2014.)
List of models used, packages used to implement code

McGill et al. (2007) classified models into five different families.  I attempted to test models from each of the separate families, excluding the spatial distribution family (McGill et al. 2007) because that requires data at a finer spatial resolution, and was outside the scope of this study.  I had initially tried to test the generalized Yule model (branching process family), but this model proved difficult to fit to empirical data and failed to converge to a solution for many of the communities, so it was excluded from the final analyses.

This might be a place to talk about the Ulrich paper, because it seems like their power-law choice was in the branching process family.  Thus, connecting the not using the gen Yule to the Ulrich paper might be important here.

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
Code neccessary to duplicate analyses and figures is available at <https://github.com/weecology/sad-comparison>. The majority of the raw data neccessary to duplicate the analyses are provided in the sad-data folder in the GitHub repository; however, the CBC datasets and NABA datasets are not publicly available and were not included.


# Results
The untruncated logseries had the best model fit in the majority of cases, for all datasets combined (Figure 1).  However, the pattern varied for each dataset individually.  For the BBS, CBC, FIA, MCDB, and NABA data, the untruncated logseries provided the best fit, while the Poisson lognormal provided the best model fit for the Gentry data, with the untruncated logseries coming in a close second (Figure 2).  The geometric performed the worst for all datasets (Figure 1), and was never the best fit for the BBS, CBC, Gentry, and NABA datasets (Figure 2).  The negative binomial distribution failed to fit a small number of sites (get actual numbers).

The actual distribution of AICc weights varied with each model.  The peaks of the AICc weights tended to overlap for the logseries, negative binomial, and Poisson lognormal (Figure 3), although the Poisson lognormal had an additional smaller peak around 1, indicating that it had very good model fit in the cases where it was the winning model (Figure 3).  The majority of the AICc weights for the geometric series were near zero (Figure 3).

Assorted colorful graphs (check Post-It notes).

# Discussion

Statistical difference vs. biological relevance (i.e., is there enough difference that we can distinguish between possible mechanisms)

Different processes can generate identical models. (expansion of point from introduction)

Paragraph on the Ulrich et al. 2010 paper. (limitations of their approach)

Next steps: identify if there are explanatory patterns in winning model by taxonomic group or by space.

# References
Connolly et al. 2014. Commonness and rarity in the marine biosphere. PNAS 111: 8524-8529.
McGill, B.J. et al. 2007. Species abundance distributions: moving beyond single prediction theories to integration within an ecological framework. Ecology Letters 10 995-1015.  
Ulrich, W., Ollik, M. and K. I. Ugland. 2010. A meta-analysis of species–abundance distributions. Oikos, 119: 1149–1155.

###Data
National Audubon Society. 2002. The Christmas Bird Count
historical results. National Audobon Society, New York,
New York, USA. http://www.audubon.org/bird/cbc  
North American Butterfly Association 2009. Butterfly Count Data, 2009.  
Phillips, O., and J. S. Miller. 2002. Global patterns of plant
diversity: Alwyn H. Gentry’s forest transect data set.
Missouri Botanical Garden Press, St. Louis, Missouri, USA.  
Sauer, J. R., J. E. Hines, J. E. Fallon, K. L. Pardieck, D. J. Ziolkowski, Jr., and Link, W. A. 2011. The
North American Breeding Bird Survey, Results and Analysis 1966 - 2010. Version 12.07.2011    
USGS Patuxent Wildlife Research Center, Laurel, MD
Thibault, K.M., Supp, S.R., Giffin, M., White, E.P, and Ernest, S.K.M. 2011. Species composition and
abundance of mammalian communities. Ecology 92: 2316.  
USDA Forest Service. 2010. Forest inventory and analysis
national core field guide (Phase 2 and 3). Version 4.0. USDA
Forest Service, Forest Inventory and Analysis, Washington,
D.C., USA.






