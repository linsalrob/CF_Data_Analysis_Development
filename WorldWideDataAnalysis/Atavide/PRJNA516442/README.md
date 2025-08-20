# Bioproject PRJNA516442

This sample comes from the [NCBI BioProject PRJNA516442](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA516442).

# Title:
Depletion of human DNA from complex clinical samples for metagenomic sequencing

# Description:
Metagenomic sequencing is a promising approach for identifying and characterizing organisms and their functional characteristics in complex, polymicrobial infections, such as airway infections in people with cystic fibrosis. These analyses are often hampered, however, by overwhelming quantities of human DNA, yielding only a small proportion of microbial reads for analysis. Additionally, many abundant microbes in respiratory samples can produce large quantities of extracellular bacterial DNA originating either from biofilms or dead cells. This study describes a method for simultaneously depleting DNA from intact human cells and extracellular DNA (human and bacterial) in sputum, using selective lysis of eukaryotic cells and endonuclease digestion. This method increases microbial sequencing depth and, consequently, both the number of taxa detected and coverage of individual genes such as those involved in antibiotic resistance, underscoring the substantial impact of DNA from sources other than live bacteria in microbiological analyses of complex, chronic infection specimens.

# Organisation:
University of Washington

# Metadata:
We have included the metadata in two separate files, a [JSON format file](PRJNA516442.metadata.json.gz) that is computer readable, or a [tsv format file](PRJNA516442.metadata.tsv.gz) that you can import into excel or similar.

Note: These sequences are too short, we have processed some but not all.

# Publications

Nelson MT, Pope CE, Marsh RL, Wolter DJ, Weiss EJ, Hager KR, Vo AT, Brittnacher MJ, Radey MC, Hayden HS, Eng A, Miller SI, Borenstein E, Hoffman LR. 2019. Human and extracellular DNA depletion for metagenomic analysis of complex clinical infection samples yields optimized viable microbiome profiles. [Cell Rep 26:2227-2240.e5](https://pmc.ncbi.nlm.nih.gov/articles/PMC6435281/).

# Analysis:

- The entire data set is 93 runs, and 34,371,719,753 bp (including amplicon sequences)
- We analysed 15 metagenomic sequence runs.
- We predicted 8 samples out of 15 (53.3%) have _Pseudomonas aeruginosa_


## Prediction outcomes

Sample | Pseudomonas Prediction | Confidence | Certainty
 --- | --- | --- | ---
SRR8731680 | Positive | 0.70 | Medium
SRR8731681 | Positive | 0.68 | Medium
SRR8731682 | Negative | 0.74 | Medium
SRR8731683 | Positive | 0.66 | Medium
SRR8731684 | Negative | 0.66 | Medium
SRR8731685 | Positive | 0.66 | Medium
SRR8731686 | Positive | 0.65 | Medium
SRR8731687 | Negative | 0.62 | Medium
SRR8731688 | Positive | 0.72 | Medium
SRR8731689 | Negative | 0.65 | Medium
SRR8731690 | Negative | 0.65 | Medium
SRR8731691 | Positive | 0.59 | Low
SRR8731692 | Positive | 0.63 | Medium
SRR8731693 | Negative | 0.79 | Medium
SRR8731694 | Negative | 0.54 | Low


## t-SNE
![Comparison of Adelaide and PRJNA516442 samples by t-SNE](img/PRJNA516442_Pseudomonas_tSNE.png 'Fig. t-SNE of all the analysed sequence data coloured by whether Pseudomonas is predicted')


## PCA
![This cluster of features are most strongly associated with the presence of Pseudomonas](img/PRJNA516442_Pseudomonas_PCA.png 'Fig. PCA of the cluster of features most strongly associated with Pseudomonas colonization in PRJNA516442')


