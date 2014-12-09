#Chapter 1 - An extensive comparison of species-abundance distribution models

# Introduction

The species abundance distribution describes the full distribution of commonness and rarity in ecological systems. It is one of the most fundamental and ubiquitous patterns in ecology, and exhibits a consistent general form with many rare species and few abundant species occurring within a community. This general shape is often referred to as a hollow curve distribution.

The species abundance distribution (SAD) has been one of the most widely studied patterns in ecology, leading to a proliferation of models that attempt to characterize the shape of the distribution and identify potential mechanisms for the pattern (see [@mcgill2007] for a recent review of SADs). These models range from arbitrary distributions that are chosen based on providing a good fit to the data (@fisher1943relation), to distributions chosen based on combinatorics and the most likely state of the system, [@harte2011; @locey2013; @frank2014], to models based on specific ecological process [@hubbell2001; @volkov2003]. 

<!--
Xiao's comment: I don't remember SAD in Frank 2014. Could it be Frank 2010 instead, where SADs are assumed to arise from the so-called "measurement scale"?
-->

Which model or models provide the best fit to the data, and the resulting implications for the processes structuring ecological systems, has been a regular topic of debate (e.g., [@mcgill2003; @volkov2003; @ulrich2010; @white2012]). Most comparisons of the different models: 1) use only a small subset of available models (typically two; e.g., [@mcgill2003; @volkov2003; @white2012]); 2) focus on a single ecosystem or taxonomic group (e.g., [@mcgill2003; @volkov2003]); or 3) fail to use the most appropriate statistical methods (e.g., [@ulrich2010]). This makes it difficult to draw general conclusions about which, if any, models provide the best empirical fit to species abundance distributions.

Here, we evaluate the performance of five of the most widely used models for the species abundance distribution. We evaluate their performance using likelihood based model selection on data from 16,218 communities, from nine taxonomic groups. This includes data from terrestrial, aquatic, and marine ecosystems representing roughly 50 million individual organisms in total.


# Methods

### Data

We compiled data from citizen science projects, government surveys, and literature mining to produce a dataset with 16,218 communities, from nine taxonomic groups, representing nearly 50 million individual terrestrial, aquatic, and marine organisms. to test the performance of five species abundance distribution models. Data for the trees, birds, butterflies and mammals was compiled by White et al. 2012 from six data sources: the US Forest Service Forest Inventory and Analysis (FIA; [@fia]), the North American Butterfly Associations North American Butterfly Count (NABC; @naba), the Mammal Community Database (MCDB; Thibault et al. 2011), Alwyn Gentry's Forest Transect Data Set (Gentry; @phillips2002), the Audubon Society Christmas Bird Count (CBC; @cbc), and the US Geological Survey's North American Breeding Bird Survey (BBS; @pardieck2014). Details of the treatment of these datasets can be found in Appendix A of White et al. [@white2012]. In addition to the data selection described by White et al, we did not use Gentry sites 102 and 179 because NEED TO DESCRIBE THE SPECIFIC ISSUE THAT PREVENTED US FROM USING THEM. Data on Actinopterygii, Reptilia, Coleoptera, Arachnida, and Amphibia, were mined from literature by Baldridge (MiscDB, Baldridge 2012). All publicly available data were accessed using the EcoData Retriever [@morris2013].

Table 1: Details of datasets used to evaluate the form of the species-abundance distribution.

| Dataset                              	| Dataset code 	| Availability                                     	| Total sites 	| Citation                                         	|
|--------------------------------------	|--------------	|--------------------------------------------------	|-------------	|--------------------------------------------------	|
| North American  Breeding Bird Survey 	| BBS          	| Publicly available                               	|2769             	| BBS; Pardieck.                          	|
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

When species-abundance distributions (SADs) are constructed using counts of individuals (the most common, but not the only approach; see [@mcgill2007 and @morlon2009]), the data are discrete (i.e., you cannot have 1.5 individuals) and therefore the most appropriate models are discrete distributions. Since our abundance data was based on individual counts, we used only discrete distributions that have been applied to SADs.

[@mcgill2007] classified models into five different families: purely statistical, branching process, population dynamics, niche partitioning, and spatial distribution of individuals. We evaluated models from each of the separate families, excluding the spatial distribution family, which requires spatially explicit data. Specifically, we evaluated the log-series, the Poisson log-normal, the negative binomial, the geometric series, and the Zipf distributions (Table 2).

We excluded models from analysis that do not have explicit likelihoods so that we could use the likelihood based methods for fitting and evaluating distributions (see Analysis).

