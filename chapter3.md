#Chapter 3- Evaluating abundance distribution based signals of neutrality in terrestrial systems

#Introduction
<!--Neutral theory is a big important theory-->
One of the fundamental goals of ecology is understanding what processes are important in structuring ecological communities. One of the major areas of debate surrounding goal is whether simple neutral models that ignore differences between species can explain many of the empirical patterns observed in ecological systems [@mcgill2006; @rosindelletal2012; @matthews2014]. While there are multiple formulations of neutral theory, all models are based on the assumptions that species and individuals are ecologically and demographically equivalent to one another, meaning that stochastic variation in birth, death, immigration, and speciation drives differences in a broad array of ecological patterns including the species abundance distribution, the species-area relationship, and the distance decay of similarity [@rosindelletal2011].

Early evaluations of neutral theory were based, in part, on comparing the fit of empirical species abundance distributions to the neutral prediction [e.g., @hubbell2001; @mcgill2003; @volkov2003]. However, further evaluations of neutral theory suggested that comparisons based on the species abundance distribution were not sufficient for rigorous tests of neutrality [@volkov2005; @mcgill2006; @volkov2006]. This idea is further supported by work suggesting that species abundance distributions may contain little information about the detailed processes operating in ecological system more generally [@pielou1975; @white2012; @locey2013]. In contrast, recent work by Connolly et al. (2014) suggests that comparisons of species abundance distributions may be sufficient for evaluating whether or not neutral processes are dominant or whether other processes are important in structuring communities.
Building on work by Pueyo [@pueyo2006], Connolly et al. (2014) were able to demonstrate that simulated neutral communities were typically better fit by negative-binomial distributions (referred to as Poisson gamma distributions by Connolly et al. 2014) than by Poisson lognormal distributions. They then performed the same analysis on over 1000 marine communities, and showed that the empirical communities were better fit by the lognormal [@connolly2014]. This suggests that, at least in marine environments, the shape of the species abundance distribution can be used to exclude neutral processes as the sole determinant of community structure. By focusing on the detailed fits of alternative models, this approach takes advantage of 'second-order effects', which have been proposed to provide an avenue for inferring ecological process  based on patterns of community structure [@blonder2014].

<!--Works for marine systems, does it work with more data, both terrestrial and marine.-->
While this approach has been well tested within marine communities, it has not yet been used in terrestrial systems. Here, we use Connolly et al.'s [@connolly2014] method to assess potential patterns of neutrality across a broad range of ecosystems and taxonomic groups. We tested this approach for vertebrate, invertebrate and plant communities in primarily terrestrial ecosystems. In total, we used abundance data from 16,218 communities from across to globe to determine whether we observe patterns that are more consistent with neutrality or non-neutrality.

#Methods

### Data
We compiled data from 9 distinct taxonomic groups and include birds, mammals, reptiles, amphibians, beetles, spiders, butterflies, trees, and bony fish from 16,218 distinct communities over all major biogeographic regions (Table 1, Figure 1). This dataset is a combination fo the data compiled by White et al. 2012 [@white2012] and the data described in Chapter 1 of this dissertation. The majority of the data are publicly available and were accessed through the EcoData Retriever [@morris2013]. These data included the US Geological Survey's North American Breeding Bird Survey [BBS; @pardieck2014], Mammal Community Database [MCDB; @thibault2011], US Forest Service Forest Inventory and Analysis [FIA; @fia], and Gentry's Forest Transect Data Set [Gentry; @phillips2002], and the data from Chapter 1. The North American Butterfly Association count data [NABC; @naba] and the Audubon Society Christmas Bird Count [CBC; @cbc] are not publicly available and were obtained through Memorandums of Understanding with their respective organizations.

Table 1: Description of total number of sites per taxa and dataset. Taxonomic groups are ordered by the total number of sites in the compiled dataset.

| Taxa        | Dataset(s)     | Total sites |
|-------------|----------------|-------------|
| Trees       | FIA, Gentry    | 10575       |
| Birds       | BBS, CBC       | 4768        |
| Butterflies | NABC           | 400         |
| Reptiles    | Reptilia       | 138         |
| Bony fish   | Actinopterygii | 161         |
| Mammals     | MCDB           | 103         |
| Amphibians  | Amphibia       | 43          |
| Spiders     | Arachnida      | 25          |
| Beetles     | Coleoptera     | 5           |


The locations of all of the data with detailed georeferencing information are presented in Figure 1. Note that the data for reptiles, amphibians, bony fish, beetles, spiders, and butterflies are not represented, due to a lack of detailed location data.

![Figure 1. Map of the georeferenced portion of the data.  Note that the data for reptiles, amphibians, bony fish, beetles, spiders, and butterflies are not represented. Redrawn from White et al. 2012](./sad-data/chapter3/partial_sites_map.png)


### Analysis
<!--Robust test with maximum likelihood methods and AiCc weights.-->

Following Connolly et al., we used maximum likelihood methods for fitting and evaluating species abundance distributions models to data (the currently accepted best practice) [@white2008; @connolly2014; @matthews2014]. This yielded fits of each distribution to each of the 16,000 communities in the dataset (Figure 2).

![Figure 2. Preston plot of empirical data for each dataset with lines representing the Poisson lognormal and the negative binomial.](./sad-data/chapter3/EmpirModelHist.png)

Connolly et al. used Akaike Information Criterion (AIC) weights to compare the fits of the negative-binomial and Poisson lognormal distributions to the empirical data. We modified this approach slightly by using weights calculated from the corrected Akaike Information Criterion (AICc) values, because AICc is more robust to small sample sizes [@burnham2002], which was a consideration for some communities. Model weights were calculated relative to the Poisson lognormal, meaning that weights near zero support the negative-binomial as the better fitting model while weights near one support the Poisson lognormal as the better fitting model.


