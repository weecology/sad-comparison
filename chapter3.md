#Chapter 3- Evaluating abundance distribution based signals of neutrality.

#Introduction
<!--Neutral theory is a big important theory-->
Understanding what processes are involved structuring and maintaining ecological communities is a much studied ecological question. <!-- The previous sentence feels clunky and needs fixing.-->  One theoretical approach that has been given a great deal of attention in recent years is the unified neutral theory of biodiversity [@matthews2014, @rosindelletal2012<!--http://www.sciencedirect.com/science/article/pii/S0169534712000237, http://userwww.sfsu.edu/parker/bio840/pdfs/neutral/Case4EcolNeutralTheory.pdf-->.  While there are multiple formulations of neutral theory, all models are based on the assumptions that species and individuals are ecologically and demographically equivalent to one another, causing stochastic variation in birth, death, immigration, and speciation to ultimately result in differences in species abundance [@rosindelletal2011]<!--http://izt.ciens.ucv.ve/ecologia/Archivos/ECO_POB%202011/ECOPO7_2011/Rosindell%20et%20al%202011.pdf-->. 

<!--Can check for neutrality using abundance distribution data-->
Building on work by Pueyo [@pueyo2006], Connolly et al. were able to identify non-neutral species abundance distributions in marine environments by comparing model fits of a lognormal distribution (non-neutral) to a gamma distribution (neutral)[@connolly2014].  This approach shows promise as a robust method for identifying communities that exhibit non-neutrality.

<!--Works for marine systems, does it work with more data, both terrestrial and marine.-->
While this approach has been preliminarily tested with marine communities over a broad geographic extent, it has not yet been tested in terrestrial systems <!--with a really expansive dataset-->.  Here, we evaluate the approach used by Connolly et al. [@connolly2014] over a much broader range of ecosystems and taxa.  We tested this approach for vertebrate, invertebrate and plant communities in terrestrial, aquatic, and marine ecosystems.  In total, we used abundance data from 16,218 communities to determine whether we observe patterns that are more consistent with neutrality or non-neutrality.

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

  
### Analysis
<!--Robust test with maximum likelihood methods and AiCc weights.-->
We followed the current best practice recommendations to use maximum likelihood methods for fitting and evaluating species abundance distributions models to data [@white2008; @connolly2014; @matthews2014].  This is the same approach used by Connolly et al. [@connolly2014].

Connolly et al. used Akaike Information Criterion (AIC) weights for model selection.  We used weights calculated from the corrected Akaike Information Criterion (AICc) values because the corrected form is more robust to small sample sizes, which was a consideration for some communities.  We used corrected Aikaike Information Criterion (AICc) weights to determine which model best approximated the data out of the set of fitted models.

<!--negative binomial vs. Poisson gamma:  Needs help regarding language and correctness-->
Negative binomial  
Connolly et al. used the Poisson gamma distribution as a good description of the neutral theory model in their analysis [@connolly2014].  We used the negative binomial as an alternative formulation of the Poisson gamma.

Lognormal  
The lognormal distribution is one of the classic and most frequently used models used to describe the shape of the species abundance distribution [@mcgill2003].  While there are both continuous and discrete forms of this distribution, the discrete form of the distribution is more appropriate to use with abundance data [@bulmer1974].  We used the Poisson lognormal, the discrete form of the distribution, in our analyses.

#Results
<!-- Graphs  -->
Connolly et al. found that species abundance for empirical communities were best approximated by a lognormal rather than a negative binomial (gamma) distribution [@connolly2014].  However, our results found that there was no overwhelming support for the lognormal over the negative binomial distribution (Figure 1) at the site level. 
![Figure 1. Log of distinct abundance values versus AIC weight of the lognormal distribution for each dataset.](./sad-data/chapter3/distabclasses_vs_lognormwgt.png)


We also averaged the AIC weight of the lognormal distribution for each dataset, and did not observe a clear signal for one distribution over another.
![Figure 2. Average AIC weight of the lognormal distribution for each dataset.](./sad-data/chapter3/avgvals_by_dataset.png)


#Discussion
<!--Big picture.-->
<!-- Our results are consistent with chapter 1, in that it seems to be really hard to pick a clear winner among/between models.-->
<!-- Our results differ from the Connolly results-->
<!--There are possible explanations for this.-->
<!--Could be a terrestrial vs. marine thing, although fish showed the same pattern.  The fish data was a little over half freshwater, a few estuary, and the rest marine, but a lot of near shore, mangrove-y areas.  No deep water sites.-->
<!--Connolly paper showed smaller scale tended to be more toward the middle, larger scale tended toward upper end.-->