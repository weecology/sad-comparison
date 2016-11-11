Dear Sara,

My apologies for the long delay in returning this ms. The lead author has been
unable to work on this and it took me a while to carve out the time to complete
the revision.

We thank you and the reviewers for your kind words and helpful suggestions. We
have worked hard to improve the manuscript in response to these
comments. Our responses are described in detail below.

In addition to the recommended changes we have also worked on improving the
figures. We have introduced a consistent, color-blind friendly, color scheme
throughout to help the readers quickly recognize the different distributions on
the different figures. We have also reworked Figure 4 somewhat extensively to
both address Reviewer 2's concerns about font size but also improve the general
appearance and communication of the figure more broadly.

Regards,
Ethan White


Reviewer 1 (Matheus Lima Ribeiro)

> L. 64: Authors show Table 1, but did not cite it across the text. Please,
> provide citation for table 1.

Two references to Table 1 have been added to the text.

> L. 101-102: the sentence “best practices” is duplicated in this phrase.

This sentence has been simplified to remove the duplication.

> L. 103-104: the word “therefore” is also duplicated in this phrase.

We have removed the duplication.

> Title of Fig. 3: “Number of cases IN WHICH each model…” instead of “where”;

Changed.

> Idem Fig. 4!

Changed.

> L. 184: word “the” is duplicated;

Fixed.

> L. 187: “negative-binomial” instead of “negatvie-binomial”;

Fixed.

> In introduction (L. 34-39), authors justify one of the basic flaw of other
> studies about SADs is that they “use only a small subset of available
> models”. Next (L. 40), the authors describe the study’s goal and say that
> compared the performance of four SADs models. If one key question of
> investigation relates with the fitness of models, why that authors did not
> considered ALL existing SAD models in their analyses? These four chosen models
> often present the best performances (by the discussion, it seems that not!)?
> In methods, the authors justify their choice (the models describe discrete
> distribution, matching the type of data), but these questions remain unclear.

We selected models based on three criteria:

1. They needed to be proper, discrete, models for the SAD
2. They needed to have probability mass functions so that we could compare the
   likelihoods of the model, which eliminates all models that can only be
   described by simulation rules.
3. We prioritized models that represented an array of underlying process types
4. We wanted models that were commonly used in the ecological literature

While these were all described in the original manuscript, the descriptions were
scattered throughout the manuscript and we agree that our thinking on model
choice was unclear. We now start the Model section of the paper with a detailed
explanation of the justifications for the models we chose to work with.

> In methods, authors start saying that compiled a wide array of data sets from
> multiple sources and for multiple taxonomic groups, but do not say which kind
> of data they obtained. Are these data species occurrence records, species
> richness, population abundance…? Which is the temporal range of data? This is
> not clear in the text.

More details have been added in the opening paragraph. All data are full samples
of a given taxonomic assemblage and most data is for a single year. Additional
details are available in the provided citations.

> In lines 62-63 and 67-68, authors say that abundances were computed using
> counts of individuals. However, besides omit the kind of sampled raw data set,
> it is not clear what are the sampling units. For example, have the authors
> split the study area in grid cells (please, describe cell resolution)? Or the
> sampling units were ecoregions…?

More details have been added in the opening paragraph. In the vast majority of
cases the data is at the site level as defined by the data source

> L. 121-126: instead of just describe the list of R-packages used to perform
> analyses, please, describe which analyses were performed using each
> R-package. If possible, please, describe also the functions from each package
> used to perform analyses. A detailed description is a general practice from
> R-modelers and would clear the description of your methods.

We are quite experienced with best practices for presenting reproducible results
and I disagree quite strongly that best practice in this space involves filling
the methods section with lengthy descriptions of how individual functions from
individual packages are used to analyze individual results. The appropriate
place for that level of detail is in the openly available code associated with
an analysis. Our code is publicly available under open source licenses at
https://github.com/weecology/sad-comparison and we have now archived it on
Zenodo and added a link to this archive in the paper. It can be run by anyone to
replicate our results and read to look up individual function use if desired.

> L.172-174: I do not agree with this sentence. The authors did not compare
> model fitting between “fully” and “incompletely” sampled communities. It seems
> that authors considered all communities in their analyses, regardless of
> sampling effort. Thus, the presence of “fully censused” communities in this
> study may have negatively affected the fitness of Zipf models. Instead
> comparing the results of this study with other studies (especially Ulrich et
> al. 2010), I invite the authors to discuss about the implications of quality
> of data sets on model fitting;

