#Chapter 1 - An extensive comparison of species-abundance distribution models

# Introduction

The species abundance distribution describes the full distribution of commonness and rarity in ecological systems. It is one of the most fundamental and ubiquitous patterns in ecology, and exhibits a consistent general form with many rare species and few abundant species occurring within a community. This general shape is often referred to as a hollow curve distribution.

The species abundance distribution (SAD) has been one of the most widely studied patterns in ecology, leading to a proliferation of models that attempt to characterize the shape of the distribution and identify potential mechanisms for the pattern (see [McGill2007species] for a recent review of SADs). These models range from arbitrary distributions that are chosen based on providing a good fit to the data (Fisher 1943), to process based ecological models [@Hubbell2001; @Volkovetal2003], to models based on combinatorics and the most likely state of the distribution [@Harte2011; @LoceyWhite2013; @Frank 2014].

Which model or models provide the best fit to the data, and the implications for the processes structuring ecological systems, has been a regular topic of debate (e.g., [@McGill2003; @Volkovetal2004; @Ulrich2010meta; @White2012maxent]). Most comparisons of the different models: 1) focus on a small subset of available models (typically two; e.g., [@McGill2003; @Volkovetal2004; @White2012maxent]); 2) use a single dataset (e.g., [@McGill2003; @Volkovetal2004]); or 3) fail to use the most appropriate modern statistical methods (e.g., [@Ulrich2010meta]). This makes it difficult to draw general conclusions about which, if any, models provide the best empirical fit to species abundance distributions.

Here, we evaluate the performance of five of the most widely used models for the species abundance distribution. We evaluate their performance using likelihood based model selection on data from 15,846 communities, from four taxonomic groups, representing nearly 50 million individual organisms.

<!---
Moved more extensive discussed on constraint vs. process based models to Discussion
-->

<!--
I'm not sure whether or not the follow section belongs in the Intro. If it does I'm not sure where to put it at the moment
-->

###No difference between models?  Maybe, but...

While different species abundance distribution models can share a single form of a distribution, many models have different but highly similar forms of the species abundance distribution.  Because many forms of the species abundance distribution are highly similar, some have suggested that there is effectively no difference between models (i.e., that the differences between/among models are so small that the models are functionally equivalent)(citations).  However, there has been little work done to rigorously test this assertion.   



# Methods

### Data
<!--
Change number of communities, number of individuals once that has settled.
-->
I used data on 15,846 communities, from nine taxonomic groups, representing nearly 50 million individual terrestrial, aquatic, and marine organisms, to test the performance of five species abundance distribution models. This data was compiled from a variety of sources.  Data for the trees, birds, butterflies and mammals was compiled by White et al. 2012 from six data sources: the US Forest Service Forest Inventory and Analysis (FIA; USDA Forest Service 2010), the North American Breeding Bird Survey (BBS; Sauer et al. 2011), the North American Butterfly Associations North American Butterfly Count (NABC; NABA 2009), the Mammal Community Database (MCDB; Thibault et al. 2011), Alwyn Gentry's Forest Transect Data Set (Gentry; Phillips and Miller 2002), and the US Geological Survey's North American Breeding Bird Survey (BBS; Sauer et al. 2011). Gentry sites 102 and 179 were culled from the dataset due to a previously unidentified flaw in those sites.  Additional data was compiled by Baldridge 2012 (fish, reptiles, beetles, spiders, amphibians; MiscDB, Baldridge 2012) and accessed through the EcoData Retriever [@Morris2013ecodata].