#Results
<!-- Graphs  -->
Connolly et al. found that species abundance for empirical communities were best approximated by a lognormal rather than a negative binomial (gamma) distribution [@connolly2014].  However, our results found that there was no overwhelming support for the lognormal over the negative binomial distribution (Figure 2) at the site level.
![Figure 3. Log of distinct abundance values versus AIC weight of the lognormal distribution for each dataset.](./sad-data/chapter3/distabclasses_vs_lognormwgt.png)


We also averaged the AIC weight of the Poisson lognormal distribution for each dataset, and did not observe a clear signal for one distribution over another (Figure 3).
![Figure 4. Average AIC weight of the lognormal distribution for each dataset.](./sad-data/chapter3/avgvals_by_dataset.png)


#Discussion
<!--Big picture.-->
<!-- Our results are consistent with chapter 1, in that it seems to be really hard to pick a clear winner among/between models.-->
Our results were consistent with our multiple species abundance distribution model comparisons in that it was difficult to identify a clear winning model (see details in Chapter 3 of this dissertation).  <!-- Our results differ from the Connolly results-->These results were contrary to what was predicted by Connolly et al., who demonstrated that the Poisson lognormal (non-neutral model) outperformed the negative binomial (neutral model) in marine systems [@connolly2014].  This suggests that marine systems are more generally approximated by non-neutral dynamics, while terrestrial and aquatic systems show more variability between neutral and non-neutral dynamics.  

<!--There are possible explanations for this.-->
<!--Could be a terrestrial vs. marine thing, although fish showed the same pattern.  The fish data was a little over half freshwater, a few estuary, and the rest marine, but a lot of near shore, mangrove-y areas.  No deep water sites.-->
Differences in marine vs. terrestrial systems are one possible explanation for the difference in our results relative to the results from Connolly et al. 2014.  However, while marine systems have not been as extensively studied as part of the macroecological research program as terrestrial systems, marine and terrestrial systems exhibit many of the same general macroecological patterns [@webb2012marine].  However, Webb 2012 raises the caveat that while the same general patterns apply, the processes generating those patterns may be different [@webb2012marine].  The results of this study could suggest that marine communities are more consistently structured by non-neutral processes than terrestrial communities.  While the vast majority of the data that we tested was terrestrial (approximately 99%), we did have 161 sites for fish.  Of these, the majority were freshwater, rather than marine; however we observed the same general pattern of results for fish as we did for the other taxa.

Marine systems have been heavily impacted historically for both target and non-target species.  While terrestrial systems have also experienced anthropogenic influences, there has been a difference in intensity and in patterns of use and management of taxa, with terrestrial systems.  Primarily wild populations of consumers are targeted in marine systems, while terrestrial systems focus more on land use for domesticated producers.  This legacy of marine exploitation and over-exploitation is a distinctly non-neutral influence on the structure of marine species abundance distributions that seems to produce a strong signal.  There are several additional potential explanations for the difference in results between our study and the Connolly 2014 paper, some non-biological (spatial structuring, sampling intensity), others related to biological/ecological differences in the data.

One potential non-biological explanation for the difference between our results and the Connolly 2014 results is differences in the spatial structure of the data: the data from Connolly 2014 is structured in natural spatial groupings, whereas the data that we used in this study is not.  In this study, the many of the sites used are more widely dispersed, or are not regularly dispersed over the landscape.  These differences in spatial grouping may lead to results that are more consistent, due to spatial similarity than our widely dispersed sites.  Related to spatial structuring, is the range of spatial scales present in the data. At a local scale (site) the range of spatial scales that data were collected varied from a very small area (FIA) to larger areas (CBC, BBS.)

Another potential non-biological explanation is related to sampling intensity.  It is possible that the way in which marine communities are sampled is different from sampling of terrestrial communities, resulting in differing intensity of sampling that produce different patterns.   However, the diversity of data we used covers the range of possible sampling intensities if sampling intensity was a major factor, ranging from a complete census (completely sampled trees), to less completely sampled (spiders, beetles).  Thus, it is unlikely that sampling intensity is producing the difference in results between marine communities and the terrestrial communities.

Because of the diversity of data that we used, with a wide range of sampling approaches, it is unlikely that the differences are due to the sampling approach rather than biological differences.  While more research needs to be done to determine what the differences are between the terrestrial and marine sites in this case, there are several possible biological explanations for the difference in results.  While many macroecological patterns hold true for marine systems, there are some significant differences between terrestrial and marine systems.  For example, many marine ecosystems exhibit an inverted biomass pyramid when compared to terrestrial systems. Biological/ecological diferences between marine and terrestrial systems could provide insight into differences in patterns of species abundance distributions.  One potential explanation comes from the core-occasional/core-transient species concept, in which core species, which are both common and temporally persistent demonstrate a different shape of the species abundance distribution than transient species, which are rare and temporally variable [@magurran2003explaining]. Differences in core vs. transient species between terrestrial and marine systems could provide an explanation for the difference in results.  


Various approaches for generating species abundance distributions suggest that species richness (S) and the total number of individuals (N) are important inputs into determining the shape of the species abundance distribution (citations, Harte, white2012, xiao, locey).  Differences in the ratio of S/N for terrestrial vs. marine communities could provide another potential explanation.  Further research needs to be done to determine if there is a difference in S/N ratios between the terrestrial data used in this study and the marine data used in Connolly 2014.  
