# Bioproject PRJEB32062

This sample comes from the [NCBI BioProject PRJEB32062](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJEB32062).

# Title:
Lung Microbiome Dynamics in Cystic Fibrosis

_Strain-resolved Dynamics of the Lung Microbiome in Patients with Cystic Fibrosis_

# Description:
In cystic fibrosis, dynamic and complex communities of microbial pathogens and commensals can colonize the lung. Cultured isolates from lung sputum reveal high inter- and intraindividual variability in pathogen strains, sequence variants, and phenotypes; disease progression likely depends on the precise combination of infecting lineages. Routine clinical protocols, however, provide limited overview of the colonizer populations. A more comprehensive and precise identification and characterization of infecting lineages could therefore assist in making corresponding decisions on treatment. Here, we describe longitudinal tracking for four cystic fibrosis patients who exhibited extreme clinical phenotypes and were thus selected from a pilot cohort of eleven patients with repeated sampling for more than a year. Following metagenomics sequencing of lung sputum, we find that the taxonomic identity of individual colonizer lineages can be easily established. Crucially, even superficially clonal pathogens can be subdivided into multiple sub-lineages at the sequence level. By tracking individual allelic differences over time, an assembly-free clustering approach allows us to reconstruct multiple lineage-specific genomes with clear structural differences. Our study showcases a culture-independent shotgun metagenomics approach for longitudinal tracking of sub-lineage pathogen dynamics, opening up the possibility of using such methods to assist in monitoring disease progression through providing high-resolution routine characterization of the cystic fibrosis lung microbiome.


# Metadata:
We have included the metadata in two separate files, a [JSON format file](PRJEB32062.metadata.json.gz) that is computer readable, or a [tsv format file](PRJEB32062.metadata.tsv.gz) that you can import into excel or similar.


# Publications

Dmitrijeva M, Kahlert CR, Feigelman R, Kleiner RL, Nolte O, Albrich WC, Baty F, von Mering C. 2021. Strain-resolved dynamics of the lung microbiome in patients with cystic fibrosis. [MBio 12](https://pmc.ncbi.nlm.nih.gov/articles/PMC8092271/).
  

Mirhakkak MH, Chen X, Ni Y, Heinekamp T, Sae-Ong T, Xu L-L, Kurzai O, Barber AE, Brakhage AA, Boutin S, Scha¤uble S, Panagiotou G. 2023. Genome-scale metabolic modeling of Aspergillus fumigatus strains reveals growth dependencies on the lung microbiome. [Nat Commun 14:4369](https://www.nature.com/articles/s41467-023-39982-5).
  
# Analysis:

- The entire data set is 27 runs, and 113,773,728,053 bp (including amplicon sequences)
- We analysed 25 metagenomic sequence runs.
- We predicted 16 samples out of 25 (64.0%) have _Pseudomonas aeruginosa_


## Prediction outcomes

According to Dmitrijeva _et al.,_ CFR06 does not have _Pseudomonas_, while the others do.

Sample | Pseudomonas Prediction | Confidence | Certainty | pwCF ID
 --- | --- | --- | --- | ---
ERR3274613 | Negative | 0.60 | Low | CFR06
ERR3274614 | Negative | 0.80 | Medium | CFR06
ERR3274615 | Negative | 0.67 | Medium | CFR06
ERR3274616 | Negative | 0.75 | Medium | CFR06
ERR3274617 | Negative | 0.77 | Medium | CFR06
ERR3274618 | Negative | 0.77 | Medium | CFR06
ERR3274619 | Negative | 0.78 | Medium | CFR06
ERR3274620 | Negative | 0.77 | Medium | CFR06
ERR3274621 | Positive | 0.71 | Medium | CFR07
ERR3274622 | Positive | 0.72 | Medium | CFR07
ERR3274623 | Positive | 0.69 | Medium | CFR07
ERR3274624 | Positive | 0.78 | Medium | CFR09
ERR3274625 | Positive | 0.78 | Medium | CFR09
ERR3274626 | Positive | 0.71 | Medium | CFR09
ERR3274627 | Positive | 0.73 | Medium | CFR09
ERR3274628 | Positive | 0.63 | Medium | CFR11
ERR3274629 | Positive | 0.66 | Medium | CFR11
ERR3274630 | Positive | 0.62 | Medium | CFR11
ERR3274631 | Positive | 0.56 | Low | CFR11
ERR3274632 | Positive | 0.55 | Low | CFR11
ERR3274633 | Negative | 0.66 | Medium | CFR11
ERR3274634 | Positive | 0.63 | Medium | CFR11
ERR3274635 | Positive | 0.61 | Medium | CFR11
ERR3274636 | Positive | 0.62 | Medium | CFR11
ERR3274637 | Positive | 0.70 | Medium | CFR11
ERR4661016 |  |  |  | CFR11
ERR4661017 |  |  |  | CFR11

## t-SNE
![Comparison of Adelaide and PRJEB32062 samples by t-SNE](img/PRJEB32062_Pseudomonas_tSNE.png 'Fig. t-SNE of all the analysed sequence data coloured by whether Pseudomonas is predicted')


## PCA
![This cluster of features are most strongly associated with the presence of Pseudomonas](img/PRJEB32062_Pseudomonas_PCA.png 'Fig. PCA of the cluster of features most strongly associated with Pseudomonas colonization in PRJEB32062')



