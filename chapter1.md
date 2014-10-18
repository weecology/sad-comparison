#Chapter 1

# Introduction
Very important first sentence.
###Proliferation of SAD models, no agreement about winners. (citations galore)
A fundamental and ubiquitous ecological pattern is the presence of many rare species and few super abundant species within a community, forming a hollow curve distribution.  Because of the generality of this pattern, the species abundance distribution (SAD) has been one of the most widely studied patterns in ecology, leading to a proliferation of models that attempt to characterize the shape of the distribution and identify potential mechanisms for the pattern. The most recent comprehensive review and classification of species abundance distributions was given by McGill et al. 2007.




###Statistical descriptions of SAD distributions, vs. process based.
### Set up process and non process based model overlap (same form)  
There are two classes of species abundance distribution models, process based models, and non-process based models.  Constraints in a process based model of species abundance distributions (SADs) provide a predicted form of a distribution, based on an assumption that the constraints that produce the form of the distribution are biologically meaningful(relevant?).  However, non-process based species abundance distribution models are purely statistical descriptions of the shape of the distribution, and do not infer any biological meaning to the constraints of the distribution.  While the goal of a process based model is to identify pattern generating mechanisms, process based models can share the same forms as other process based or non-process based species abundance distribution models.  Because of the overlap between/among models, it can be difficult to identify potential mechanisms with any degree of certainty (if two models have an identical form, it is impossible to say which model is 'correct'). The difficulty involved in distinguishing between/among models makes it challenging, if not impossible to identify a clear winner among the species abundance distribution models (citations). 

###No difference between models?  Maybe, but...
While different species abundance distribution models can share a single form of a distribution, many models have different but highly similar forms of the species abundance distribution.  Because many forms of the species abundance distribution are highly similar, some have suggested that there is effectively no difference between models (i.e., that the differences between/among models are so small that the models are functionally equivalent)(citations).  However, there has been little work done to rigorously test this assertion.   


###No comprehensive comparision across models using the most rigorous statistical approaches, large datasets (plus across taxonomic groups).
While there have been some studies that compete species abundance distribution models against one another (citations including the Ulrich one), there has not yet been a comprehensive comparison across models using the most rigorous statistical approaches, large datasets, or across multiple taxonomic groups.  


# Methods
###Data, (from White et al 2012, minus the broken Gentry site 102 or something like that).
I used the following datasets analyzed by White et al. 2012 to test the performance of five species abundance distribution models.  

####BBS
The North American Breeding Bird Survey (BBS) is a publicly available dataset, collected by volunteers, and was downloaded with the EcoData Retriever (BBS; Sauer et al. 2011) (EcoData Retriever, Morris and White 2013). Number of sites.
####CBC
The Christmas Bird Count (CBC) is conducted by volunteers and is available by obtaining a memorandum of understanding. (CBC; National Audubon Society 2002). Number of sites.
####Gentry
The Alwyn Gentry’s Forest Transect dataset (Gentry) was downloaded with the EcoData Retriever  (Gentry; Phillips and Miller 2002)(EcoData Retriever, Morris and White 2013). Number of sites.
####FIA
The Forest Inventory Analysis (FIA) was downloaded with the EcoData Retriever  (FIA; USDA Forest Service 2010)(EcoData Retriever, Morris and White 2013). Number of sites.
####MCDB
The Mammal Community Database (MCDB), publicly available at Ecological Archives, was downloaded with the EcoData Retriever (MCDB, Thibault et al. 2011)(EcoData Retriever, Morris and White 2013)). Number of sites.
####NABA    
The North American Butterfly Count data (NABA) is conducted by volunteers and is available by obtaining a memorandum of understanding.  (NABA; North American Butterfly Association 2009). Number of sites.

Gentry sites 102 and 179 were culled from the dataset due to a previously unidentified flaw in that site (one species had a decimal rather than integer abundance).  In total, I used data for 15,846 communities across four taxonomic groups over six large datasets.  The data have a North American bias, as the BBS, CBC, and FIA data are restricted to North America.

THIS HAS PROBABLY CHANGED, CHECK
A small percentage of sites (number of sites) in the FIA dataset blew up on the negative binomial and the Poisson lognormal and one site in the MCDB blew up on the Poisson lognormal (Appendix?).  

For sites where a model or models failed, AICc weights were calculated for only those models which successfully fit the data and blanks were inserted into the list of AICc weights post calculation.  All other model/data combinations ran successfully. 

###Likelihood based statistical comparison (White et al 2008, Edwards et al 2007, 2008)
I used a maximum likelihood approach to model fitting because it is the most robust approach for this type of model comparison, and the log-likelihood also provides a measure of goodness of fit (citations Hummingbird book).  If a model did not have a likelihood method for fitting the model to empirical data, it was excluded to keep the results comparable across models. 
Used AICc (citations).
I used corrected Aikaike Information Criterion (AICc) weights to identify the model with the best performance relative to the number of model parameters for a given dataset (citation).  AICc weights were used because more robust, provides a penalty for more parameters (citation).  Also, seemingly magic.