<!--
We need to add a couple of sentences about each distribution, where it comes from, and why we chose it. We also need citations for each distribution as part of this description. This could possible go in the table instead of in the text, but the information definitely needs to be included somewhere.
-->

<!--
Xiao's comment: Is it possible to very briefly go over the 20-ish distributions from McGill et al. 2007 and discuss why we chose these five but excluded the others?
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

Following current best practices for fitting distributions to data and evaluating their fit, we used maximum likelihood estimation to fit models to the data [@clark1999, @newman2005, @white2008] and likelihood based model selection to compare the fits of the different models [@BurnhamAnderson2002, @edwards2007] These general best practices have recently been affirmed as best practices for species abundance distributions [@MatthewsWhittaker2014]. We did not include models lacking likelihoods in the analysis.

For model comparison we used corrected Aikaike Information Criterion (AICc) weights to compare the fits of models while correcting for differences in the number of parameters and appropriately handling the small sample sizes (i.e., numbers of species) in some communities [@burnham2002]. The Poisson log-normal and the negative binomial each have two fitted parameters, while the log-series, geometric series, and Zipf distributions have one fitted parameter each. The model with the greatest AICc weight in each community was determined to be the best model for that community. We also assessed the full distribution of weights to evaluate how similar the fits of the different models were.

In addition to evaluating AICc of each model, we also examined the log-likelihood values of the models directly. We did this to assess the fit of the model while ignoring corrections for the number of parameters and similarities to other models in the set of candidate models. If two models are similar in shape, they will have similar log-likelihood values, while their AICc weights will be driven primarily by the number of parameters they have.

<!-- What do you want to do about this?  Should we leave in the weirdness, or take it out?  I feel like this was a weirdness that we did to better visualize the results for ourselves, but it's distracting in the actual paper. -->

<!--
In hindsight I don't think we actually need the relative likelihoods. Our main point is about the likelihoods themselves, we just need to figure out how to display them effectively. I've opened an issue with a possible solution. Feel free to delete these comments if you agree.
-->

