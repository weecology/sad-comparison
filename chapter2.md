# Chapter 2- Community abundance data of underrepresented taxonomic groups.

## Abstract
The majority of publicly available datasets used for macroecological research have a North American terrestrial bias, and focus primarily on warm-blooded vertebrates and plants. This dataset helps to improve the availability of data suitable for macroecological questions for less frequently studied taxa. The data were compiled from the literature by focusing on less frequently studied groups, and includes seven classes of animals, amphibians, spiders, beetles, reptiles, birds, and ray finned and cartilaginous fish. The data contains data representing over 2000 species and more than 1.3 million individuals from over 700 sites including locations on all continents except Antarctica.

## Background & Summary
Increasingly large amounts of data are available for studying ecological systems [@reichman2011]. One of the most common forms of ecological data is community abundance data, which is composed of counts of the number of individuals of each species occuring in a community or assemblage. These kinds of data can be used to address a broad array of questions and have become central to research in macroecology.

One major criticism of macroecology is that the majority of research has been driven by a few major datasets, primarily terrestrial North American and European birds, mammals, and plants [@beck2012]. This is due, in part, to the fact that large publicly available datasets with many sites tend to focus on these taxonomic groups [e.g., @fia; @pardieck2014; @thibault2011]. This makes it difficult to determine if observed patterns are general or whether they only apply to the few taxa for which large amounts of easy to analyze data is available. It also makes it difficult to perform meaningful cross-taxonomic comparisons, which can be valuable to understanding the processes driving ecological systems. One suggestion for improving macroecology in this regard is to make better use of existing data [@beck2012]. There is a great deal of community abundance data in the literature, but most include a single to a few communities, and the majority of the data requires data entry and processing to be useable in analyses. In particular, much of this data is only available tables in the text of papers.

To address this deficit in readily available data, I have compiled a dataset from the literature that combines data for multiple taxa and biogeographic regions into a single publicly available source. This will allow researchers to make ecological comparisons for a wider range of taxa without having to gather and process the data from the literature before use. This data compilation contains abundance data for seven classes of animal, including vertebrates and invertebrates, endotherms and ectotherms, and was collected by intentionally focusing on the collection of data for taxa that are not currently well represented in commonly used macroecological datasets.

This emphasis on underrepresented taxa resulted in large amounts of data for fish, reptiles, and amphibians and reasonable amounts of data for spiders and insects (Figure 1, Figure 2). While the majority of the data is Nearctic, there is a worldwide distribution of sites (Figure 3), improving the representation of data outside of North America. This dataset will allow for a more robust comparison of patterns across taxa, especially when combined with existing macroecological datasets. While the primary focus of data collection was filling in the gaps for vertebrate taxa, I also collected community abundance data on other taxa incidentally.

![Number of sites per taxon](./sad-data/chapter2/taxa_sites.png)

![Number of individuals per taxon.](./sad-data/chapter2/num_taxa.png)

![Number of sites per biogeographic region.](./sad-data/chapter2/bioregions.png)

## Methods

### Data Sources

Data were compiled from a combination of journal articles, theses, and dissertations. The taxonomic focus of the literature search has determined based on an initial search of the literature for community abundance data to get a sense of what data were available, and which underrepresented taxa were likely to yield reasonable amounts of data. After the initial search, I conducted a systematic through the literature, with fish, amphibians, and reptiles as the main focus of data collection. Data for other groups were collected on an *ad hoc* when they were encountered, which resulted in a reasonable amount of data for arachnids and insects (Figure 1).

----------------------------------------------------------------------------------------------------------------
 Search Parameters                                               Search engine                Date Accessed 
 -------------------------------------------------------------   -----------------------      ------------------
 community abundance in Biology, Life Sciences, etc.             Google Scholar               29 Nov 2010

 fish assemblage abundance, fish community* abundance            Google Scholar               14 Feb 2011
 in Biology, Life Sciences, etc.
 
 fish community* abundance, fish assemblage abundance            ProQuest UMI                 15 Feb 2011
                                                                 Dissertations & Theses

 reptile assemblage abundance, reptile community* abundance      Google Scholar               20 Aug 2011
 in Biology, Life Sciences, etc.
 
 reptile community* abundance, reptile assemblage abundance      ProQuest UMI                 21 Aug 2011
                                                                 Dissertations & Theses
 
 amphibian assemblage abundance, amphibian community* abundance  Google Scholar               7 Oct 2011
 in Biology, Life Sciences, etc.
 
 amphibian community* abundance, amphibian assemblage abundance  ProQuest UMI                 7 Oct 2011
                                                                 Dissertations & Theses
-----------------------------------------------------------------------------------------------------------------

Table: Dates, sources, and search terms used to identify possible data sources

### Data Collection

References found by the searches in Table 1 were downloaded. Each article, thesis, and dissertation was then manually scanned to determine if it met the criteria for inclusion in the database. The selection criteria included:

* Data must include quantitative abundances, preferably total number of individuals (no incidence only, i.e., presence-absence, data)
* Data must be for animal data
* Sampling and reporting must be complete (i.e., no data where only a fraction of the community/assemblage was sampled or reported)
* For vertebrate taxa: the majority of species must be fully identified to species
* For invertebrate taxa: the majority of species may did not have to be fully identified to species (due to the number of individuals per sample and the state of taxonomy for the invertebrate groups)
* Data must not be heavily summarized or processed

