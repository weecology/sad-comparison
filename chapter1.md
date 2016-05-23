An extensive comparison of species-abundance distribution models

Elita Baldridge, *elita.baldridge@weecology.org, Utah State University*, David J. Harris, *University of Florida*, Xiao Xiao, *Utah State University, University of Maine*, and Ethan P. White, *Utah State University, University of Florida*

# Introduction

The species abundance distribution (SAD) describes the full distribution of commonness and rarity in ecological systems. It is one of the most fundamental and ubiquitous patterns in ecology, and exhibits a consistent general form with many rare species and few abundant species occurring within a community. This general shape is often referred to as a hollow curve.

The SAD is one of the most widely studied patterns in ecology, leading to a proliferation of models that attempt to characterize the shape of the distribution and identify potential mechanisms for the pattern [see @mcgill2007 for a recent review of SADs]. These models range from arbitrary distributions that are chosen based on providing a good fit to the data [@fisher1943], to distributions chosen based on the most likely states of generic random systems [@frank2011; @harte2011; @locey2013], to models based more directly on ecological processes [@tokeshi1993; @hubbell2001; @volkov2003; @alroy2015].

Which model or models provide the best fit to the data, and the resulting implications for the processes structuring ecological systems, has been an active area of research [e.g., @mcgill2003; @volkov2003; @ulrich2010; @white2012; @connolly2014]. However, most comparisons of the different models: 1) use only a small subset of available models [typically two; e.g., @mcgill2003; @volkov2003; @white2012; @connolly2014]; 2) focus on a single ecosystem or taxonomic group [e.g., @mcgill2003; @volkov2003]; or 3) fail to use the most appropriate statistical methods [e.g., @ulrich2010]. This makes it difficult to draw general conclusions about which, if any, models provide the best empirical fit to species abundance distributions.

Here, we evaluate the performance of four of the most widely used models for the species abundance distribution. We evaluate their performance using likelihood-based model selection on data from 16,209 communities, from nine taxonomic groups. This includes data from terrestrial, aquatic, and marine ecosystems representing roughly 50 million individual organisms in total.


# Methods

### Data

We compiled data from citizen science projects, government surveys, and literature mining to produce a dataset with 16,209 communities, from nine taxonomic groups, representing nearly 50 million individual terrestrial, aquatic, and marine organisms. Data for trees, birds, butterflies and mammals was compiled by White et al. [-@white2012] from six data sources: the US Forest Service Forest Inventory and Analysis [FIA; @fia], the North American Butterfly Association's North American Butterfly Count [NABC; @naba], the Mammal Community Database [MCDB; @thibault2011], Alwyn Gentry's Forest Transect Data Set [Gentry; @phillips2002], the Audubon Society Christmas Bird Count [CBC; @cbc], and the US Geological Survey's North American Breeding Bird Survey [BBS; @pardieck2014]. The publicly available datasets (FIA, MCDB, Gentry, and BBS) were acquired using the EcoData Retriever [@morris2013]. Details of the treatment of these datasets can be found in Appendix A of White et al. [-@white2012]. Data on Actinopterygii, Reptilia, Coleoptera, Arachnida, and Amphibia, were mined from literature by Baldridge and are publicly available [@Baldridge2013].

<!--
Add note about not using Gentry sites 102 and 179 including detailed description of why we didn't use them.
-->

Table 1: Details of datasets used to evaluate the form of the species abundance distribution. Datasets marked as Private were obtained through data requests to the providers resulting in Memorandums of Understanding governing data use.

| Dataset                              	| Dataset code 	| Availability                                     	| Total sites 	| Citation                                         	|
|--------------------------------------	|--------------	|----------------------------------	|-------------	|--------------------------------------------------	|
| Breeding Bird Survey 	                | BBS          	| Public                               	|2769             	| @pardieck2014                          	|
| Christmas Bird Count                 	| CBC          	| Private      	|1999             	| @cbc.              	|
| Alwyn Gentry's Forest Transects      	| Gentry       	| Public                               	|220              	| @phillips2002                	|
| Forest Inventory Analysis            	| FIA          	| Public                               	| 10355           	| @fia                   	|
| Mammal Community Database            	| MCDB         	| Public                               	|103             	| @thibault2011                      	|
| North American Butterfly Count       	| NABA         	| Private  	|400             	| @naba 	|
| Actinopterygii      	                | Actinopterygii| Public  	|161             	| @Baldridge2013	|
| Reptilia      	                    | Reptilia      | Public  	|129            	| @Baldridge2013 	|
| Amphibia      	                    | Amphibia 	    | Public  	|43             	| @Baldridge2013	|
| Coleoptera      	                    | Coleoptera    | Public  	|5             	| @Baldridge2013 	|
| Arachnida      	                    | Arachnida     | Public  	|25             	| @Baldridge2013 	|

