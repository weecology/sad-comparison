#Chapter 1 - An extensive comparison of species-abundance distribution models

# Introduction

The species abundance distribution describes the full distribution of commonness and rarity in ecological systems. It is one of the most fundamental and ubiquitous patterns in ecology, and exhibits a consistent general form with many rare species and few abundant species occurring within a community. This general shape is often referred to as a hollow curve distribution.

The species abundance distribution (SAD) has been one of the most widely studied patterns in ecology, leading to a proliferation of models that attempt to characterize the shape of the distribution and identify potential mechanisms for the pattern (see [@McGill2007species] for a recent review of SADs). These models range from arbitrary distributions that are chosen based on providing a good fit to the data (@fisher1943relation), to distributions chosen based on combinatorics and the most likely state of the distribution, [@Harte2011; @LoceyWhite2013; @Frank 2014], to models based on specific ecological process [@Hubbell2001; @Volkovetal2003]. 

Which model or models provide the best fit to the data, and the resulting implications for the processes structuring ecological systems, has been a regular topic of debate (e.g., [@McGill2003; @Volkovetal2004; @Ulrich2010meta; @White2012maxent]). Most comparisons of the different models: 1) use only a small subset of available models (typically two; e.g., [@McGill2003; @Volkovetal2004; @White2012maxent]); 2) focus on a single ecosystem or taxonomic group (e.g., [@McGill2003; @Volkovetal2004]); or 3) fail to use the most appropriate statistical methods (e.g., [@Ulrich2010meta]). This makes it difficult to draw general conclusions about which, if any, models provide the best empirical fit to species abundance distributions.

Here, we evaluate the performance of five of the most widely used models for the species abundance distribution. We evaluate their performance using likelihood based model selection on data from 16,218 communities, from nine taxonomic groups. This includes data from terrestrial, aquatic, and marine ecosystems representing roughly 50 million individual organisms in total.


# Methods

### Data

We compiled data from on citizen science projects, government surveys, and literature mining to produce a dataset with 16,218 communities, from nine taxonomic groups, representing nearly 50 million individual terrestrial, aquatic, and marine organisms. to test the performance of five species abundance distribution models. Data for the trees, birds, butterflies and mammals was compiled by White et al. 2012 from six data sources: the US Forest Service Forest Inventory and Analysis (FIA; USDA Forest Service 2010), the North American Breeding Bird Survey (BBS; Sauer et al. 2011), the North American Butterfly Associations North American Butterfly Count (NABC; NABA 2009), the Mammal Community Database (MCDB; Thibault et al. 2011), Alwyn Gentry's Forest Transect Data Set (Gentry; Phillips and Miller 2002), and the US Geological Survey's North American Breeding Bird Survey (BBS; Sauer et al. 2011). Details of the treatment of these datasets can be found in Appendix A of White et al. [@white2012]. In addition to the data selection described by White et al, we did not use Gentry sites 102 and 179 because NEED TO DESCRIBE THE SPECIFIC ISSUE THAT PREVENTED US FROM USING THEM. Data on Actinopterygii, Reptilia, Coleoptera, Arachnida, and Amphibia, were mined from literature by Baldridge (MiscDB, Baldridge 2012). All publicly available data were accessed using the EcoData Retriever [@Morris2013ecodata].

Table 1: Details of datasets used to evaluate the form of the species-abundance distribution.

