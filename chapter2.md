#Chapter 2

#Abstract
<!--  Number of taxa, number of communities -->Ray finned and cartilaginous fish, amphibians, spiders, birds, beetles, reptiles from 706 sites over all continents except Antarctica.


#Background & Summary
<!-- Background and summary for collecting the data.  Publicly available community datasets suitable for macroecological research mostly birds, trees, mammals, North American focus.  Other taxa also good, compilation with abundances for greater comparisonability across taxa -->
Small number of large, publicly available datasets that have been used extensively for macroecological comparisons/analysis, North American bias, birds, trees.  Lots of data in the literature, but the majority of compilations have not been made publicly available.  My compilation is useful because it allows for comparison of patterns across taxa.  

#Methods
<!-- How data were collected, verified, metadata-->
Data Sources:

Data were compiled from the scientific literature.  References for data sources are presented in a separate file, citations_table_abundances.csv, as well as in the reference section.

 

Data Collection

Data were hand entered into a raw data file as they came from the original source or extracted from the original source computationally and then manually checked for consistency with the original source.  All the data initially collected were not included in the final database, because they were not deemed suitable for inclusion in the final product.

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
This is compiled data from a variety of literature sources.  Because of the nature of this data, it is more appropriate to treat each site individually, rather than aggregating sites.  

#References

