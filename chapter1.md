#Chapter 1 - An extensive comparison of species-abundance distribution models

# Introduction

The species abundance distribution (SAD) describes the full distribution of commonness and rarity in ecological systems. It is one of the most fundamental and ubiquitous patterns in ecology, and exhibits a consistent general form with many rare species and few abundant species occurring within a community. This general shape is often referred to as a hollow curve distribution.

The SAD is one of the most widely studied patterns in ecology, leading to a proliferation of models that attempt to characterize the shape of the distribution and identify potential mechanisms for the pattern [see @mcgill2007 for a recent review of SADs]. These models range from arbitrary distributions that are chosen based on providing a good fit to the data [@fisher1943], to distributions chosen based on combinatorics and the most likely state of the system, [@frank2011; @harte2011; @locey2013], to models based on ecological process [@tokeshi1993; @hubbell2001; @volkov2003].

Which model or models provide the best fit to the data, and the resulting implications for the processes structuring ecological systems, has been an active area of research  [e.g., @mcgill2003; @volkov2003; @ulrich2010; @white2012; @connolly2014]. However, most comparisons of the different models: 1) use only a small subset of available models [typically two; e.g., @mcgill2003; @volkov2003; @white2012; @connolly2014]; 2) focus on a single ecosystem or taxonomic group [e.g., @mcgill2003; @volkov2003]; or 3) fail to use the most appropriate statistical methods [e.g., @ulrich2010]. This makes it difficult to draw general conclusions about which, if any, models provide the best empirical fit to species abundance distributions.

Here, we evaluate the performance of five of the most widely used models for the species abundance distribution. We evaluate their performance using likelihood based model selection on data from 16,218 communities, from nine taxonomic groups. This includes data from terrestrial, aquatic, and marine ecosystems representing roughly 50 million individual organisms in total.


# Methods

### Data

We compiled data from citizen science projects, government surveys, and literature mining to produce a dataset with 16,218 communities, from nine taxonomic groups, representing nearly 50 million individual terrestrial, aquatic, and marine organisms. Data for trees, birds, butterflies and mammals was compiled by White et al. [-@white2012] from six data sources: the US Forest Service Forest Inventory and Analysis [FIA; @fia], the North American Butterfly Associations North American Butterfly Count [NABC; @naba], the Mammal Community Database [MCDB; @thibault2011], Alwyn Gentry's Forest Transect Data Set [Gentry; @phillips2002], the Audubon Society Christmas Bird Count [CBC; @cbc], and the US Geological Survey's North American Breeding Bird Survey [BBS; @pardieck2014]. The publicly available datasets (FIA, MCDB, Gentry, and BBS) were acquired using the EcoData Retriever [@morris2013]. Details of the treatment of these datasets can be found in Appendix A of White et al. [-@white2012]. Data on Actinopterygii, Reptilia, Coleoptera, Arachnida, and Amphibia, were mined from literature by Baldridge (see details in Chapter 1 of this dissertation).

<!--
Add note about not using Gentry sites 102 and 179 including detailed description of why we didn't use them.
-->

Table 1: Details of datasets used to evaluate the form of the species-abundance distribution. Datasets marked as Private were obtained through data requests to the providers resulting in Memorandums of Understanding governing data use.

| Dataset                              	| Dataset code 	| Availability                                     	| Total sites 	| Citation                                         	|
|--------------------------------------	|--------------	|----------------------------------	|-------------	|--------------------------------------------------	|
| Breeding Bird Survey 	                | BBS          	| Public                               	|2769             	| @pardieck2014                          	|
| Christmas Bird Count                 	| CBC          	| Private      	|1999             	| @cbc.              	|
| Alwyn Gentry's Forest Transects      	| Gentry       	| Public                               	|10355             	| @phillips2002                	|
| Forest Inventory Analysis            	| FIA          	| Public                               	|220             	| @fia                   	|
| Mammal Community Database            	| MCDB         	| Public                               	|103             	| @thibault2011                      	|
| North American Butterfly Count       	| NABA         	| Private  	|400             	| @naba 	|
| Actinopterygii      	                | Actinopterygii| Public  	|161             	| this dissertation	|
| Reptilia      	                    | Reptilia      | Public  	|138            	| this dissertation 	|
| Amphibia      	                    | Amphibia 	    | Public  	|43             	| this dissertation 	|
| Coleoptera      	                    | Coleoptera    | Public  	|5             	| this dissertation 	|
| Arachnida      	                    | Arachnida     | Public  	|25             	| this dissertation 	|

