# Bioproject PRJNA71831

This sample comes from the [NCBI BioProject PRJNA71831](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA71831).

# Title:
Viral and Microbial Cystic Fibrosis Lung Metagenome


# Description:
CF patients undergo recurrent pulmonary exacerbations. Prognosis and treatment regimes are entirely based on clinical examinations and culture results. Patients are typically treated with a common set of IV antibiotics during pulmonary exacerbations. In addition to the improvement in lung function, the eradication of "pathogenic" microbes based on microbe-targeted assays serves as an indicator of recovery. However, there is often little correlation between the beneficial outcome and the clearance of the infection. The goal of this study is to generate a set of metagenomes and metatranscriptomes from each patient to characterize the microbial and viral communities in CF lungs associated with different perturbations, such as during exacerbations and following antibiotic treatments. Expectorated sputum samples were collected from Cystic Fibrosis individuals.

# Organisation:
San Diego State University


# Metadata:
We have included the metadata in two separate files, a [JSON format file](PRJNA71831.metadata.json.gz) that is computer readable, or a [tsv format file](PRJNA71831.metadata.tsv.gz) that you can import into excel or similar.

# Publications


Lim YW, Schmieder R, Haynes M, Willner D, Furlan M, Youle M, Abbott K, Edwards R, Evangelista J, Conrad D, Rohwer F. 2013. Metagenomics and metatranscriptomics: windows on CF-associated viral and microbial communities. [J Cyst Fibros 12:154-164](https://doi.org/10.1016/j.jcf.2012.07.009).
  
# Analysis:


- The entire data set is 38 runs, and 1,179,409,307 bp (including amplicon sequences)
- We analysed 21 metagenomic sequence runs.
- We predicted 4 samples out of 21 (19.0%) have _Pseudomonas aeruginosa_


## Prediction outcomes

Sample | Pseudomonas Prediction | Confidence | Certainty
 --- | --- | --- | ---
SRR1177382 | Positive | 0.57 | Low
SRR1177387 | Negative | 0.70 | Medium
SRR1180012 | Negative | 0.55 | Low
SRR1180013 | Positive | 0.66 | Medium
SRR606445 | Negative | 0.68 | Medium
SRR610353 | Negative | 0.77 | Medium
SRR610359 | Negative | 0.71 | Medium
SRR610360 | Negative | 0.81 | High
SRR610361 | Positive | 0.52 | Low
SRR610365 | Negative | 0.66 | Medium
SRR610366 | Positive | 0.54 | Low
SRR610547 | Negative | 0.69 | Medium
SRR610548 | Negative | 0.83 | High
SRR610549 | Negative | 0.87 | High
SRR610550 | Negative | 0.75 | Medium
SRR610551 | Negative | 0.77 | Medium
SRR610552 | Negative | 0.78 | Medium
SRR610553 | Negative | 0.71 | Medium
SRR610554 | Negative | 0.64 | Medium
SRR610555 | Negative | 0.53 | Low
SRR610556 | Negative | 0.71 | Medium


## t-SNE
![Comparison of Adelaide and PRJNA71831 samples by t-SNE](img/PRJNA71831_Pseudomonas_tSNE.png 'Fig. t-SNE of all the analysed sequence data coloured by whether Pseudomonas is predicted')


## PCA
![This cluster of features are most strongly associated with the presence of Pseudomonas](img/PRJNA71831_Pseudomonas_PCA.png 'Fig. PCA of the cluster of features most strongly associated with Pseudomonas colonization in PRJNA71831')