All abundances in the compiled datasets were counts of individuals.

### Models

The majority of species abundance distributions (SADs) are constructed using counts of individuals [for discussion of alternative approaches see @mcgill2007 and @morlon2009]. As such, the data are discrete and therefore discrete distributions are more appropriate.

McGill et al. [-@mcgill2007] classified species abundance distribution models into five different families: purely statistical, branching process, population dynamics, niche partitioning, and spatial distribution of individuals. We evaluated models from each of the separate families, excluding the spatial distribution family, which requires spatially explicit data. Specifically, we evaluated the log-series, the Poisson lognormal, the negative binomial, and the Zipf distributions. All distributions were defined to be capable of having non-zero probability at values from 1 to infinity. We excluded models from analysis that do not have explicit likelihoods [e.g., geometric; @motomura1932, some niche partitioning models; @sugihara1980; @tokeshi1993, double geometric; @alroy2015] so we could use likelihood based methods for fitting and evaluating distributions (see Analysis).

The log-series is one of the first distributions used to describe the SAD, being derived as a purely statistical distribution by Fisher [-@fisher1943]. It has since been derived as the result of ecological processes, the metacommunity SAD for ecological neutral theory [@hubbell2001; @volkov2003], and several different maximum entropy models [@pueyo2007; @harte2008].

The lognormal is one of the most commonly used distributions for describing the SAD [@mcgill2003] and has been derived as a null form of the distribution resulting from the central limit theorem [@may1975], population dynamics [@engen1996], and niche partitioning [@sugihara1980]. We use the Poisson lognormal because it is a discrete form of the distribution appropriate for fitting discrete abundance data [@bulmer1974].

The negative binomial (which can be derived as a Gamma-distributed mixture of Poisson distributions) provides a good characterization of the SAD predictions for several different ecological neutral models for the purposes of model selection [@connolly2014]. We use it to represent neutral models as a class.

The Zipf (or power law) distribution was derived based on branching processes and was one of the best fitting distributions in a recent meta-analysis of SADs [@ulrich2010].

### Analysis

Following current best practices for fitting distributions to data and evaluating their fit, we used maximum likelihood estimation to fit models to the data [@clark1999; @newman2005; @white2008] and likelihood-based model selection to compare the fits of the different models [@burnham2002; @edwards2007]. These general best practices have recently been affirmed as best practices for species abundance distributions [@connolly2014; @matthews2014].

For model comparison we used corrected Akaike Information Criterion (AICc) weights to compare the fits of models while correcting for differences in the number of parameters and appropriately handling the small sample sizes (i.e., numbers of species) in some communities [@burnham2002]. The Poisson lognormal and the negative binomial each have two fitted parameters, while the log-series distribution and the Zipf distributions have one fitted parameter each. The model with the greatest AICc weight in each community was considered to be the best fitting model for that community. We also assessed the full distribution of AICc weights to evaluate the similarity of the fits of the different models.

In addition to evaluating AICc of each model, we also examined the log-likelihood values of the models directly. We did this to assess the fit of the model while ignoring corrections for the number of parameters and the influence of similarities to other models in the set of candidate models.