<!--
How about a table for the sections below?
-->
Table : Information on data sets used.  All publicly available datasets were accessed through the EcoData Retriever (Morris and White 2013).  
| Dataset                              	| Dataset code 	| Availability                                     	| Total sites 	| Citation                                         	|
|--------------------------------------	|--------------	|--------------------------------------------------	|-------------	|--------------------------------------------------	|
| North American  Breeding Bird Survey 	| BBS          	| Publicly available                               	|2769             	| BBS; Sauer et al. 2011.                          	|
| Christmas Bird Count                 	| CBC          	| Data request;  Memorandum of  Understanding      	|1999             	| CBC; National Audubon Society 2002.              	|
| Alwyn Gentry's Forest Transects      	| Gentry       	| Publicly available                               	|10355             	| Gentry; Phillips and Miller 2002.                	|
| Forest Inventory Analysis            	| FIA          	| Publicly available                               	|220             	| FIA; USDA Forest Service 2010.                   	|
| Mammal Community Database            	| MCDB         	| Publicly available                               	|103             	| MCDB; Thibault et al. 2011.                      	|
| North American Butterfly Count       	| NABA         	| Data request with  Memorandum of  Understanding  	|400             	| NABA; North American Butterfly Association 2009. 	|
| Actinopterygii; Miscellaneous abundance database      	| fish         	| Publicly available  	|##             	| MiscDB; Baldridge 2012. 	|
| Reptilia; Miscellaneous abundance database      	| reptiles         	| Publicly available  	|##             	| MiscDB; Baldridge 2012. 	|
| Amphibia; Miscellaneous abundance database      	| amphibia         	| Publicly available  	|##             	| MiscDB; Baldridge 2012. 	|
| Coleoptera; Miscellaneous abundance database      	| beetles        	| Publicly available  	|##             	| MiscDB; Baldridge 2012. 	|
| Arachnida; Miscellaneous abundance database      	| spiders         	| Publicly available  	|##             	| MiscDB; Baldridge 2012. 	|

 

For sites where a model or models failed, AICc weights were calculated for only those models which successfully fit the data. All other model/data combinations ran successfully. 

### Models

When species-abundance distributions (SADs) are constructed using counts of individuals (the most common, but not the only approach; see [@McGill2007species and @Morlonetal2009]), the data are discrete (i.e., you cannot have 1.5 individuals) and therefore the most appropriate models are discrete distributions. Therefore, we used only discrete forms of the distributions that have been applied to SADs.

[@McGill2007species] classified models into five different families: purely statistical, branching process, population dynamics, niche partitioning, and spatial distribution of individuals. I attempted to test models from each of the separate families, excluding the spatial distribution family [@McGill2007species] which requires spatially explicit data.  I had initially tried to test the generalized Yule model (branching process family), but this model proved difficult to fit to empirical data and failed to converge to a solution for many of the communities, so it was excluded from the final analyses.

<!--
This might be a place to talk about the Ulrich paper, because it seems like their power-law choice was in the branching process family, or at least it cites the same Nee 2003 paper that the McGill et al. 2007 paper uses.  Thus, connecting the not using the gen Yule to the Ulrich paper might be important here.
-->

[@Ulrich2010meta] tested a power law model like the generalized Yule distribution as one of their species abundance distributions, and found that it fit the data best when the datasets were incomplete. Another transitional sentence to explain this better. It also had better performance when the data were binned [@Ulrichetal2003], suggesting that this form of the species abundance distribution is not a "true form" of the speciea abundance distribution (i.e., reveals that the data are incomplete/undersampled). <!--Transition sentence.-->

I tested the following distributions with the following packages: 

Table 1: Provides the species abundance distribution models used with links to the code implementation and model classification following McGill et al. 2007.  Additional classifications of models are also provided where appropriate.

| Species abundance distribution model     	| Code implementation                            	| Model classification  (McGill et al. 2007) 	| Additional model classifications                    	|
|------------------------------------------	|------------------------------------------------	|--------------------------------------------	|-----------------------------------------------------	|
| Maximum Entropy Theory of Ecology (METE) 	| https://github.com/weecology/METE.git          	|                                            	| Information-theoretic                               	|
| Untruncated logseries                    	| https://github.com/weecology/macroecotools.git 	| Purely statistical                         	|                                                     	|
| Poisson lognormal                        	| https://github.com/weecology/macroecotools.git 	| Purely statistical                         	|                                                     	|
| Negative binomial                        	| https://github.com/weecology/macroecotools.git 	| Purely statistical                         	| Neutral theory approximation (Connolly et al. 2014) 	|
| Geometric series                         	| https://github.com/weecology/macroecotools.git 	| Niche partitioning                         	|                                                     	|
| Zipf distribution (Zipf-Mandelbrot)      	| https://github.com/weecology/macroecotools.git                                    	| Branching process                          	| Power-law (Ulrich et al. 2010)                      	|

### Analysis

I used a maximum likelihood to fit models to the data and likelihood based model selection to compare the fits of the different models. I did not include models lacking likelihoods in the analysis.

