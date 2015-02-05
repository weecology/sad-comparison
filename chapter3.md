#Chapter 3

#Introduction
<!-- Connolly et al 2014. -->
Neutral theory is a big important theory

Can check for neutrality using abundance distribution data

Works for marine systems, does it work with more data, both terrestrial and marine.

#Methods
<!-- Redid analyses with more data-->
### Data
For this analysis, we used the data from White et al 2012 [@white2012], as well as the data described in chapter 2 of this dissertation.  These data cover 9 distinct taxonomic groups and include birds, mammals, reptiles, amphibians, bony fish, beetles, spiders, butterflies, and trees from 16,218 distinct communities over all major biogeographic regions.  The majority of the data are publicly available and were accessed through the EcoData Retriever [@morris2013] (US Geological Survey's North American Breeding Bird Survey [BBS; @pardieck2014], Mammal Community Database [MCDB; @thibault2011], US Forest Service Forest Inventory and Analysis [FIA; @fia], Gentry's Forest Transect Data Set [Gentry; @phillips2002]). The North American Butterfly Association count data [NABC; @naba] and the Audubon Society Christmas Bird Count [CBC; @cbc] are not publicly available and were obtained through Memorandums of Understanding with their respective organizations.

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
The lognormal distribution is one of the classic and most frequently used models used to describe the shape of the species abundance distribution [@mcgill2003].  While there are both continuous and discrete forms of this distribution, the discrete form of the distribution is more appropriate to use with abundance data [@citation].  We used the Poisson lognormal, the discrete form of the distribution, in our analyses.

#Results
<!-- Graphs  -->
Figures similar to Figure 1 minus the map and figure 2B.

#Discussion
<!--Big picture.-->