The following papers remained as data sources based on these criteria: @ref1, @ref2, @ref3, @ref4, @ref5, @ref6, @ref7, @ref8, @ref9, @ref10, @ref11, @ref12, @ref13, @ref14, @ref15, @ref16, @ref17, @ref18, @ref19, @ref20, @ref21, @ref22, @ref23, @ref24, @ref25, @ref26, @ref27, @ref28, @ref29, @ref30, @ref31, @ref32, @ref33, @ref34, @ref35, @ref36, @ref37, @ref38, @ref39, @ref40, @ref41, @ref42, @ref43, @ref44, @ref45, @ref46, @ref47, @ref48, @ref49, @ref50, @ref51, @ref52, @ref53, @ref54, @ref55, @ref56, @ref57, @ref58, @ref59, @ref60, @ref61, @ref62, @ref63, @ref64, @ref65, @ref66, @ref67, @ref68, @ref69, @ref70, @ref71, @ref72, @ref73, @ref74, @ref75, @ref76, @ref77, @ref78, @ref79, @ref80, @ref81, @ref82, @ref83, @ref84, @ref85, @ref86, @ref87, @ref88, @ref89, @ref90, @ref91, @ref92, @ref93, @ref94, @ref95, @ref96, @ref97, @ref98, @ref99, @ref100, @ref101, @ref102, @ref103, @ref104, @ref105, @ref106, @ref107, @ref108, @ref109, @ref110, @ref111, @ref112, @ref113, @ref114, @ref115, @ref116.
Information on these data sources is also available as part of the dataset in the *citations_table_abundances.csv* file.

Data were hand entered into a raw data file as they came from the original source or were extracted from the original source computationally. Data were then manually checked for consistency with the original source. Species names were kept as given in the original source.



### Variables

Variables collected are listed in Table 2.

| Variable name | Variable definition | Units | Storage type | Range of values |
|----------------------|-------------------------------|-------|--------------|-----------------|
| Class | Taxonomic class of species | N/A | Character | N/A |
| Family | Taxonomic family of species | N/A | Character | N/A |
| Genus | Taxonomic genus of species | N/A | Character | N/A |
| Species | Specific epithet of species | N/A | Character | N/A |
| Relative_abundance | Relative abundance of species | N/A | Double | 0 - 309 |
| Abundance | Abundance of species | N/A | Integer | 0-181726 |
| Collection_Year | Start of collecting | N/A | Integer | 1952-2008 |
| End_Collection | End of collecting | N/A | Integer | 1977-2009 |
| Site_Name | Name/description of site | N/A | Character | N/A |
| Biogeographic_region | Biogeographic region | N/A | Character | N/A |
| Site_notes | Additional site information | N/A | Character | N/A |

Table: List of variables collected for each dataset

## Data Records

The data are stored in comma-separated values files using a relational database structure with three separate tables.

### Data files

1. Abundance data: *Species_abundances.csv*
2. Sites data : *Sites_table_abundances.csv*
3. Reference data: *Citations_table_abundances.csv*

### Format and Storage mode

ASCII text, comma delimited, not compressed.

### Header information

1. Class, Family, Genus, Species, Relative_abundance, Abundance, Site_ID, Citation_ID 
2. Site_ID, Collection_Year, End_Collection, Citation_ID, Site_Name, Biogeographic_region, Site_notes
3. Citation_ID, Authors, Yr, Title, Journal, Issue, Pages

### Special characters/fields

Blanks indicate no data: no special characters used.


## Technical Validation

Data have undergone manual quality and assurance checking. Data were entered directly from the source material into the raw data file and values were double checked on entry. Validation of proper downloading and importing of the data can be determined using the following information.

#### Abundance table

1. Number of records, not including header row = 22142
2. Sum of Relative_abundance = 10797.37352
3. Sum of Abundance = 1320592
5. Number of distinct values in species = 1953
5. Number of distinct values in genus = 1262
6. md5 checksum for file = 225508ec2acc8cadd230b5e80446504e

#### Sites table

1. Number of records, not including header row = 706
2. Number of distinct values in collection_year = 48
3. Number of distinct values in biogeographic_region = 6
4. Sum of collection_year = 1378306
5. md5 checksum for file = 9935391079863726d24a9204ea68149d

#### References table

1. Number of records, not including header row = 116
2. Sum of yr = 231916
3. Number of distinct values in journal = 83
4. md5 checksum for file = e42838ee418a44e9e5d33ff99bf96ebb


## Usage Notes

This is compiled data from a variety of literature sources.  Within a study, methods of data collection are the same. However, among studies, even within the same taxonomic grouping, methods of collection, capture success, etc. vary substantially. Because of the methodological variation present in compiled data, it is more appropriate to treat each site individually, rather than aggregating sites across studies for doing things like looking for geographic patterns.  Aggregating data across sites can lead to false signals in species richness, abundance,  etc. that are due to methodological rather than biological/ecological differences.  In addition, some sites also have recorded absences (zeros); in cases where zeros should not be included, data queries should be written accordingly.

The data can be easily downloaded an installed into a variety of database management and programming environments using the EcoData Retriever [@morris2013].

## References