| Dataset                              	| Dataset code 	| Availability                                     	| Total sites 	| Citation                                         	|
|--------------------------------------	|--------------	|--------------------------------------------------	|-------------	|--------------------------------------------------	|
| North American  Breeding Bird Survey 	| BBS          	| Publicly available                               	|2769             	| BBS; Sauer et al. 2011.                          	|
| Christmas Bird Count                 	| CBC          	| Data request;  Memorandum of  Understanding      	|1999             	| CBC; National Audubon Society 2002.              	|
| Alwyn Gentry's Forest Transects      	| Gentry       	| Publicly available                               	|10355             	| Gentry; Phillips and Miller 2002.                	|
| Forest Inventory Analysis            	| FIA          	| Publicly available                               	|220             	| FIA; USDA Forest Service 2010.                   	|
| Mammal Community Database            	| MCDB         	| Publicly available                               	|103             	| MCDB; Thibault et al. 2011.                      	|
| North American Butterfly Count       	| NABA         	| Data request with  Memorandum of  Understanding  	|400             	| NABA; North American Butterfly Association 2009. 	|
| Actinopterygii; Miscellaneous abundance database      	| Actinopterygii 	| Publicly available  	|161             	| MiscDB; Baldridge 2012. 	|
| Reptilia; Miscellaneous abundance database      	| Reptilia         	| Publicly available  	|138            	| MiscDB; Baldridge 2012. 	|
| Amphibia; Miscellaneous abundance database      	| Amphibia 	| Publicly available  	|43             	| MiscDB; Baldridge 2012. 	|
| Coleoptera; Miscellaneous abundance database      	| Coleoptera        	| Publicly available  	|5             	| MiscDB; Baldridge 2012. 	|
| Arachnida; Miscellaneous abundance database      	| Arachnida         	| Publicly available  	|25             	| MiscDB; Baldridge 2012. 	|

All abundances in the compiled datasets where counts of individuals.

### Models

When species-abundance distributions (SADs) are constructed using counts of individuals (the most common, but not the only approach; see [@McGill2007species and @Morlonetal2009]), the data are discrete (i.e., you cannot have 1.5 individuals) and therefore the most appropriate models are discrete distributions. Since our abundance data was based on individual counts, we used only discrete distributions that have been applied to SADs.

[@McGill2007species] classified models into five different families: purely statistical, branching process, population dynamics, niche partitioning, and spatial distribution of individuals. We evaluated models from each of the separate families, excluding the spatial distribution family, which requires spatially explicit data. Specifically, we evaluated the log-series, the Poisson log-normal, the negative binomial, the geometric series, and the Zipf distributions (Table 2).

We excluded models from analysis that do not have explicit likelihoods so that we could use the likelihood based methods for fitting and evaluating distributions (see Analysis).

<!--
We need to add a couple of sentences about each distribution, where it comes from, and why we chose it. We also need citations for each distribution as part of this description. This could possible go in the table instead of in the text, but the information definitely needs to be included somewhere.
-->

<!--
TODO: Add mathematical form of the distributions to the table. This can replace the "Code implementation" column since everything comes from the same place.

I'd also recommend combining the model classification columns and then providing citations for each classification using footnotes. So, many of them, will simply footnote to McGill, but in the case of things like the negative binomial the "Purely statistical" footnote goes to McGill and the Population Dynamics footnote goes to Connolly. 
-->

Table 2: Species abundance distribution models evaluated, their mathematical forms and model classifications.

| Species abundance distribution model     	| Code implementation                            	| Model classification  (McGill et al. 2007) 	| Additional model classifications                    	|
|------------------------------------------	|------------------------------------------------	|--------------------------------------------	|-----------------------------------------------------	|
| Untruncated logseries                    	| https://github.com/weecology/macroecotools.git 	| Purely statistical                         	|                                                     	|
| Poisson lognormal                        	| https://github.com/weecology/macroecotools.git 	| Purely statistical                         	|                                                     	|
| Negative binomial                        	| https://github.com/weecology/macroecotools.git 	| Purely statistical and population dynamics   	| Neutral theory approximation (Connolly et al. 2014) 	|
| Geometric series                         	| https://github.com/weecology/macroecotools.git 	| Niche partitioning                         	|                                                     	|
| Zipf distribution (Zipf-Mandelbrot)      	| https://github.com/weecology/macroecotools.git    | Branching process                          	| Power-law (Ulrich et al. 2010)                      	|

### Analysis

Following current best practices for fitting distributions to data and evaluating their fit, I used maximum likelihood estimation to fit models to the data [@clark1999, @newman2005, @white2008] and likelihood based model selection to compare the fits of the different models [@BurnhamAnderson2002, @edwards2007] These general best practices have recently been affirmed as best practices for species abundance distributions [@MatthewsWhittaker2014]. I did not include models lacking likelihoods in the analysis.

