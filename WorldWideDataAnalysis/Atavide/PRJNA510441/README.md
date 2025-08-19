# Bioproject PRJNA510441

This sample comes from the [NCBI BioProject PRJNA510441](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA510441).

# Title:
Cystic fibrosis case studies

# Description:
Time series of patients with cystic fibrosis


# Metadata:
We have included the metadata in two separate files, a [JSON format file](PRJNA510441.metadata.json.gz) that is computer readable, or a [tsv format file](PRJNA510441.metadata.tsv.gz) that you can import into excel or similar.

# Publications

Silveira CB, Cobián-Güemes AG, Uranga C, Baker JL, Edlund A, Rohwer F, Conrad D. 2021. Multi-Omics Study of Keystone Species in a Cystic Fibrosis Microbiome. [Int J Mol Sci 22](https://pubmed.ncbi.nlm.nih.gov/34769481/).
  
# Analysis:


- The entire data set is 14 runs, and 906,511,907 bp (including amplicon sequences)
- We analysed 14 metagenomic sequence runs.
- We predicted 5 samples out of 14 (35.7%) have _Pseudomonas aeruginosa_

We don't do very well with the predictions here, and it doesn't make sense why. Both the levels of _Pseudomonas_ associated clusters, and _Pseudomonas_ itself are very high, and we should be able to predict them.



## Prediction outcomes

Sample | Pseudomonas Prediction | Confidence | Certainty
 --- | --- | --- | ---
SRR8334087 | Negative | 0.69 | Medium
SRR8334088 | Negative | 0.50 | Low
SRR8334089 | Positive | 0.67 | Medium
SRR8334090 | Positive | 0.70 | Medium
SRR8334091 | Negative | 0.69 | Medium
SRR8334092 | Negative | 0.57 | Low
SRR8334093 | Positive | 0.66 | Medium
SRR8334094 | Negative | 0.60 | Low
SRR8334095 | Negative | 0.63 | Medium
SRR8334096 | Negative | 0.62 | Medium
SRR8334097 | Negative | 0.53 | Low
SRR8334098 | Negative | 0.51 | Low
SRR8334099 | Positive | 0.57 | Low
SRR8334100 | Positive | 0.62 | Medium

# Comparison of our predictions to the reported clinical data


Day | Status | Bacteria | Fungi | SRA Run ID | Original Sample ID | Our Predictions | Our Score | Our confidence
--- | --- | --- | --- | --- | --- | --- | --- | --- 
724 |  |  |  | SRR8334088 | CF01mgD724 | Negative | 0.5 | Low
723 |  |  |  | SRR8334087 | CF01mgD723 | Negative | 0.69 | Medium
722 |  |  |  | SRR8334090 | CF01mgD722 | Positive | 0.7 | Medium
721 |  |  |  | SRR8334089 | CF01mgD721 | Positive | 0.67 | Medium
720 |  |  |  | SRR8334100 | CF01mgD720 | Positive | 0.62 | Medium
719 | exacerbation | Pseudomonas aeruginosa, Pseudomonas fluorescens | Yeast, Aspergillus fumigatus | SRR8334099 | CF01mgD719 | Positive | 0.57 | Low
718 |  |  |  | SRR8334092 | CF01mgD718 | Negative | 0.57 | Low
674 | stable | Pseudomonas aeruginosa |  |  |  |  |  | 
547 | stable | Pseudomonas aeruginosa | Yeast |  |  |  |  | 
540 | stable | Pseudomonas aeruginosa | Yeast |  |  |  |  | 
414 | stable | Pseudomonas aeruginosa | Yeast |  |  |  |  | 
409 |  |  |  | SRR8334091 | CF01mgD409 | Negative | 0.69 | Medium
373 | stable | Pseudomonas aeruginosa | Yeast |  |  |  |  | 
286 |  |  |  | SRR8334094 | CF01mgD286 | Negative | 0.6 | Low
279 |  |  |  | SRR8334096 | CF01Dmt303 | Negative | 0.62 | Medium
279 |  |  |  | SRR8334095 | CF01mtD279 | Negative | 0.63 | Medium
204 | exacerbation | Pseudomonas aeruginosa, Stenotrophomonas maltophilia | Yeast |  |  |  |  | 
192 | exacerbation | Pseudomonas aeruginosa, Stenotrophomonas maltophilia | Yeast, Aspergillus terreus |  |  |  |  | 
48 | stable | Pseudomonas aeruginosa, Stenotrophomonas maltophilia, Enterobacter cloacae | Yeast |  |  |  |  | 
24 | exacerbation | Pseudomonas aeruginosa, Enterobacter cloacae | Yeast |  |  |  |  | 
14 | exacerbation | Pseudomonas aeruginosa | Yeast |  |  |  |  | 
8 |  |  |  | SRR8334098 | CF01mtD8 | Negative | 0.51 | Low
8 |  |  |  | SRR8334093 | CF01mgD8 | Positive | 0.66 | Medium
7 | exacerbation | Pseudomonas aeruginosa, Stenotrophomonas maltophilia | Yeast | SRR8334097 | CF01mtD7 | Negative | 0.53 | Low
1 | exacerbation | Pseudomonas aeruginosa, Stenotrophomonas maltophilia |  |  |  |  |  | 
0 | exacerbation | Pseudomonas aeruginosa, Stenotrophomonas maltophilia | Aspergillus terreus |  |  |  |  | 


## t-SNE
![Comparison of Adelaide and PRJNA510441 samples by t-SNE](img/PRJNA510441_Pseudomonas_tSNE.png 'Fig. t-SNE of all the analysed sequence data coloured by whether Pseudomonas is predicted')


## PCA
![This cluster of features are most strongly associated with the presence of Pseudomonas](img/PRJNA510441_Pseudomonas_PCA.png 'Fig. PCA of the cluster of features most strongly associated with Pseudomonas colonization in PRJNA510441')