As detailed in the sentences following lines 172-174 this argument is based on
comparing datasets that are very well sampled with those that are not. Ours come
in large aggregations that are also associated with taxonomic groups, but
none-the-less the comparison is very similar in concept to Ulrich et al. in that
they have a bunch of datasets some of which are determined to be fully censused
and some which are determined to be incomplete. In our case this is based on
meaningful differences in sampling methodology that are discussed in the
associated paragraph. In short, we don't understand the objection.

If the suggestion being made is that we use methods similar to those in Ulrich
et al., then we would note that there are serious issues with those methods that
effectively guarantee the results seen in that paper, because the methods used
for determining the degree of sampling are based on the shape of the abundance
distribution itself.

> L. 209-210: the author did not analyze the double geometric model in this
> study, so it is not a reasonable option to conclude that its performance
> appears to present minor difference with log-series, lognormal and negative
> binomial. This is speculation not supported by analyses;

This paragraph begins with "In combination, the results of these three papers
suggest..." This statement is based on the results of Alroy (2015) in
combination with our results.

> L. 214-216: this is an excellent conclusion from this study! It is supported
> by analyses performed here and yet considerate that found in
> literature. Please, develop all the discussion on this way and avoid
> unsupported speculations.

We thank the review for their kind words. As detailed above we do not believe
that we have engaged in "unsupported speculations" anywhere in the paper. We are
simply doing our best to fully engage with the existing literature within the
limits imposed by our analyses.

## Reviewer 2 (Anonymous)

> The paper is very 'self-contained' with clear, focused goals that are reported
> and discussed in context to previous work. The data is made open when
> possible. The english language is good, in some cases it could a shortened but
> the manuscript is already short so this is not a problem.

Thanks!

> Label sizes of Figure 4 should be increased if the plot is intended to be this
> size in the final article.

We have increased the label sizes on this figure and also worked to improve it
more generally so that it will communicate well with the readers and be easy to
view and understand on a printed pdf.

> The experimental design is transparent and simple, and well-described. The
> knowledge gap is clearly stated, although in this case it is more of an
> 'information gap' that is filled by comparing more data sets. The authors
> improve on previous work by gathering more data sets and testing a greater
> number of SAD models, which is good.

Thanks!

> The statistical methods are appropriate, the results seem solid and are well
> presented.

Thanks!

> However, since each dataset reports findings from one taxa, I don't know how
> certain it is to state that the SAD is different for different taxa. This
> might just be an artifact of the sampling method within each dataset which is
> correlated to taxa. The authors discuss that trees are fully sampled yet the
> selected SAD model is different for both of them (log-series for fia,
> log-series and poisson for gentry, figure 4, lines 176-177).

We agree with the limitation mentioned here and have added clarifying sentences
to end of the 2nd paragraph of the Discussion and the end of the third paragraph
of the Results.

> Are there datasets with several taxa that could be analysed? It would be
> interesting to break data up into sub-taxa within each category to assess if
> there are some general trends in SAD among subtaxa within a single taxa. For
> example, separate birds into passerines, parrots, falcons, pigeons, loons,
> etc, and see if the SAD model varies by subtaxa. Or by geographical regions.

These are definitely cool ideas and are things we've discussed, but we believe
they are more appropriate for a follow up analysis. We are unlikely to get to
this anytime soon, but would be happy to support anyone interested in
undertaking the effort.

> The article is clearly and concisely written. It set out clear goals and
> fulfilled them. As the authors state in the conclusion, there are clearly more
> detailed ways to analyse the SAD, with multiple macroecological patterns or
> second-order effects, but that was not their goal.

Thanks for the very kind, helpful, and positive review.

> 162 two parameter-model performing

Fixed.

> 184 remove one the

Fixed.

> 186 that the

Fixed.

> 187 negative

Fixed.

> 189 demonstrate

Fixed.

> 192 two analyses

Fixed.

> 200 showed that

Fixed.

> 207 those papers?

We prefer the original phrasing.

> 217 emphasize the challenge 

We have changed this to "emphasizes the challenge" since "emphasize" is
associated with the "relatively similar fit" not with "distributions".