Model fitting, log-likelihood, and AICc calculations were performed using the macroecotools Python package (https://github.com/weecology/macroecotools). All of the code and the majority of the data necessary to replicate these analyses is available at (https://github.com/weecology/sad-comparison). The CBC datasets and NABA datasets are not publicly available and therefore we are not allowed to redistribute the raw data.

For sites where the maximum likelihood estimates for one or more models failed to converge (n=XXXX), AICc weights were calculated for only those models which successfully converged. ADD A SENTENCE OR TWO DESCRIBING WHICH DATASETS THESE CONVERGENCE FAILURES OCCURRED IN. All other model/data combinations ran successfully.

# Results

Across all datasets, the log-series was the best fitting distribution most often. The geometric series also performed well, and was a close second in the number of wins (Figure 1). The Poisson lognormal and negative binomial distributions had very similar numbers of wins, and the Zipf distribution had slightly less (Figure 1).

![Total wins by model for all datasets combined.](./sad-data/chapter1/total_wins.png)

Evaluating the best fitting distributions within individual datasets and taxonomic groups, the log-series was the best model in the majority of cases (Figure 2). It was the most frequent best fitting model for all datasets except FIA, where it was outperformed by the geometric series (Figure 2). The relative performance of the other models varied among datasets and taxonomic groups. The negative binomial never won for the Coleoptera and Arachnida datasets, and the Poisson lognormal never won for the Coleoptera dataset; however, these datasets had the fewest number of sites (Figure 2).

<!--
The above paragraph would benefit from another couple of sentences describing patterns in Figure 2.
-->

![Total wins by model for each dataset individually.](./sad-data/chapter1/wins_by_dataset.png)

The full distribution of AICc weights show some separation among models (Figure 3). On average, the Zipf and geometric distributions perform poorly, with the primary mode of the weight distribution occurring near 0 (Figure 3). However, the geometric distribution also exhibits better performance for a subset of communities, with a secondary mode near 0.5. The negative binomial and the Poisson lognormal distributions have peaks around 0.1, with the Poisson lognormal also having a small peak close to 1.0 (Figure 3).  The logseries performs the best overall, with a gentle peak from approximately 0.3-0.5, and another from 0.6-0.7 (Figure 3).

![AICc weights by model for all datasets combined.](./sad-data/chapter1/AICc_weights.png)
 
While the AICc weights show separation among models, these values include a correction for the number of parameters along with relative model performance. Therefore we also compared the negative log-likelihoods of the different models to determine whether or not their absolute fits differed. The log-likelihoods show almost complete overlap among models (Figure 4), indicating that all models fit the data equivalently and that differences in AICc weights resulted primarily from differences in the number of parameters and differences in how similar different models in the set of models were.

![Log-likelihoods by model for all datasets combined.](./sad-data/chapter1/likelihoods.png)
 
<!-- Xiao's comment: I modified the above sentence so that the word "model" doesn't get repeated in one sentence. 

The second half of the last sentence ("and differences in how similar different models in the set of models were") is a bit confusing to me. 
-->

# Discussion
Our extensive comparison of different models for the species-abundance distribution using rigorous statistical methods demonstrates that most existing models provide equivalently good fits to empirical data. Since all models perform well, the models with the fewest parameters perform better in AIC-based model selection since these approaches penalize model complexity.  Since the logseries provides equivalent likelihoods to the other species distribution models, has a single fitted parameter, is easy to fit to empirical data, and is the best overall model using standard model selection, it provides a good naive model for fitting species abundance distributions. 
 
We addressed two unresolved questions about <!--(something goes here)--> species abundance distributions by comparing five species abundance distribution models.  One problem with the analysis of species abundance distributions is the difficulty of identifying pattern generating mechanisms for species abundance distribution models.  Another problem with species abundance distribution models is determining whether statistical difference between/among models translates into biological relevance.  These questions have been challenging to address throughly; although researchers have compared species abundance distribution models in the past, previous studies have not analyzed as many species abundance distribution models, or with as many different taxonomic groups or number of communities.   

#### Implications for understanding processes using SADs
There are two classes of species abundance distribution models, process based models, and non-process based models. However, non-process based species abundance distribution models are purely statistical descriptions of the shape of the distribution, and do not infer any biological meaning to the constraints of the distribution, although post hoc biological explanations are sometimes applied to statistical descriptions.  Process based models can share the same forms as other process based or non-process based species abundance distribution models.  Because of the overlap between/among models, it can be difficult to identify potential mechanisms with any degree of certainty (if two models have an identical form, it is impossible to say which model is 'correct'). The difficulty involved in distinguishing between/among models makes it challenging, if not impossible to identify a clear winner among the species abundance distribution models [see @locey2013; @frank2014 for possible explanations].

Identifying pattern generating mechanisms of the species abundance distribution is functionally impossible for several reasons.  The three reasons why pattern generating mechanisms are not identifiable are identical distribution forms for different models, multiple mechanistic models for the same distribution, and single mechanisms that can generate multiple forms of the species abundance distribution.  Different process-based species abundance distribution models can generate identical forms of the species abundance distribution.  For example, the negative binomial distribution, a purely statistical model of species abundance distributions, is also the predicted result of neutral theory at the local scale [@Conolly2014].  To further confuse the issue, different biological explanations have been proposed for the same non-process based models, and the same biological explanations have been proposed for different forms of the species abundance distribution.  For example, [@hughes1986] suggested that a model of community dynamics could produce both the logseries or the lognormal, depending on community conditions.  There might also be so little difference among model goodness of fits that any differerences among models might be irrelevant, making it even more unlikely that any biological mechanisms could be conclusively identified. 

<!--Recommend strong tests for identifying process-->
Species abundance distributions can be useful in determining pattern generating mechanisms, but they cannot be used by themselves to identify mechanism.  To attempt to identify mechanism, it is important to compare the predictions of process-based models across multiple macroecological patterns (bunch of citations, McGill, Xiao, etc.)  An inability to identify biological mechanisms for the species abundance distribution does not mean that the species abundance distribution is not useful for prediction.  However, purely statistical forms of the distribution are more appropriate if using the species abundance distribution for predictions, because purely statistical forms of the distribution tend to have fewer parameters and mechanism cannot be identified anyway. 

####Statistical difference vs. biological relevance (i.e., is there enough difference that we can distinguish between possible mechanisms)
A winning model can be identified by determining which model has the best fit to the data relative to other tested models given a certain set of conditions.  However, there might not be much difference between/among model fits.  We used AICc weights in our analysis to determine the winning model, but examining log-likelihoods allowed me to determine that there was functionally no difference among models in the fit of the model to the data for the majority of models, although we were able to identify the model which fit the most poorly.  Even if one model does win by having the largest AICc weight, the actual difference between/among the models might not be enough to conclusively state that the processes suggested by that particular model are the dominant processes operating in the system as the majority of models provided equivalent fits to the data. Since most models predict the form of the distribution equivalently well, models with fewer parameters might be preferable.

<!--
The four paragraphs above should be condensed into 1-2 paragraphs that discuss the implications of our results for assessing process from the form of the SAD. This should start with background and citations to early work discussing why this is difficult (including equivalent models) and then emphasize that what we have shown is that even when models are distinguishable, they all basically yield the same likelihoods anyway.

We should mention that this result is in contrast to recent suggestions that specific biology can be directly inferred using SADs see [@macnally2014] and possible mention the recent Enquist lab paper suggesting that processes may be detectable in 2nd order components of these kinds of patterns.
-->

####Similar studies

[@Ulrich2010meta] tested three types of species abundance distribution models in their analysis, and attempted to identify if there were patterns in the winning model according to several environmental variables, as well as the type of plot used to model the data.  As suggested by [@mcgill2007], modern computing power means that species abundance data no longer requiring binning to calculate (resulting in a loss of thingy, it's a statistical word).  Formal testing of binning data for species abundance distributions by [@Ulrich2010meta] concluded that binning performed worse in all cases. Several limitations of the approach by [@Ulrich2010meta] were the multiple methods applied to determine goodness of fit of the data to the model, and the decision to use both continuous and discrete data to test the models.  [@ulrich2010] concluded that completeness of sampling helped to explain differences in winning model.

<!-- How did our results differ from the Ulrich results? -->
[@ulrich2010] found that the lognormal fitted the data best for completely sampled sites and the power law (Zipf distribution) fit the data best for incompletely sampled sites, while we found that the logseries fit the data best overall, and the Poisson lognormal and the Zipf distribution had similar numbers of wins, but were nowhere close to the logseries. 

<!-- Difference in approach --> 
We used a single method (AICc) to determine which model provides the best fit to the data while correcting for the number of free parameters.  We also used a likelihood approach for fitting all models to the data.  This approach allowed for robust comparison among models/datasets.  We also used the raw abundance (count) data from each site to fit the models, while [@Ulrich2010meta] used total abundance (N) and species richness (S) to fit the models.  We also used discrete models that were fit directly from the data, while [@Ulrich2010meta] used a method of fitting continuous distributions for the lognormal and logseries that required the model to be estimated from binned expected abundances. <!-- Xiao, Ethan, or both, if you could check out the manual for the software that Ulrich and Ollik used, and make sure that I'm saying this correctly, that would be super. http://www.keib.umk.pl/wp-content/uploads/2013/04/RADManual.pdf -->

<!-- Completeness of sampling -->
 Besides the difference in method, [@ulrich2010] used data from aquatic invertebrates, while we did not use any data from aquatic invertebrates.  Although the actual taxa were different, a rough estimate of completeness of sampling can be made for some of the datasets.  Due to the nature of forest inventories (Gentry, FIA) where all trees above a certain stem diameter are sampled, tree inventories can be assumed to be highly complete.  However, taxonomic groups that contain many individuals that are only identified to morphospecies (Coleoptera, Arachnida) are likely to be incompletely sampled.  Transect or point surveys, especially for highly vagile groups (BBS, CBC, NABA) can be assumed to be intermediate between the complete censusing of the forest surveys, and the incomplete sampling of the arthropod groups.  However, sampling completeness does not seem to provide an adequate explanation for the results of our study.  


<!--
The four paragraphs above should be condensed into 1-2 paragraphs.
-->

<!--
TODO: Add paragraph discussing implications for prediction
-->

###Conclusions
Although species abundance distribution models have different formulations, most models perform equivalently.  This raises the question of why disparate models have similar performance. [@frank2014] points out that general patterns typically have large numbers of models that fit, but that model fit does not neccessarily provide insight into pattern generating mechanisms.
[@locey2013] demonstrates that the majority of the possible forms for a species abundance distribution produced by combinatorics are clustered in a narrow range, suggesting that all model formulations are likely to fit relatively well.  We observed that log-likelihoods among the models in this study were equivalent, providing further evidence that the majority of species abundance distribution models fit equivalently well, and process cannot be identified by competing models against each other for a single pattern.  Instead, we suggest that the [@mcgill2003] recommendations for strong inference in macroecology (testing process-based model performance with multiple patterns at the same time) are the only appropriate approach for identifying macroecological mechanisms.  However, lack of ability to identify pattern generating mechanisms does not mean that a pattern is not useful for prediction, which is one of the goals to move macroecology forward as a discipline (McGill).  Another approach for identifying macroecological mechanism may be to examine the constraints that models have in common, for example, determining what factors are relevant to determining species richness (S) and abundance (N) at a site.


# References