All abundances in the compiled datasets were counts of individuals.

### Models

The majority of species-abundance distributions (SADs) are constructed using counts of individuals [for discussion of alternative approaches see @mcgill2007 and @morlon2009]. As such, the data are discrete and therefore the most appropriate models are discrete distributions. Therefore we used only abundance data based on individual counts and used only discrete distributions that have been used as models for SADs.

McGill et al. [-@mcgill2007] classified models into five different families: purely statistical, branching process, population dynamics, niche partitioning, and spatial distribution of individuals. We evaluated models from each of the separate families, excluding the spatial distribution family, which requires spatially explicit data. Specifically, we evaluated the log-series, the Poisson log-normal, the negative binomial, the geometric series, and the Zipf distributions. All distributions were defined to have support defined by the positive integers (i.e., they are capable of having non-zero probability at values from 1 to infinity). We excluded models from analysis that do not have explicit likelihoods [e.g., some niche partitioning models; @sugihara1980; @tokeshi1993] so that we could use the likelihood based methods for fitting and evaluating distributions (see Analysis).

The log-series is one of the first distributions used to describe the SAD, being derived as a purely statistical distribution by Fisher [-@fisher1943]. It has since been derived as the result of both ecological processes, the metacommunity SAD for ecological neutral theory [@hubbell2001; @volkov2003], and several different maximum entropy models [@pueyo2007; @harte2008].

The lognormal is one of the most commonly used distributions for describing the SAD [@mcgill2003] and has been derived as a null form of the distribution resulting from the central limit theorem [@may1975], population dynamics [@engen1996], and niche partitioning [@sugihara1980]. We use the Poisson lognormal because it is a discrete form of the distribution appropriate for fitting discrete abundance data [@bulmer1974].

The negative-binomial (which can be derived as a mixture of the Poisson and Gamma distributions) provides a good characterization of the SAD predictions for several different ecological neutral models for the purposes of model selection [@connolly2014]. We use it to represent neutral models as a class.

The geometric series was one of the first distributions derived as a model of the SAD and was derived based on niche partitioning [@motomura1932].

The Zipf (or power law) distribution was derived based on branching processes and was one of the best fitting distributions in a recent meta-analysis of SADs [@ulrich2010]

### Analysis

Following current best practices for fitting distributions to data and evaluating their fit, we used maximum likelihood estimation to fit models to the data [@clark1999; @newman2005; @white2008] and likelihood based model selection to compare the fits of the different models [@burnham2002; @edwards2007]. These general best practices have recently been affirmed as best practices for species abundance distributions [@connolly2014; @matthews2014].

For model comparison we used corrected Aikaike Information Criterion (AICc) weights to compare the fits of models while correcting for differences in the number of parameters and appropriately handling the small sample sizes (i.e., numbers of species) in some communities [@burnham2002]. The Poisson log-normal and the negative binomial each have two fitted parameters, while the log-series, geometric series, and Zipf distributions have one fitted parameter each. The model with the greatest AICc weight in each community was considered to be the best fitting model for that community. We also assessed the full distribution of AICc weights to evaluate the similarity of the fits of the different models.

In addition to evaluating AICc of each model, we also examined the log-likelihood values of the models directly. We did this to assess the fit of the model while ignoring corrections for the number of parameters and the influence of similarities to other models in the set of candidate models.