Possibly something about number of parameters for each model?

The model with the greatest AICc weight was determined to be the winning model for that site.
Used relative likelihood (citations)
Species richness varies greatly across the datasets, and the value of log-likelihoods (a measure of goodness of fit of model to data) are highly dependant on the starting species richness, making it difficult to compare goodness of fit across datasets.  To better visualize model fit across datasets, I also calculated relative likelihoods with AICc weights by setting the number of parameters in each model to one, effectively normalizing the results (definitely need a citation here).   
Packages used to do analysis.
Model fitting, log-likelihood, and relative likelihood calculations were performed with the macroeco_distributions module in the macroecotools package, while AICcs and AICc weights were calculated with the macroecotools package (Macroecotools, <https://github.com/weecology/macroecotools.git>).

I followed the recommendations for strong inference in comparing species abundance distribution models provided by McGill et al. 2007.


###Model selection (justification of why we chose those, justification for neutral theory, Neutral theory predicts the negative binomial distribution (Connolly et al. 2014.)
List of models used, packages used to implement code

McGill et al. (2007) classified models into five different families: purely statistical, branching process, population dynamics, niche partitioning, and spatial distribution of individuals .  I attempted to test models from each of the separate families, excluding the spatial distribution family (McGill et al. 2007) which requires spatially explicit data.  I had initially tried to test the generalized Yule model (branching process family), but this model proved difficult to fit to empirical data and failed to converge to a solution for many of the communities, so it was excluded from the final analyses.

This might be a place to talk about the Ulrich paper, because it seems like their power-law choice was in the branching process family, or at least it cites the same Nee 2003 paper that the McGill et al. 2007 paper uses.  Thus, connecting the not using the gen Yule to the Ulrich paper might be important here.

Ulrich et al. (2010) tested a power law model like the generalize Yule distribution as one of their species abundance distributions, and found that it fit the data best when the datasets were incomplete.  It also had better performance when the data were binned (Ulrich et al. 2003), suggesting that this form of the species abundance distribution is not a "true form" of the distribution (i.e., reveals that the data are incomplete/undersampled). Transition sentence.

Because abundance is discrete, rather than continuous, discrete approximations of species abundance distributions are more appropriate choices for model selection than continuous versions of the distribution, so all models used were discrete forms of the distributions (Ethan's paper).

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
The untruncated logseries had the best model fit in the majority of cases, for all datasets combined (Figure 1).  However, the pattern varied for each dataset individually.  For the BBS, CBC, FIA, MCDB, and NABA data, the untruncated logseries provided the best fit, while the Poisson lognormal provided the best model fit for the Gentry data, with the untruncated logseries coming in a close second (Figure 2).  The truncated lognormal performed the worst for the combined datasets (Figure 1) (zero sites, not graphed), and was never the best fit for the BBS, CBC, Gentry, and NABA datasets (Figure 2)(zero sites, not graphed).  The negative binomial distribution failed to fit *word choice here* a small number of sites (get actual numbers).

The actual distribution of AICc weights varied with each model.  The peaks of the AICc weights tended to overlap for the truncated logseries, negative binomial, and Poisson lognormal (Figure 3), although the Poisson lognormal had an additional smaller peak around 1, indicating that it had very good model fit in the cases where it was the winning model (Figure 3).  The majority of the AICc weights for the geometric series were near zero (Figure 3).


Although the truncated logseries and untruncated logseries do not have much overlap for AICc weights (Figure 3), and the truncated logseries was never the winning model (Figures 1, 2), the log-likelihood values have almost complete congruence (Figure 4).  This indicates that both the truncated and untruncated logseries fit equally well to the data, but that the truncated logseries recieves a heavy penalty in AICc weighting due to the extra truncation parameter. All of the models but the geometric series have very similar log-likelihood values, indicating very similar goodnesses of fit of models to data.  



Assorted colorful graphs (check Post-It notes).
Additional graphs showing the AICc weights and the log-likelihood weights separately are in Appendix whatever.

# Discussion
Intro paragraph outlining points before jumping into them. 

####Different processes can generate identical models. (expansion of point from introduction)
Identifying pattern generating mechanisms of the species abundance distribution is functionally impossible for several reasons.  Different process-based species abundance distribution models can generate identical forms of the species abundance distribution.  For example, the negative binomial distribution, a purely statistical model of species abundance distributions, is also the predicted result of neutral theory at the local scale (Conolly paper).  To further confuse the issue, different biological explanations have been proposed for the same non-process based models, and the same biological explanations have been proposed for different forms of the species abundance distribution.  For example, Hughes (1986) suggested that a model of community dynamics could produce both the logseries or the lognormal, depending on community conditions. 

Actually, this might be a place to have that potential table with the form of the distribution on the left and a list of the mechanistic models that produce the shape of that distribution or proposed mechanisms on the right.

Ugland & Gray 1982, Hummingbird book (a couple years ago, 2011-ish?)


Logseries:niche preemption with random recruitment(May 1975) more dispersal/immigration (Hughes 1986) community dynamics (Hughes 1986)
Lognormal:hierarchical niche apportionment (Sugihara 1980) more independant, lower dispersal, larger communities (Hughes 1986) community dynamics (Hughes 1986)
Negative binomial:neutral (Connolly et al. 2014)
Geometric:niche preemption with regular recruitment(May 1975)


####Statistical difference vs. biological relevance (i.e., is there enough difference that we can distinguish between possible mechanisms)
Something about AICc weights and the number of parameters vs. the likelihoods and model fit and what that all means.  Make the point that even if one model does win, the actual difference between/among the models might not be enough to conclusively state that the processes suggested by that particular model are the dominant processes operating in the system.  

Something acknowledging model failure for certain datasets, which I suspect is due to a low species richness and abundance.  Both the negative binomial and the Poisson lognormal distributions failed to provide an accurate fit to empirical data for n number of datasets. In cases where total community abundance is low and species richness is low, those models are not a good choice.  Also maybe Ken's feasible sets?  

####Paragraph on the Ulrich et al. 2010 paper. (limitations of their approach)
Ulrich et al. (2010) tested three types of species abundance distribution models in their analysis, and attempted to identify if there were patterns in the winning model according to several environmental variables, as well as the type of plot used to model the data.  As suggested by McGill et al (2007), modern computing power means that species abundance data no longer requiring binning to calculate (resulting in a loss of thingy, it's a statistical word).  Formal testing of binning data for species abundance distributions by Ulrich et al. (2010) concluded that binning performed worse in all cases. Several limitations of the approach by Ulrich et al (2010) were the different methods used to determine goodness of fit of the data to the model, and the decision not to assess statistical significance of a particular model.  My approach used a single method (AICc) to determine which model provides the best fit.  I also used a likelihood approach for fitting the data.  

####Next steps: identify if there are explanatory patterns in winning model by taxonomic group or by space. Or by species richness/abundance?

####Wrap up
Big picture conclusions:

While the logseries fit best for the majority of the dataset, the Poisson lognormal also performed well.  However, the actual degree of difference among models was not that great, suggesting that the fit of any  given species abundance distribution model is not an good test of that model.  Instead, I suggest that the McGill (I think the 2003, but others as well) recommendations for strong inference in macroecology( testing process-based model performance with multiple patterns at the same time) is the only appropriate approach for identifying macroecological mechanisms.  However, lack of ability to identify mechanisms that produce a pattern does not mean that a pattern is not useful for prediction, which is one of the goals to move macroecology forward as a discipline (citation, this is weak, and needs a rewrite, but the general idea is there).  


Cannot use species abundance distributions by themselves to identify mechanism- need to use multiple patterns (bunch of citations, McGill, Xiao, etc.)  Inability to identify mechanism doesn't mean that patterns can't be useful for prediction- but purely statistical forms of the distribution should probably be used, because mechanism can't be identified anyway.


#### Bit that really needs some work, but is about mechanism not neccessarily important to make predictions, which is a good point, although I think mechanism is more interesting.
Identifying which forms of the species abundance distribution most closely follow the empirical form of the distribution can provide something or other insights into making or refine ability to prediction or something like that.  Anyway, the models are so close together in a lot of cases that it doesn't actually matter, so long as you don't pick the geometric, which just tends to be bad.  Also, picking a distribution that models the thing that you are looking for is good.  If you are interested, for example in modelling the abundance of rare species at a site, you might pick a species abundance distribution model that fits less well overall, but fits better at the rare species end. 

# References
Connolly et al. 2014. Commonness and rarity in the marine biosphere. PNAS 111: 8524-8529.
McGill, B.J. et al. 2007. Species abundance distributions: moving beyond single prediction theories to integration within an ecological framework. Ecology Letters 10 995-1015.
Morris, B.D. and E.P. White. 2013. The EcoData Retriever: Improving Access to Existing Ecological Data. PLoS ONE 8: 65848. doi:10.1371/journal.pone.0065848.  
Sugihara, F. 1980. Minimal community structure: An explanation of species abundance patterns. The American Naturalist 116: 770-787. 
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
national core field guide (Phase 2 and 3). Version 4.0. USDA Forest Service, Forest Inventory and Analysis, Washington,
D.C., USA.

###Code
sad-comparison, <https://github.com/weecology/sad-comparison.git>  
METE, <https://github.com/weecology/METE.git>  
Macroecotools, <https://github.com/weecology/macroecotools.git>





