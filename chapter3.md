#Chapter 3- Evaluating abundance distribution based signals of neutrality.

#Introduction
<!--Neutral theory is a big important theory-->
A major set of ecological questions are what processes are involved structuring and maintaining ecological communities.  One theoretical approach that has been given a great deal of attention in recent years is the unified neutral theory of biodiversity [@matthews2014, @rosindelletal2012.  While there are multiple formulations of neutral theory, all models are based on the assumptions that species and individuals are ecologically and demographically equivalent to one another, causing stochastic variation in birth, death, immigration, and speciation to ultimately result in differences in species abundance [@rosindelletal2011].

Early evaluations of neutral theory were based on comparing the fit of empirical species abundance distributions to the neutral prediction [@citations]. Later evaluations of neutral theory thought that species abundance comparisons were not sufficient for a rigorous test of neutrality [@mcgill2006]. Recent work by Connolly et al. suggests that comparisons of species abundance distributions may be sufficient for the evaluation of neutral theory against competing models.
Building on work by Pueyo [@pueyo2006], Connolly et al. were able to identify non-neutral species abundance distributions in marine environments by comparing model fits of a lognormal distribution (non-neutral) to a gamma distribution (neutral)[@connolly2014].  This approach shows promise as a robust method for identifying communities that exhibit non-neutrality.

<!--Works for marine systems, does it work with more data, both terrestrial and marine.-->
While this approach has been preliminarily tested with marine communities over a broad geographic extent, it has not yet been tested in terrestrial systems <!--with a really expansive dataset-->.  Here, we evaluate the approach used by Connolly et al. [@connolly2014] over a much broader range of ecosystems and taxa.  We tested this approach for vertebrate, invertebrate and plant communities in primarily terrestrial ecosystems.  In total, we used abundance data from 16,218 communities to determine whether we observe patterns that are more consistent with neutrality or non-neutrality.

#Methods
<!-- Redid analyses with more data-->
### Data
For this study, we used the data from White et al. 2012 [@white2012], as well as the data described in chapter 2 of this dissertation.  These data cover 9 distinct taxonomic groups and include birds, mammals, reptiles, amphibians, bony fish, beetles, spiders, butterflies, and trees from 16,218 distinct communities over all major biogeographic regions.  The majority of the data are publicly available and were accessed through the EcoData Retriever [@morris2013] (US Geological Survey's North American Breeding Bird Survey [BBS; @pardieck2014], Mammal Community Database [MCDB; @thibault2011], US Forest Service Forest Inventory and Analysis [FIA; @fia], Gentry's Forest Transect Data Set [Gentry; @phillips2002]). The North American Butterfly Association count data [NABC; @naba] and the Audubon Society Christmas Bird Count [CBC; @cbc] are not publicly available and were obtained through Memorandums of Understanding with their respective organizations.

Table 1: Description of total number of sites per taxa and dataset.

| Taxa        | Dataset(s)     | Total sites |
|-------------|----------------|-------------|
| Birds       | BBS, CBC       | 4768        |
| Mammals     | MCDB           | 103         |
| Reptiles    | Reptilia       | 138         |
| Amphibians  | Amphibia       | 43          |
| Bony fish   | Actinopterygii | 161         |
| Beetles     | Coleoptera     | 5           |
| Spiders     | Arachnida      | 25          |
| Butterflies | NABC           | 400         |
| Trees       | FIA, Gentry    | 10575       |

All of the georeferenced data are presented in figure 1, redrawn from White et al. 2012.  Note that the data for reptiles, amphibians, bony fish, beetles, spiders, and butterflies are not represented, due to a lack of location data. 
![Figure 1. Map of the georeferenced portion of the data.  Note that the data for reptiles, amphibians, bony fish, beetles, spiders, and butterflies are not represented.](./sad-data/chapter3/partial_sites_map.png)

  
### Analysis
<!--Robust test with maximum likelihood methods and AiCc weights.-->
We followed the current best practice recommendations to use maximum likelihood methods for fitting and evaluating species abundance distributions models to data [@white2008; @connolly2014; @matthews2014].  This is the same approach used by Connolly et al. [@connolly2014].

Connolly et al. used Akaike Information Criterion (AIC) weights for model selection.  We used weights calculated from the corrected Akaike Information Criterion (AICc) values because the corrected form is more robust to small sample sizes, which was a consideration for some communities.  We used corrected Aikaike Information Criterion (AICc) weights to determine which model best approximated the data out of the set of fitted models.

<!--negative binomial vs. Poisson gamma:  Needs help regarding language and correctness-->
Negative binomial  
Connolly et al. used the negative binomial (referred to in their paper as the Poisson gamma distribution) as a good description of the neutral theory model in their analysis [@connolly2014].

Lognormal  
The lognormal distribution is one of the classic and most frequently used models used to describe the shape of the species abundance distribution [@mcgill2003].  While there are both continuous and discrete forms of this distribution, the discrete form of the distribution is more appropriate to use with abundance data [@bulmer1974].  We used the Poisson lognormal, the discrete form of the distribution, in our analyses.

#Results
<!-- Graphs  -->
Connolly et al. found that species abundance for empirical communities were best approximated by a lognormal rather than a negative binomial (gamma) distribution [@connolly2014].  However, our results found that there was no overwhelming support for the lognormal over the negative binomial distribution (Figure 2) at the site level. 
![Figure 2. Log of distinct abundance values versus AIC weight of the lognormal distribution for each dataset.](./sad-data/chapter3/distabclasses_vs_lognormwgt.png)


We also averaged the AIC weight of the Poisson lognormal distribution for each dataset, and did not observe a clear signal for one distribution over another (Figure 3).
![Figure 3. Average AIC weight of the lognormal distribution for each dataset.](./sad-data/chapter3/avgvals_by_dataset.png)


#Discussion
<!--Big picture.-->
<!-- Our results are consistent with chapter 1, in that it seems to be really hard to pick a clear winner among/between models.-->
Our results were consistent with our simultaneous comparisons of multiple species abundance distribution models in that it was difficult to identify a clear winning model (see details in Chapter 1 of this dissertation).  <!-- Our results differ from the Connolly results-->These results were contrary to what was predicted by Connolly et al, who demonstrated that the Poisson lognormal (non-neutral) outperformed the negative binomial (neutral) in marine systems [@connolly2014].  This suggests that marine systems are more generally approximated by non-neutral dynamics, while terrestrial and aquatic systems show more variability between neutral and non-neutral dynamics.  

<!--There are possible explanations for this.-->
<!--Could be a terrestrial vs. marine thing, although fish showed the same pattern.  The fish data was a little over half freshwater, a few estuary, and the rest marine, but a lot of near shore, mangrove-y areas.  No deep water sites.-->
Differences in marine vs. terrestrial systems are one possible explanation for the difference in our results relative to the results from Connolly et al. 2014.  However, while marine systems have not been as extensively studied as part of the macroecological research program as terrestrial systems, marine and terrestrial systems exhibit the same general macroecological patterns [@webb2012marine].  However, Webb 2012 raises the caveat that while the same general patterns apply, the processes generating those patterns may be different[@webb2012marine].  The results of this study could suggest that marine communities are more consistently structured by non-neutral processes than terrestrial communities.  While the vast majority of the data that we tested was terrestrial (approximately 99%), we did have 161 sites for fish.  Of these, the majority were freshwater, rather than marine; however we observed the same general pattern of results for fish as we did for the other taxa.

There are several potential explanations for the difference in results between our study and the Connolly 2014 paper, some non-biological (spatial structuring, sampling intensity), others related to biological/ecological differences in the data.

One potential non-biological explanation for the difference between our results and the Connolly 2014 results is differences in the spatial structure of the data: the data from Connolly 2014 is structured in natural spatial groupings, whereas the data that we used in this study is not.  In this study, the many of the sites used are more widely dispersed, or are not regularly dispersed over the landscape.  These differences in spatial grouping may lead to results that are more consistent, due to spatial similarity than our widely dispersed sites.  Related to spatial structuring, is the range of spatial scales present in the data. At a local scale (site) the range of spatial scales that data were collected varied from a very small area (FIA) to larger areas (CBC, BBS.)

Another potential non-biological explanation is related to sampling intensity.  It is possible that the way in which marine communities are sampled is different from sampling of terrestrial communities, resulting in differing intensity of sampling that produce different patterns.   However, the diversity of data we used covers the range of possible sampling intensities if sampling intensity was a major factor, ranging from a complete census (completely sampled trees), to less completely sampled (spiders, beetles).  Thus, it is unlikely that sampling intensity is producing the difference in results between marine communities and the terrestrial communities.

Because of the diversity of data that we used, with a wide range of sampling approaches, it is unlikely that the differences are due to the sampling approach rather than biological differences.  While more research needs to be done to determine what the differences are between the terrestrial and marine sites in this case, there are several possible biological explanations for the difference in results.

While many macroecological patterns hold true for marine systems, there are some significant differences between terrestrial and marine systems.  For example, many marine ecosystems exhibit an inverted biomass pyramid when compared to terrestrial systems. Biological/ecological diferences between marine and terrestrial systems could provide insight into differences in patterns of species abundance distributions.  One potential explanation comes from the core-occasional/core-transient species concept, in which core species, which are both common and temporally persistent demonstrate a different shape of the species abundance distribution than transient species, which are rare and temporally variable [@magurran2003explaining]. Differences in core vs. transient species between terrestrial and marine systems could provide an explanation for the difference in results.  

Various approaches for generating species abundance distributions suggest that species richness (S) and the total number of individuals (N) are important inputs into determining the shape of the species abundance distribution (citations, Harte, white2012, xiao, locey).  Differences in the ratio of S/N for terrestrial vs. marine communities could provide another potential explanation.  Further research needs to be done to determine if there is a difference in S/N ratios between the terrestrial data used in this study and the marine data used in Connolly 2014.-->
  