Model fitting, log-likelihood, and AICc calculations were performed using the macroecotools Python package [https://github.com/weecology/macroecotools](https://github.com/weecology/macroecotools). All of the code and the majority of the data necessary to replicate these analyses is available at [https://github.com/weecology/sad-comparison](https://github.com/weecology/sad-comparison). The CBC datasets and NABA datasets are not publicly available and therefore are not included.

The negative-binomial distribution failed to converge for 1444 sites in FIA (13.9%), 5 sites in Gentry (2.3%), 3 sites in Reptilia (2.2%), and 1 site in NABA (0.25%). For these sites likelihoods and AICc weights were calculated for only those models which successfully converged.

# Results

Across all datasets, the log-series had the lowest value of AICc, indicating the best fit to the data, in the greatest proportion of datasets (42.9%). The geometric series also performed well based on AICc, providing the best fit in 33.7% of the datasets. The Poisson lognormal and negative binomial distributions provided the best fit in 8.8% and 8.5% of the datasets respectively, and the Zipf distribution had the fewest cases of the lowest AICc with 6.1% of datasets (Figure 1).

![Total wins by model for all datasets combined.](./sad-data/chapter1/total_wins.png)

Evaluating the best fitting distributions within individual datasets and taxonomic groups, the log-series was the most frequent best fitting model for all datasets except FIA (Figure 2). For the FIA data the geometric series provided the most frequent best fit to the data, and the strong performance of the geometric series in the FIA data is the cause of its strong performance when all of the data are analyzed together. The relative performance of the other models varies among datasets and taxonomic groups. The negative binomial performed well in the bird datasets (BBS and CBC), but was almost never the best fitting model for plants (FIA and Gentry), Coleoptera, Arachnida, or Reptilia. The Poisson lognormal performed well for the bird datasets and the Gentry tree data, but almost never won in the FIA and Coleoptera datasets (Figure 2). The Zipf distribution performed well for Arachnida, but was never the best fitting model for the bird datasets.

![Total wins by model for each dataset individually.](./sad-data/chapter1/wins_by_dataset.png)

The full distribution of AICc weights shows separation among models (Figure 3). On average, the Zipf and geometric distributions perform poorly, with the primary mode of the weight distribution occurring near zero (Figure 3). However, the geometric distribution also exhibits better performance for a subset of communities, with a secondary mode near 0.5. This mode is driven by the FIA data. The negative binomial and the Poisson lognormal distributions have peaks around 0.1, with the Poisson lognormal also having a small peak close to 1.0 indicating that in a small number of cases it provides a fit that is clearly superior to that of the other distributions (Figure 3).  The logseries performs the best overall, with a large mode spanning AICc values from 0.3 to 0.5, and secondary mode from 0.6-0.7 (Figure 3).

![AICc weights by model for all datasets combined.](./sad-data/chapter1/AICc_weights.png)
 
While the AICc weights show separation among models, these values include a correction for the number of parameters and are also influenced by the similarity between models. Therefore, we also compared the negative log-likelihoods of the different models to determine whether or not their absolute fits differed. Frequency distributions of log-likelihoods show almost complete overlap among models (Figure 4) and one-to-one plots of the likelihoods of each model against the likelihood of the log-series show that the likelihoods of the different models correspond almost perfectly for individual distributions (Figure 5). This indicates that all models fit the data equivalently and that differences in AICc weights resulted primarily from differences in the number of parameters and differences in how similar different models in the set of models were (i.e., if three identically fitting models are included in the analysis none of them can have a AICc weight > 0.34).

![Log-likelihoods by model for all datasets combined.](./sad-data/chapter1/likelihoods.png)

![Log-likelihoods by model for all datasets combined.](./sad-data/chapter1/likelihoods_one_to_one.png)

# Discussion

Our extensive comparison of different models for the species abundance distribution (SAD) using rigorous statistical methods demonstrates that most existing models provide equivalently good absolute fits to empirical data. As a result, the models with the fewest parameters perform better in AIC-based model selection since these approaches penalize model complexity. Since the log-series provides equivalent likelihoods to the other distributions, has a single fitted parameter, is easy to fit to empirical data, and is the best overall model using standard model selection, it provides a good naive model for fitting SADs.

The similar absolute fits of these five commonly used distributions emphasizes the challenges of inferring the processes operating in ecological systems from the form of the abundance distribution. It is already well established that models based on different processes can yield equivalent models of the SAD, i.e., they predict distributions of exactly the same form [@cohen1968, @pielou1975, @boswell1971, @mcgill2007]. It is also possible for the same biological explanations to result in  different forms of the species abundance distribution depending on community conditions [@hughes1986]. Our results support the idea that even when models do differ in their precise mathematical predictions that they are often not distinguishable enough to identify potential mechanisms with any degree of certainty [@volkov2005]. In other words, it is difficult to distinguish among the different distributions used to characterize the SAD, let alone the processes that generate the form of a particular distribution.

In cases where it is desirable to infer process based on macroecological patterns like the SAD, compare the predictions of different models using multiple macroecological patterns simultaneously is likely to be more effective [@mcgill2003, @mcgill2006, @newman2014, @xiao2015]. It has also been suggested that examining second-order effects, such as the scale-dependence of macroecological patterns  [@blonder2014] or the how the parameters of the distribution change across gradients [@macnally2014], can provide better inference about process from these kinds of pattern.

A previous analysis of ~500 SADs comparing three models, concluded that the form of the distribution varied consistently between fully censused communities, best fit by the lognormal, and incompletely sampled communities, best fit by the Zipf and logseries [@ulrich2010]. The most completely sampled data in our analysis is arguably the forest inventories (Gentry, FIA), since these inventories count all trees above a certain stem diameter and  detection of trees is straightforward so they are unlikely to be missed. The lognormal model is not the best fitting model in either of these datasets. The methods used by Ulrich et al. [@ulrich2010] involve the use of binning and fitting models to rank abundance plots, which deviates from the best practices [@matthews2014] used in this paper. A comparison of these two studies with equivalent methods will be necessary to resolve the discrepancies with respect to the influence of sampling on the observed form of the SAD.

In some cases linking ecological patterns to particular sets of processes is not the goal. In particular, ecological patterns can be used for prediction in the absence of any link to process. For example, the species-area relationship, which characterizes how the number of species observed changes with spatial scale, is often used to make predictions for how many species will occur at larger and smaller scales than those observed. This is done without a strong link between biological processes and the empirical pattern. The SAD has been similarly used by White et al. [@white2012] who used the log-series to make predictions for the number of rare species occurring in a community. These predictions are independent of the processes generating the log-series. Given the equivalent fit of the five different distributions observed in this study, it is likely that any choice of distribution would have yielded equivalently strong predictions. In fact, patterns that not strongly contingent on the operation of specific processes can be applied to prediction more broadly, because it is not necessary to understand the detailed biology of the system in order to use them.

It is interesting to consider why so many different models for the SAD yield similar predictions and fits to empirical data. Frank [@frank2009, @frank2014] suggests that general patterns do not result from specific processes, but from the fact that there are many possible ways in which that pattern can be generated. For the SAD it has been shown that of the possible forms of the SAD (the "feasible set") most have similar general shapes [@locey2013]. This suggests that most data and most model predictions will have similar forms because most possible forms are similar. Maximum entropy based predictions for the SAD similarly suggest that the observed SAD should be the most likely possible form based on the random assignment of abundances to species under some basic constraints [@pueyo2007; @harte2008; @harte2011; @white2012]. The fact that we observed equivalent log-likelihoods across five different models from a diverse array of ecosystems and taxonomic groups, that are likely being influenced by a diverse array of processes, supports the idea that the detailed processes operating in ecological systems are not having direct and meaningful influences on the SAD [@white2012; but see @macnally2014].

# Acknowledgments

This research was supported by the National Science Foundation through a CAREER Grant 0953694 to Ethan White, and by the Gordon and Betty Moore Foundation's Data-Driven Discovery Initiative through Grant GBMF4563 to Ethan White.

# References






