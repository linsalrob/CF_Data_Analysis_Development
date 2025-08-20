# Bioproject PRJNA316588

This sample comes from the [NCBI BioProject PRJNA316588](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA316588).

# Title:
Human lung metagenome

_Sputum Metagenome Of CF, COPD, Smokers And Healthy Subjects_

# Description:
Sputum samples were collected from healthy smokers and non-smoking individuals, Cystic Fibrosis and Chronic Obstructive Pulmonary Disease patients. DNA was extracted from these samples without any prior removal of human DNA and the samples were whole genome shotgun sequenced foracquiring an unbiased qualitative view of the microbial community present in thedifferent lungs.


# Metadata:
We have included the metadata in two separate files, a [JSON format file](PRJNA316588.metadata.json.gz) that is computer readable, or a [tsv format file](PRJNA316588.metadata.tsv.gz) that you can import into excel or similar.

# Publications

Feigelman R, Kahlert CR, Baty F, Rassouli F, Kleiner RL, Kohler P, Brutsche MH, von Mering C. 2017. Sputum DNA sequencing in cystic fibrosis: non-invasive access to the lung microbiome and to pathogen details. [Microbiome 5:20](https://doi.org/10.1186/s40168-017-0234-1).
  
# Analysis:

- The entire data set is 18 runs, and 121,257,187,412 bp (including amplicon sequences)
- We analysed 17 metagenomic sequence runs.
- We predicted 2 samples out of 17 (11.8%) have _Pseudomonas aeruginosa_

_We **correctly** predicted the _Pseudomonas aeruginosa_ colonisation of all of these samples.

## Prediction outcomes

Sample | Pseudomonas Prediction | Confidence | Certainty | Reported clinically relevant bacteria
 --- | --- | --- | --- | ---
SRR5109913 | Negative | 0.65 | Medium | _Staphylococcus aureus_, _Achromobacter xylosoxidans_
SRR5109957 | Positive | 0.67 | Medium | _Pseudomonas aeruginosa_
SRR5109959 | Positive | 0.63 | Medium | _Pseudomonas aeruginosa_
SRR5109960 | Negative | 0.84 | High | _Staphylococcus aureus_
SRR5109961 | Negative | 0.71 | Medium | _Stenotrophomonas maltophilia_, _Haemophilus influenzae_
SRR5110005 | Negative | 0.81 | High | _Staphylococcus aureus_
SRR5110496 | Negative | 0.79 | Medium | _Staphylococcus aureus_
SRR5110508 | Negative | 0.86 | High | 
SRR5110517 | Negative | 0.85 | High | 
SRR5110523 | Negative | 0.78 | Medium | 
SRR5110531 | Negative | 0.69 | Medium | 
SRR5110535 | Negative | 0.68 | Medium | 
SRR5110576 | Negative | 0.76 | Medium | 
SRR5110588 | Negative | 0.74 | Medium | 
SRR5110763 | Negative | 0.86 | High | 
SRR5110777 | Negative | 0.77 | Medium | 
SRR5110789 | Negative | 0.70 | Medium | 


## t-SNE
![Comparison of Adelaide and PRJNA316588 samples by t-SNE](img/PRJNA316588_Pseudomonas_tSNE.png 'Fig. t-SNE of all the analysed sequence data coloured by whether Pseudomonas is predicted')


## PCA
![This cluster of features are most strongly associated with the presence of Pseudomonas](img/PRJNA316588_Pseudomonas_PCA.png 'Fig. PCA of the cluster of features most strongly associated with Pseudomonas colonization in PRJNA316588')