I used corrected Aikaike Information Criterion (AIC) weights were used to compare the fits of models while correcting for differences in the number of parameters [@BurnhamAnderson2002]. Most of the models analyzed included two fitted parameters, with the exception of the log-series which has one parameter. I used AICc in these weights to address the small sample sizes (i.e., numbers of species) in some communities [@BurnhamAnderson2002]. The model with the greatest AICc weight was determined to be the best model for that site and distributions of weights were compared to determine which models performed best across all datasets.

I also examined the log-likelihood values to compare the fit of model to data without taking into account the number of parameters used to fit the model. Since species richness varies greatly across the datasets, and the value of log-likelihoods are highly dependent on the number of data points, I calculated relative likelihoods with the AICc weights package in macroecotools (macroecotools, <https://github.com/weecology/macroecotools.git>) by setting the number of parameters in each model to one, effectively normalizing the results <!--(definitely need a citation here)-->.

<!-- We should actually do a proper relatively likelihood comparison with it's own function when we get the chance. It won't change the result, but it will avoid this awkward step in the righting and make it easier for others understand what we've done. -->

Model fitting, log-likelihood, relative likelihood, and AIC  calculations were using the macroecotools Python package (https://github.com/weecology/macroecotools). Code necessary and the majority of the data necessary to replicate these analyses is available at (https://github.com/weecology/sad-comparison). The CBC datasets and NABA datasets are not publicly available and are not included.


# Results
<!--
Needs total rewrite with new results
-->
<!--
Add inline figures.
-->
  While the logseries was the consistent winner for all datasets combined, the geometric series also performed quite well, and was a fairly close second in the number of wins (Figure 1).  The Poisson lognormal and negative binomial distributions had very similar numbers of wins, and the Zipf distribution had slightly less (Figure 1).

![Figure 1](./sad-data/chapter1/total_wins.png "Figure 1. Total wins by model for all datasets combined.")
Figure 1. Total wins by model for all datasets combined.

The logseries had the best model fit in the majority of cases (Figure 2). It provided the best fit for all datasets except FIA, where it was outperformed by the geometric series(Figure 2.) Although the logseries was the overall winner for the combined datasets, there was no consistent pattern in model wins when the datasets were examined separately (Figure 2).  The negative binomial never won for the Coleoptera and Arachnida datasets, and the Poisson lognormal never won for the Coleoptera dataset; however, these datasets had the fewest number of sites (Figure 2).

![Figure 2](./sad-data/chapter1/wins_by_dataset.png "Figure 2. Total wins by model for each dataset individually.")
Figure 2. Total wins by model for each dataset individually.

The AICc weights show some separation among models after correcting for the number of model parameters (Figure 3).  The main peak of the weight distribution for the Zipf and geometric distributions tends to fall slightly above 0.0 (Figure 3).  The negative binomial and the Poisson lognormal distributions have peaks slightly higher, around .1, while the Poisson lognormal has another small peak close to 1.0 (Figure 3).  The logseries has a gentle peak from approximately 0.3-0.5, and another from 0.6-0.7 (Figure 3.)  The geometric series has a peak that is fairly consistent to .4, where it shows a slight increase to .5 and falls off sharply at .6 (Figure 3). 

 AICc weights
 ![Figure 3](./sad-data/chapter1/AICc_weights.png "Figure 3. AICc weights by model for all datasets combined.")
 Figure 3. AICc weights by model for all datasets combined.
 
 While the AICc weights show some separation among models after correction for the number of parameters (Figure 3), the log-likelihoods show almost complete overlap among models (Figure 4), indicating that all models fit the data equivalently <!-- not the right word -->well relative to one another.
 ![Figure 4](./sad-data/chapter1/likelihoods.png "Figure 4. Log-likelihoods by model for all datasets combined.")
 Figure 4. Log-likelihoods by model for all datasets combined.
 
 <!-- Do we want to add in the 'relative likelihood' graphs, or wait until we do a proper goodness of fit test? -->
 
# Discussion
<!---
TODO:

Add some discussion of the fact that since log-series yields equivalent likelihoods, has the fewest parameters, and is trivial to fit, it is probably the best naive model for the SAD

"goodness of fit" is used a lot, but traditionally this is used to describe whether the model fits the data. All we've done so far is see who well the different models fit the data relative to one another. Adding some tests of actually goodness of fit would probably be a worthwhile addition, either based on binning or comparing R^2 with the real data to simulated distributions like Xiao did in her in press AmNat paper. Regardless, we shouldn't use "goodness of fit" to refer to this particular set of analyses.

I think some discussion of Locey & White, Frank 2014, and other constraint based approaches as possible explanations for why so many models yield similar results would be a useful way to wrap things up.
-->

Our extensive comparison of different models for the species-abundance distribution using rigorous statistical methods demonstrates that most existing models provide equivalently good fits to empirical data. Since all models perform well, the models with the fewest parameters perform better in AIC-based model selection, since these approaches penalize model complexity.  Since the logseries provides equivalent likelihoods to the other species distribution models, has a single fitted parameter, and is trivial to fit to empirical data, it is probably the best naive model for fitting species abundance distributions. 

 
I addressed two unresolved questions about (something goes here) species abundance distributions by comparing five species abundance distribution models.  One problem with the analysis of species abundance distributions is the difficulty of identifying pattern generating mechanisms for species abundance distribution models.  Another problem with species abundance distribution models is determining whether statistical difference between/among models translates into biological relevance.  These questions have been challenging to address throughly; although researchers have compared species abundance distribution models in the past, previous studies have not analyzed as many species abundance distribution models, or with as many different taxonomic groups or number of communities.   

####Different processes can generate identical models. (expansion of point from introduction)

Identifying pattern generating mechanisms of the species abundance distribution is functionally impossible for several reasons.  The three reasons why pattern generating mechanisms are not identifiable are identical distribution forms for different models, multiple mechanistic models for the same distribution, and single mechanisms that can generate multiple forms of the species abundance distribution.  Different process-based species abundance distribution models can generate identical forms of the species abundance distribution.  For example, the negative binomial distribution, a purely statistical model of species abundance distributions, is also the predicted result of neutral theory at the local scale [@Conolly2014commonness].  To further confuse the issue, different biological explanations have been proposed for the same non-process based models, and the same biological explanations have been proposed for different forms of the species abundance distribution.  For example, [@Hughes1986] suggested that a model of community dynamics could produce both the logseries or the lognormal, depending on community conditions.  There might also be so little difference among model goodness of fits that any differerences among models might be irrelevant, making it even more unlikely that any biological mechanisms could be conclusively identified. 

Actually, this might be a place to have that potential table with the form of the distribution on the left and a list of the mechanistic models that produce the shape of that distribution or proposed mechanisms on the right.

Ugland & Gray 1982, Hummingbird book (a couple years ago, 2011-ish?)

Logseries:niche preemption with random recruitment(May 1975) more dispersal/immigration (Hughes 1986) community dynamics (Hughes 1986), neutral at metacommunity scale
Lognormal:hierarchical niche apportionment (Sugihara 1980) more independant, lower dispersal, larger communities (Hughes 1986) community dynamics (Hughes 1986)
Negative binomial:neutral (Connolly et al. 2014)
Geometric:niche preemption with regular recruitment(May 1975)


####Statistical difference vs. biological relevance (i.e., is there enough difference that we can distinguish between possible mechanisms)

Something about AICc weights and the number of parameters vs. the likelihoods and model fit and what that all means.  Make the point that even if one model does win, the actual difference between/among the models might not be enough to conclusively state that the processes suggested by that particular model are the dominant processes operating in the system.
A winning model can be identified by determining which model has the best fit to the data given a certain set of conditions.  However, there might not be much difference between/among model fits.  I used AICc weights in my analysis to determine the winning model, but examining log-likelihoods and relative likelihoods allowed me to determine that there was functionally no difference in goodness of fit for the majority of models, although I was able to identify the model which fit the most poorly.  Even if one model does win by having the largest AICc weight, the actual difference between/among the models as measured by the goodness of fit (likelihood) might not be enough to conclusively state that the processes suggested by that particular model are the dominant processes operating in the system as the majority of models provided equivalent fits to the data.

Something acknowledging model failure for certain datasets, which I suspect is due to a low species richness and abundance.  Both the negative binomial and the Poisson lognormal distributions failed to provide an accurate fit to empirical data for n number of datasets. In cases where total community abundance is low and species richness is low, those models are not a good choice.  Also maybe Ken's feasible sets?  

####Paragraph on the Ulrich et al. 2010 paper. (limitations of their approach)

[@Ulrich2010meta] tested three types of species abundance distribution models in their analysis, and attempted to identify if there were patterns in the winning model according to several environmental variables, as well as the type of plot used to model the data.  As suggested by [@McGill2007species], modern computing power means that species abundance data no longer requiring binning to calculate (resulting in a loss of thingy, it's a statistical word).  Formal testing of binning data for species abundance distributions by [@Ulrich2010meta] concluded that binning performed worse in all cases. Several limitations of the approach by [@Ulrich2010meta] were the multiple methods applied to determine goodness of fit of the data to the model, and the decision not to assess statistical significance of a particular model. <!-- We haven't assessed the significance of particular models either -->  My approach used a single method (AICc) to determine which model provides the best fit.  I also used a likelihood approach for fitting the data and assessing goodness of fit of the model to the data.  This approach allowed for robust comparison among models/datasets


####Next steps: identify if there are explanatory patterns in winning model by taxonomic group or by space. Or by species richness/abundance?

####Wrap up

#### Bit that really needs some work, but is about mechanism not neccessarily important to make predictions, which is a good point, although I think mechanism is more interesting.

Identifying which forms of the species abundance distribution most closely follow the empirical form of the distribution can provide something or other insights into making or refine ability to prediction or something like that.  Anyway, the models are so close together in a lot of cases that it doesn't matter, so long as you don't pick the geometric, which just tends to be bad.  Also, picking a distribution that models the thing that you are looking for is good.  If you are interested, for example in modelling the abundance of rare species at a site, you might pick a species abundance distribution model that fits less well overall, but fits better at the rare species end.

####Big picture conclusions:

While the logseries fit best for the majority of the dataset, the Poisson lognormal also performed well.  However, the actual degree of difference among models was not that great, suggesting that the fit of any  given species abundance distribution model is not an good test of that model.  Instead, I suggest that the McGill (I think the 2003, but others as well) recommendations for strong inference in macroecology( testing process-based model performance with multiple patterns at the same time) is the only appropriate approach for identifying macroecological mechanisms.  However, lack of ability to identify mechanisms that produce a pattern does not mean that a pattern is not useful for prediction, which is one of the goals to move macroecology forward as a discipline (citation, this is weak, and needs a rewrite, but the general idea is there).  

Species abundance distributions can be useful in determining pattern generating mechanisms, but they cannot be used by themselves to identify mechanism.  To attempt to identify mechanism, it is important to compare the predictions of process-based models across multiple macroecological patterns (bunch of citations, McGill, Xiao, etc.)  An inability to identify biological mechanisms for the species abundance distribution does not mean that the species abundance distribution is not useful for prediction.  However, purely statistical forms of the distribution are more appropriate if using the species abundance distribution for predictions, because purely statistical forms of the distribution tend to have fewer parameters and mechanism cannot be identified anyway. 


<!--
The following section has been moved down from the Intro. Not sure exactly where it belongs yet
-->

###Statistical descriptions of SAD distributions, vs. process based.

### Set up process and non process based model overlap (same form)  

There are two classes of species abundance distribution models, process based models, and non-process based models.  Constraints in a process based model of species abundance distributions (SADs) provide a predicted form of a distribution based on the assumption that the constraints that produce the form of the distribution are biologically meaningful(relevant?).  However, non-process based species abundance distribution models are purely statistical descriptions of the shape of the distribution, and do not infer any biological meaning to the constraints of the distribution, although post hoc biological explanations are frequently applied to statistical descriptions (every paper ever written).  Process based models can share the same forms as other process based or non-process based species abundance distribution models.  Because of the overlap between/among models, it can be difficult to identify potential mechanisms with any degree of certainty (if two models have an identical form, it is impossible to say which model is 'correct'). The difficulty involved in distinguishing between/among models makes it challenging, if not impossible to identify a clear winner among the species abundance distribution models (citations).


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
Baldridge, Elita. 2013. Community abundance data. figshare. http://dx.doi.org/10.6084/m9.figshare.79251

###Code

sad-comparison, <https://github.com/weecology/sad-comparison.git>  
METE, <https://github.com/weecology/METE.git>  
Macroecotools, <https://github.com/weecology/macroecotools.git>