Model fitting, log-likelihood, and AICc calculations were performed using the macroecotools Python package [https://github.com/weecology/macroecotools](https://github.com/weecology/macroecotools) and with the R programming language [@r2006]. All of the code and the majority of the data necessary to replicate these analyses is available at [https://github.com/weecology/sad-comparison](https://github.com/weecology/sad-comparison). The CBC datasets and NABA datasets are not publicly available and therefore are not included.

# Results

Across all data sets, the negative binomial and Poisson lognormal distributions had very similar average log-likelihoods (within 0.01 of one another). The log-likelihoods for each of these distributions averaged 0.8 units higher than for the log-series distribution and 5 units higher than for the Zipf distribution (corresponding to likelihoods that were twice as high and 140 times as high, respectively).

Although the negative binomial and Poisson lognormal distributions matched the data most closely, the likelihood provides a biased estimate of these distributions' ability to generalize to unobserved species. AICc approximately removes this bias by penalizing models with more degrees of freedom---such as the negative binomial and Poisson lognormal distributions, which have two free parameters instead of one like the log-series and Zipf distributions. After applying this penalty, the log-series distribution would be expected to make the best predictions for 69.2% of the sites. The Poisson lognormal and negative binomial distributions were each preferred in about 12% of the sites, and the Zipf distribution was preferred least often (6.0% of sites; Figure 1).

![Total wins by model for all datasets combined.](./sad-data/chapter1/total_wins.png)

Across all data sets and taxonomic groups, the log-series distribution had the highest AICc weights more often than any other model. The negative binomial performed well for BBS, but was almost never the best fitting model for plants (FIA and Gentry),  butterflies (NABA), Acintopterygii, or Coleoptera. The Poisson lognormal performed well for the bird datasets (BBS and CBC) and the Gentry tree data, but almost never won in the FIA and Coleoptera datasets (Figure 2). The Zipf distribution performed well for Arachnida, but was never the best fitting model for the bird datasets.

![Total wins by model for each dataset individually.](./sad-data/chapter1/wins_by_dataset.png)

The full distribution of AICc weights shows separation among models (Figure 3). Although the log-series distribution had the best AICc score much more often than the other models, Figure 3 shows that its lead was never decisive: across all 16,209 sites, it never had more than about 75% of the AICc weight. Most of the remaining weight was assigned to the negative binomial and Poisson lognormal distributions (each of which usually had at least 12-15% of the weight but was occasionally favored very strongly).  The Zipf distribution showed a strong mode near zero, and usually had less than 7% of the weight.

![AICc weights by model for all datasets combined.](./sad-data/chapter1/AICc_weights.png)

![Log-likelihoods by model for all datasets combined.](./sad-data/chapter1/likelihoods.png)

![Log-likelihoods by model for all datasets combined.](./sad-data/chapter1/likelihoods_one_to_one.png)

# Discussion

Our extensive comparison of different models for the species abundance distribution (SAD) using rigorous statistical methods demonstrates that several of the most popular existing models provide equivalently good absolute fits to empirical data. As a result, the models with the fewest parameters performed better in AICc-based model selection, which penalizes model complexity. Since the log-series provides essentially equivalent likelihoods to the other distributions, has a single fitted parameter, is easy to fit to empirical data, and is the best overall model using standard model selection, it provides a good baseline model whenever the biological mechanisms behind the SAD are not of primary concern (e.g. when the goal is to predict the number of rare species in a community; [@white2012]).

Our results differ from the analysis of ~500 SADs by [@ulrich2010], which found that the form of the abundance distribution varied consistently between fully censused communities, best fit by the lognormal, and incompletely sampled communities, best fit by the Zipf and log-series [@ulrich2010]. Our AICc values do not support the conclusion that the lognormal outperforms the log-series in well-sampled communities (e.g. the Gentry and FIA forest inventories, which involve large stationary organisms and were collected with the goal of including all trees above a certain stem diameter). Moreover, the Zipf distribution consistently performed worse in our analyses than the other three methods. The discrepancy between our results and those found in [@ulrich2010] are probably due to their use of binning and fitting curves to rank abundance plots, which deviates from the likelihood-based best practices [@matthews2014] used in this paper.

The relatively similar fits of several commonly used distributions emphasizes the challenges of inferring the processes operating in ecological systems from the form of the abundance distribution. It is already well established that models based on different processes can yield equivalent models of the SAD, i.e., they predict distributions of exactly the same form [@cohen1968, @pielou1975, @boswell1971, @mcgill2007]. To the extent that SADs are determined by random statistical processes, one might expect the observed distributions to be compatible with a wide variety of different process-based and process-free models [@frank2009, @frank2011, @locey2013]. Regardless of the underlying reason that the models performed similarly, our results indicate that the SAD usually does not contain sufficient information to distinguish among the possible statistical processes---let alone biological processes---with any degree of certainty [@volkov2005]. A more promising way to draw inferences about ecological processes is to evaluate each model's ability to simultaneously explain multiple macroecological patterns, rather than relying on a single pattern like the SAD [@mcgill2003, @mcgill2006, @newman2014, @xiao2015]. It has also been suggested that examining second-order effects, such as the scale-dependence of macroecological patterns [@blonder2014] or how the parameters of the distribution change across gradients [@macnally2014], can provide better inference about process from these kinds of pattern.

# Acknowledgments

This research was supported by the National Science Foundation through a CAREER Grant 0953694 to Ethan White, and by the Gordon and Betty Moore Foundation's Data-Driven Discovery Initiative through Grant GBMF4563 to Ethan White.

# References
