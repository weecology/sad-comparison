#Chapter 2- Community abundance data of underrepresented taxonomic groups.

#Abstract
The majority of publicly available datasets used for macroecological research have a North American terrestrial bias, and focus primarily on warm-blooded vertebrates and plants. This dataset helps to improve the availability of data suitable for macroecological questions for less frequently studied taxa. The data were compiled from the literature by focusing on less frequently studied groups, and includes seven classes of animals, amphibians, spiders, beetles, reptiles, birds, and ray finned and cartilaginous fish. The data contains data representing over 2000 species and more than 1.3 million individuals from over 700 sites including locations on all continents except Antarctica.

#Background & Summary
<!-- Background and summary for collecting the data.  Publicly available community datasets suitable for macroecological research mostly birds, trees, mammals, North American focus.  Other taxa also good, compilation with abundances for greater comparisonability across taxa -->
<!-- Why does this data matter, lots of it available for certain taxonomic groups? -->
Comparing macroecological patterns across taxa is a valuable approach for identifying potential pattern-generating mechanisms and determining the generality of a pattern or process.  One major criticism of macroecology is that the majority of research has been driven by a few major datasets, primarily terrestrial North American and European birds and mammals [@beck2012]. In additional, large, publicly available datasets with many sites have been primarily for a single taxa, restricting the majority of macroecological comparisons to a single taxa. One suggestion for improving macroecology is to make better use of existing data [@beck2012]. There is a great deal of community abundance data in the literature, but most include a single to a few communities, and the majority of the data require further processing to be useable in other analyses (i.e., presented in a table in the text of the paper). 
<!-- Why are these data special.  Focus on the taxonomy, cite papers on taxonomic bias in macroecological datasets.  http://www.biodiversity-plants.de/downloads/JD158.pdf -->
This dataset gathers and combines data for multiple taxa and biogeographic regions from the literature into a single, open access, publicly available source.  This will allow researchers to make macroecological comparisons for a wider range of taxa without having to gather and process the data from the literature before use, resulting in more robust comparisons, and a better assessment of generality of pattern and process across taxa and biogeographic regions.  

<!-- Filling in the gaps -->
My compilation is useful because it contains abundance data for seven classes of animal, including vertebrates and invertebrates, endotherms and ectotherms, and includes taxa that are not currently well represented, if at all, in the common macroecological datasets.  This dataset will allow for a more robust comparison of patterns across taxa, especially when combined with existing macroecological datasets.  The primary focus of this dataset was to provide a single source for community abundance data for fish, amphibians and reptiles, as there are currently large publicly available datasets for birds and mammals [e.g., North American Breeding Bird Survey, BBS; @pardieck2014, Mammal Community Database, MCDB; @thibault2011].  While the primary focus of data collection was filling in the gaps for vertebrate taxa,  I also collected community abundance data on other taxa incidentally.  



While the majority of the data is Nearctic, there is a worldwide distribution of sites (Figure 1.)
![Number of sites per biogeographic region.](./sad-data/chapter2/bioregions.png)

![Number of sites per taxon](./sad-data/chapter2/taxa_sites.png)

![Number of individuals per taxon.](./sad-data/chapter2/num_taxa.png)

#Methods
<!-- How data were collected, verified, metadata-->
Data Sources:

Data were compiled from the scientific literature.  References for data sources are presented in a separate file, citations_table_abundances.csv, as well as in the reference section.

<!-- search terms, how I filtered, http://wiki.weecology.org/w/page/36018991/Database--Find unique, add table of sources that I checked but which were ultimately rejected -->
I did an intial quick search of the literature for community abundance data to get a sense of what data were available, and which taxa were likely to have a good amount of data available. After the initial search, I began a more systematic approach to searching through the literature, and selected fish, amphibians, and reptiles as the main focus of data collection. 

| Search Parameters                                                                              | Search engine                        | Date Accessed |
|------------------------------------------------------------------------------------------------|--------------------------------------|---------------|
| community abundance in Biology, Life Sciences, etc.                                           | Google Scholar                       | 29 Nov 2010   |
| fish assemblage abundance, fish community* abundance in Biology, Life Sciences, etc.           | Google Scholar                       | 14 Feb 2011   |
| fish community* abundance, fish assemblage abundance                                           | ProQuest UMI Dissertations & Theses  | 15 Feb 2011   |
| reptile assemblage abundance, reptile community* abundance in Biology, Life Sciences, etc.     | Google Scholar                       | 20 Aug 2011   |
| reptile community* abundance, reptile assemblage abundance                                     | ProQuest UMI Dissertations & Theses  | 21 Aug 2011   |
| amphibian assemblage abundance, amphibian community* abundance in Biology, Life Sciences, etc. | Google Scholar                       | 7 Oct 2011    |
| amphibian community* abundance, amphibian assemblage abundance                                 | ProQuest UMI Dissertations & Theses  | 7 Oct 2011    |

Data Collection
After initial download of the references found by various searches, I manually scanned each article to determine if it met the criteria for inclusion in the database. Selection criteria are as follows:

*Papers with incomplete data (i.e., not all community sampled or reported) excluded

*Papers where the majority of species were poorly identified were excluded for vertebrate taxa, but not for invertebrate taxa, due to the number of individuals per sample and the state of taxonomy for the invertebrate groups.

*Papers with incidence (presence-absence) only data excluded.

*Papers with heavily summarized or processed data excluded.

*Must have quantitative abundances, preferably total number of individuals.

*Must be animal data.


Data were hand entered into a raw data file as they came from the original source or extracted from the original source computationally and then manually checked for consistency with the original source.  All the references initially collected were not included in the final database, because they were not deemed suitable for inclusion in the final product.

Species names were kept as given in the original source.  

 
Variables:

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

#Data Records
The data are presented here in the following files: 
 
Abundance data: Species_abundances.csv

Reference file: Citations_table_abundances.csv

Sites data file : Sites_table_abundances.csv
    

#Technical Validation
<!--Validation and figures (breakdown of data by taxa, etc.)-->
Data have undergone initial quality and assurance checking.  Data were entered directly from the source material into the raw data file and values were double checked on entry.  
  

Identity:

1. Abundance data: Species_abundances.csv

2. Sites data file : Sites_table_abundances.csv

3. Reference file: Citations_table_abundances.csv

 

Size:

1. 22143 records, including header row.

2. 707 records, including header row.

3. 117 records, including header row.

     
Format and Storage mode:

ASCII text, comma delimited, not compressed.


Header information:

1. Class, Family, Genus, Species, Relative_abundance, Abundance, Site_ID, Citation_ID 

2. Site_ID, Collection_Year, End_Collection, Citation_ID, Site_Name, Biogeographic_region, Site_notes


3. Citation_ID, Authors, Yr, Title, Journal, Issue, Pages


Special characters/fields:

Blanks indicate no data: no special characters used.

 

Authentication procedures:

1. Sum of Relative_abundance = 10797.37352
	
   Sum of Abundance = 1320592

#Usage Notes
<!-- Best practices for using the data, EcoData Retriever compatible.  -->
This is compiled data from a variety of literature sources.  Within a study, methods of data collection are the same.  However, among studies within the same taxonomic grouping, methods of collection, capture success, etc. vary, and the differences among taxa are even greater.  Because of the methodological variation present in compiled data, it is more appropriate to treat each site individually, rather than aggregating sites across studies.  Aggregating data across sites can lead to false signals in species richness, abundance,  etc. that are due to methodological rather than biological/ecological differences.  <!--Why should these be done one at a time  (methods aren't the same, why this is important)-->  

#References