For model comparison we used corrected Aikaike Information Criterion (AICc) weights to compare the fits of models while correcting for differences in the number of parameters and appropriately handling the small sample sizes (i.e., numbers of species) in some communities [@BurnhamAnderson2002]. The Poisson log-normal and the negative binomial each have two fitted parameters, while the log-series, geometric series, and Zipf distributions have one fitted parameter each. The model with the greatest AICc weight in each community was determined to be the best model for that community. We also assessed the full distribution of weights to evaluate how similar the fits of the different models were.

In addition to evaluating AICc of each model, we also examined the log-likelihood values of the models directly. We did this to assess the fit of the model while ignoring corrections for the number of parameters and similarities to other models in the set of candidate models. If two models are very similar in shape this will be definition decrease their AICc weights because they will have very similar AICc's to one other.

<!-- What do you want to do about this?  Should we leave in the weirdness, or take it out?  I feel like this was a weirdness that we did to better visualize the results for ourselves, but it's distracting in the actual paper. -->

<!--
In hindsight I don't think we actually need the relative likelihoods. Our main point is about the likelihoods themselves, we just need to figure out how to display them effectively. I've opened an issue with a possible solution. Feel free to delete these comments if you agree.
-->

Model fitting, log-likelihood, and AICc calculations were performed using the macroecotools Python package (https://github.com/weecology/macroecotools). All of the code and the majority of the data necessary to replicate these analyses is available at (https://github.com/weecology/sad-comparison). The CBC datasets and NABA datasets are not publicly available and therefore we are not allowed to make the raw data publicly available.

For sites where the maximum likelihood estimates for one or more models failed to converge (n=XXXX), AICc weights were calculated for only those models which successfully fit the data. ADD A SENTENCE OR TWO DESCRIBING WHICH DATASETS THESE CONVERGENCE FAILURES OCCURRED IN. All other model/data combinations ran successfully.

# Results

Across all datasets, the log-series was the best fitting distribution most often. The geometric series also performed well, and was a close second in the number of wins (Figure 1). The Poisson lognormal and negative binomial distributions had very similar numbers of wins, and the Zipf distribution had slightly less (Figure 1).

![Total wins by model for all datasets combined.](./sad-data/chapter1/total_wins.png)

Evaluting the best fitting distributions within individual datasets and taxonomic groups, the log-series had the best model in the majority of cases (Figure 2). It was the most frequent best fitting model for all datasets except FIA, where it was outperformed by the geometric series (Figure 2). The relative performance of the other models varied among datasets and taxonomic groups. The negative binomial never won for the Coleoptera and Arachnida datasets, and the Poisson lognormal never won for the Coleoptera dataset; however, these datasets had the fewest number of sites (Figure 2).

<!--
The above paragraph would benefit from another couple of sentences describing patterns in Figure 2.
-->

![Total wins by model for each dataset individually.](./sad-data/chapter1/wins_by_dataset.png)

The full distribution of AICc weights show some separation among models (Figure 3). On average, the Zipf and geometric distributions perform poorly, with the primary mode of the weight distribution occurring near 0 (Figure 3). However, the geometric distribution also exhibits better performance for a subset of communities, with a secondary mode near 0.5. The negative binomial and the Poisson lognormal distributions have peaks around 0.1, with the Poisson lognormal also having a small peak close to 1.0 (Figure 3).  The logseries performs the best overall, with has a gentle peak from approximately 0.3-0.5, and another from 0.6-0.7 (Figure 3).

![AICc weights by model for all datasets combined.](./sad-data/chapter1/AICc_weights.png)
 
While the AICc weights show separation among models, these values include both a  correction for the number of parameters and show model performance relative to other models in the set of candidate models. Therefore we also compared the negative log-likelihoods of the different models to determine whether or not their absolute fits differed. The log-likelihoods show almost complete overlap among models (Figure 4), indicating that all models fit the data equivalently and that differences in AICc weights resulted primarily from differences in the number of parameters and differences in how similar different models in the set of models were.

![Log-likelihoods by model for all datasets combined.](./sad-data/chapter1/likelihoods.png)
 

# Discussion
My extensive comparison of different models for the species-abundance distribution using rigorous statistical methods demonstrates that most existing models provide equivalently good fits to empirical data. Since all models perform well, the models with the fewest parameters perform better in AIC-based model selection, since these approaches penalize model complexity.  Since the logseries provides equivalent likelihoods to the other species distribution models, has a single fitted parameter, and is trivial to fit to empirical data, it is probably the best naive model for fitting species abundance distributions. 

 
I addressed two unresolved questions about <!--(something goes here)--> species abundance distributions by comparing five species abundance distribution models.  One problem with the analysis of species abundance distributions is the difficulty of identifying pattern generating mechanisms for species abundance distribution models.  Another problem with species abundance distribution models is determining whether statistical difference between/among models translates into biological relevance.  These questions have been challenging to address throughly; although researchers have compared species abundance distribution models in the past, previous studies have not analyzed as many species abundance distribution models, or with as many different taxonomic groups or number of communities.   

####Different processes can generate identical models. 
There are two classes of species abundance distribution models, process based models, and non-process based models.  Constraints in a process based model of species abundance distributions (SADs) provide a predicted form of a distribution based on the assumption that the constraints that produce the form of the distribution are biologically meaningful(relevant?).  However, non-process based species abundance distribution models are purely statistical descriptions of the shape of the distribution, and do not infer any biological meaning to the constraints of the distribution, although post hoc biological explanations are sometimes applied to statistical descriptions.  Process based models can share the same forms as other process based or non-process based species abundance distribution models.  Because of the overlap between/among models, it can be difficult to identify potential mechanisms with any degree of certainty (if two models have an identical form, it is impossible to say which model is 'correct'). The difficulty involved in distinguishing between/among models makes it challenging, if not impossible to identify a clear winner among the species abundance distribution models [see @locey2013species; @frank2014generative for possible explanations].

Identifying pattern generating mechanisms of the species abundance distribution is functionally impossible for several reasons.  The three reasons why pattern generating mechanisms are not identifiable are identical distribution forms for different models, multiple mechanistic models for the same distribution, and single mechanisms that can generate multiple forms of the species abundance distribution.  Different process-based species abundance distribution models can generate identical forms of the species abundance distribution.  For example, the negative binomial distribution, a purely statistical model of species abundance distributions, is also the predicted result of neutral theory at the local scale [@Conolly2014commonness].  To further confuse the issue, different biological explanations have been proposed for the same non-process based models, and the same biological explanations have been proposed for different forms of the species abundance distribution.  For example, [@Hughes1986] suggested that a model of community dynamics could produce both the logseries or the lognormal, depending on community conditions.  There might also be so little difference among model goodness of fits that any differerences among models might be irrelevant, making it even more unlikely that any biological mechanisms could be conclusively identified. 

<!--Recommend strong tests for identifying process-->
Species abundance distributions can be useful in determining pattern generating mechanisms, but they cannot be used by themselves to identify mechanism.  To attempt to identify mechanism, it is important to compare the predictions of process-based models across multiple macroecological patterns (bunch of citations, McGill, Xiao, etc.)  An inability to identify biological mechanisms for the species abundance distribution does not mean that the species abundance distribution is not useful for prediction.  However, purely statistical forms of the distribution are more appropriate if using the species abundance distribution for predictions, because purely statistical forms of the distribution tend to have fewer parameters and mechanism cannot be identified anyway. 



####Statistical difference vs. biological relevance (i.e., is there enough difference that we can distinguish between possible mechanisms)
A winning model can be identified by determining which model has the best fit to the data relative to other tested models given a certain set of conditions.  However, there might not be much difference between/among model fits.  I used AICc weights in my analysis to determine the winning model, but examining log-likelihoods allowed me to determine that there was functionally no difference among models in the fit of the model to the data for the majority of models, although I was able to identify the model which fit the most poorly.  Even if one model does win by having the largest AICc weight, the actual difference between/among the models might not be enough to conclusively state that the processes suggested by that particular model are the dominant processes operating in the system as the majority of models provided equivalent fits to the data. Since most models predict the form of the distribution equivalently well, models with fewer parameters might be preferable.

####Similar studies

[@Ulrich2010meta] tested three types of species abundance distribution models in their analysis, and attempted to identify if there were patterns in the winning model according to several environmental variables, as well as the type of plot used to model the data.  As suggested by [@McGill2007species], modern computing power means that species abundance data no longer requiring binning to calculate (resulting in a loss of thingy, it's a statistical word).  Formal testing of binning data for species abundance distributions by [@Ulrich2010meta] concluded that binning performed worse in all cases. Several limitations of the approach by [@Ulrich2010meta] were the multiple methods applied to determine goodness of fit of the data to the model, and the decision to use both continuous and discrete data to test the models.  [@Ulrich2010meta] concluded that completeness of sampling helped to explain differences in winning model.

<!-- How did our results differ from the Ulrich results? -->
[@Ulrich2010meta] found that the lognormal fitted the data best for completely sampled sites and the power law (Zipf distribution) fit the data best for incompletely sampled sites, while I found that the logseries fit the data best overall, and the Poisson lognormal and the Zipf distribution had similar numbers of wins, but were nowhere close to the logseries. 

<!-- Difference in approach --> 
I used a single method (AICc) to determine which model provides the best fit to the data while correcting for the number of free parameters.  I also used a likelihood approach for fitting all models to the data.  This approach allowed for robust comparison among models/datasets.  I also used the raw abundance (count) data from each site to fit the models, while [@Ulrich2010meta] used total abundance (N) and species richness (S) to fit the models.  I also used discrete models that were fit directly from the data, while [@Ulrich2010meta] used a method of fitting continuous distributions for the lognormal and logseries that required the model to be estimated from binned expected abundances. <!-- Xiao, Ethan, or both, if you could check out the manual for the software that Ulrich and Ollik used, and make sure that I'm saying this correctly, that would be super. http://www.keib.umk.pl/wp-content/uploads/2013/04/RADManual.pdf -->

<!-- Completeness of sampling -->
 Besides the difference in method, [@Ulrich2010meta] used data from aquatic invertebrates, while I did not use any data from aquatic invertebrates.  Although the actual taxa were different, a rough estimate of completeness of sampling can be made for some of the datasets.  Due to the nature of forest inventories (Gentry, FIA) where all trees above a certain stem diameter are sampled, tree inventories can be assumed to be highly complete.  However, taxonomic groups that contain many individuals that are only identified to morphospecies (Coleoptera, Arachnida) are likely to be incompletely sampled.  Transect or point surveys, especially for highly vagile groups (BBS, CBC, NABA) can be assumed to be intermediate between the complete censusing of the forest surveys, and the incomplete sampling of the arthropod groups.  However, sampling completeness does not seem to provide an adequate explanation for the results of my study.  


###Conclusions
Although species abundance distribution models have different formulations, most models perform equivalently.  This raises the question of why disparate models have similar performance. [@frank2014generative] points out that general patterns typically have large numbers of models that fit, but that model fit does not neccessarily provide insight into pattern generating mechanisms.
[@locey2013species] demonstrates that the majority of the possible forms for a species abundance distribution produced by combinatorics are clustered in a narrow range, suggesting that all model formulations are likely to fit relatively well.  I observed that log-likelihoods among the models in this study were equivalent, providing further evidence that the majority of species abundance distribution models fit equivalently well, and process cannot be identified by competing models against each other for a single pattern.  Instead, I suggest that the [@McGill 2003] recommendations for strong inference in macroecology (testing process-based model performance with multiple patterns at the same time) are the only appropriate approach for identifying macroecological mechanisms.  However, lack of ability to identify pattern generating mechanisms does not mean that a pattern is not useful for prediction, which is one of the goals to move macroecology forward as a discipline (McGill).  Another approach for identifying macroecological mechanism may be to examine the constraints that models have in common, for example, determining what factors are relevant to determining species richness (S) and abundance (N) at a site.


# References

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





