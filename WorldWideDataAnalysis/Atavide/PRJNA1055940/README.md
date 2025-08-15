# Bioproject PRJNA1055940

This sample comes from the [NCBI BioProject PRJNA1055940](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA1055940).

# Title:
Microbiome analysis in the respiratory tract of individuals with cystic fibrosis and non-cystic fibrosis bronchiectasis

# Description:
This study aimed to analyze the differences in the lungs and nasopharyngeal microbiome among three groups: Cystic fibrosis, non-cystic fibrosis bronchiectasis, and healthy subjects.

Background
Bronchiectasis is a condition characterized by abnormal and irreversible bronchial dilation resulting from lung tissue damage and can be categorized into two main groups: cystic fibrosis (CF) and non-CF bronchiectasis (NCFB). Both diseases are marked by recurrent infections, inflammatory exacerbations, and lung damage. Given that infections are the primary drivers of disease progression, characterization of the respiratory microbiome can shed light on compositional alterations and susceptibility to antimicrobial drugs in these cases compared to healthy individuals.

Methods
To assess the microbiota in the two studied diseases, 35 subjects were recruited, comprising 10 NCFB and 13 CF patients and 12 healthy individuals. Nasopharyngeal swabs and induced sputum were collected, and total DNA was extracted. The DNA was then sequenced by the shotgun method and evaluated using the SqueezeMeta pipeline and R.

Results
We observed reduced species diversity in both disease cohorts, along with distinct microbial compositions and profiles of antimicrobial resistance genes, compared to healthy individuals. The nasopharynx exhibited a consistent microbiota composition across all cohorts. Enrichment of members of the Burkholderiaceae family and an increased Firmicutes/Bacteroidetes ratio in the CF cohort emerged as key distinguishing factors compared to NCFB group. Staphylococcus aureus and Prevotella shahii also presented differential abundance in the CF and NCFB cohorts, respectively, in the lower respiratory tract. Considering antimicrobial resistance, a high number of genes related to antibiotic efflux were detected in both disease groups, which correlated with the patient’s clinical data.

Conclusions
Bronchiectasis is associated with reduced microbial diversity and a shift in microbial and resistome composition compared to healthy subjects. Despite some similarities, CF and NCFB present significant differences in microbiome composition and antimicrobial resistance profiles, suggesting the need for customized management strategies for each disease.

# Metadata:
We have included the metadata in two separate files, a [JSON format file](PRJNA1055940.metadata.json.gz) that is computer readable, or a [tsv format file](PRJNA1055940.metadata.tsv.gz) that you can import into excel or similar.

# Publications


Motta H, Reuwsaat JCV, Lopes FC, Viezzer G, Volpato FCZ, Barth AL, de Tarso Roth Dalcin P, Staats CC, Vainstein MH, Kmetzsch L. 2024. Comparative microbiome analysis in cystic fibrosis and non-cystic fibrosis bronchiectasis. [Respir Res 25:211](https://pmc.ncbi.nlm.nih.gov/articles/PMC11102160/).
  
# Analysis:

- The entire data set is 61 runs, and 386,942,064,540 bp (including amplicon sequences)
- We analysed 61 metagenomic sequence runs.
- We predicted 9 samples out of 61 (14.8%) have _Pseudomonas aeruginosa_



<details>
<summary>
A comparison of our predictions with the published analysis shows that we correctly identified many of the positive cases, and the cases that we incorrectly identified have marginal read abundance in the sample.

</summary>

Original ID | Type | Sample | Number of Pseudomonas reads reported in SOM | Cultured | Pseudomonas Prediction | Confidence | Certainty | Result | Reason
--- | --- | --- | --- | --- | --- | --- | --- | --- | ---
be_01 | human induced sputum | SRR27326975 | 17,545 |  | Negative | 0.51 | Low | Correct | 
be_01 | human nasopharyngeal swab | SRR27326950 | 558 |  | Negative | 0.72 | Medium | Correct | 
be_02 | human induced sputum | SRR27326974 | 55 |  | Negative | 0.81 | High | Correct | 
be_03 | human induced sputum | SRR27326963 | 135,805 | _P. aeruginosa_ | Positive | 0.76 | Medium | Correct | 
be_03 | human nasopharyngeal swab | SRR27326949 | 166,746 | _P. aeruginosa_ | Positive | 0.67 | Medium | Correct | 
be_04 | human induced sputum | SRR27326952 | 52,813 | _P. aeruginosa_ | Positive | 0.62 | Medium | Correct | 
be_04 | human nasopharyngeal swab | SRR27326948 | 9,049 | _P. aeruginosa_ | Positive | 0.55 | Low | Correct | 
be_05 | human induced sputum | SRR27326932 | 257 | _P. aeruginosa_, _S. aureus_ | Negative | 0.72 | Medium | Incorrect | Low read abundance
be_05 | human nasopharyngeal swab | SRR27326938 | 194 | _P. aeruginosa_, _S. aureus_ | Negative | 0.81 | High | Incorrect | Low read abundance
be_06 | human induced sputum | SRR27326921 | 85 | _P. aeruginosa_, _S. aureus_ | Negative | 0.74 | Medium | Incorrect | Low read abundance
be_06 | human nasopharyngeal swab | SRR27326937 | 147 | _P. aeruginosa_, _S. aureus_ | Negative | 0.67 | Medium | Incorrect | Low read abundance
be_07 | human induced sputum | SRR27326943 | 6,627 | _P. aeruginosa_, _Achromobacter_ sp. | Negative | 0.62 | Medium | Incorrect | Marginal
be_07 | human nasopharyngeal swab | SRR27326936 | 210 | _P. aeruginosa_, _Achromobacter_ sp. | Negative | 0.72 | Medium | Incorrect | Low read abundance
be_08 | human induced sputum | SRR27326941 | 261 | _P. aeruginosa_ | Negative | 0.7 | Medium | Incorrect | Low read abundance
be_08 | human nasopharyngeal swab | SRR27326935 | 173 | _P. aeruginosa_ | Negative | 0.75 | Medium | Incorrect | Low read abundance
be_09 | human induced sputum | SRR27326940 | 144 |  | Negative | 0.55 | Low | Correct | 
be_09 | human nasopharyngeal swab | SRR27326934 | 552 |  | Negative | 0.64 | Medium | Correct | 
be_10 | human nasopharyngeal swab | SRR27326933 | 124 |  | Negative | 0.84 | Hig | Correct | 
cf_01 | human induced sputum | SRR27326939 | 1,197 | _P. aeruginosa_, _S. aureus_ | Negative | 0.68 | Medium | Incorrect | Low read abundance
cf_02 | human induced sputum | SRR27326973 | 112 | _P. aeruginosa_, _S. aureus_ | Negative | 0.67 | Medium | Incorrect | Low read abundance
cf_02 | human nasopharyngeal swab | SRR27326930 | 198 | _P. aeruginosa_, _S. aureus_ | Negative | 0.7 | Medium | Incorrect | Low read abundance
cf_03 | human induced sputum | SRR27326972 | 553,062 | _P. aeruginosa_, _S. aureus_ | Positive | 0.8 | High | Correct | 
cf_04 | human induced sputum | SRR27326971 | 59 |  | Negative | 0.79 | Medium | Correct | 
cf_04 | human nasopharyngeal swab | SRR27326928 | 107 |  | Negative | 0.68 | Medium | Correct | 
cf_05 | human induced sputum | SRR27326970 | 179,447 | _P. aeruginosa_, _S. aureus_ | Positive | 0.72 | Medium | Correct | 
cf_05 | human nasopharyngeal swab | SRR27326927 | 61,591 | _P. aeruginosa_, _S. aureus_ | Positive | 0.53 | Low | Correct | 
cf_06 | human induced sputum | SRR27326969 | 2,451 | _P. aeruginosa_, _S. aureus_, _B. cepacia_ | Negative | 0.51 | Low | Incorrect | Low read abundance
cf_06 | human nasopharyngeal swab | SRR27326926 | 1,438 | _P. aeruginosa_, _S. aureus_, _B. cepacia_ | Negative | 0.55 | Low | Incorrect | Low read abundance
cf_07 | human induced sputum | SRR27326968 | 89 | _S. aureus_ | Negative | 0.78 | Medium | Correct | 
cf_07 | human nasopharyngeal swab | SRR27326925 | 5,302 | _S. aureus_ | Negative | 0.54 | Low | Correct | 
cf_08 | human induced sputum | SRR27326967 | 1,270 | _P. aeruginosa_, _B. cepacia_ | Negative | 0.7 | Medium | Incorrect | 
cf_08 | human nasopharyngeal swab | SRR27326924 | 252 | _P. aeruginosa_, _B. cepacia_ | Negative | 0.77 | Medium | Incorrect | 
cf_09 | human induced sputum | SRR27326966 | 1,962 | _B. cepacia_ | Negative | 0.53 | Low | Correct | 
cf_09 | human nasopharyngeal swab | SRR27326923 | 250 | _B. cepacia_ | Negative | 0.76 | Medium | Correct | 
cf_10 | human induced sputum | SRR27326965 | 303,849 | _P. aeruginosa_ | Positive | 0.67 | Medium | Correct | 
cf_10 | human nasopharyngeal swab | SRR27326922 | 112,810 | _P. aeruginosa_ | Positive | 0.71 | Medium | Correct | 
cf_11 | human induced sputum | SRR27326953 | 4,060 |  | Negative | 0.51 | Low | Correct | 
cf_11 | human nasopharyngeal swab | SRR27326942 | 374 |  | Negative | 0.55 | Low | Correct | 
cf_12 | human nasopharyngeal swab | SRR27326931 | 268 | _H. influenzae_ | Negative | 0.73 | Medium | Correct | 
cf_13 | human nasopharyngeal swab | SRR27326929 | 414 | _P. aeruginosa_, _S. aureus_ | Negative | 0.61 | Medium | Incorrect | 
ht_01 | human induced sputum | SRR27326964 | 1,795 |  | Negative | 0.54 | Low | Correct | 
ht_01 | human nasopharyngeal swab | SRR27326920 | 173 |  | Negative | 0.75 | Medium | Correct | 
ht_02 | human induced sputum | SRR27326962 | 485 |  | Negative | 0.64 | Medium | Correct | 
ht_02 | human nasopharyngeal swab | SRR27326919 | 162 |  | Negative | 0.72 | Medium | Correct | 
ht_03 | human induced sputum | SRR27326961 | 216 |  | Negative | 0.72 | Medium | Correct | 
ht_04 | human induced sputum | SRR27326960 | 135 |  | Negative | 0.72 | Medium | Correct | 
ht_04 | human nasopharyngeal swab | SRR27326917 | 259 |  | Negative | 0.74 | Medium | Correct | 
ht_05 | human induced sputum | SRR27326959 | 73 |  | Negative | 0.71 | Medium | Correct | 
ht_05 | human nasopharyngeal swab | SRR27326916 | 480 |  | Negative | 0.62 | Medium | Correct | 
ht_06 | human induced sputum | SRR27326958 | 100 |  | Negative | 0.73 | Medium | Correct | 
ht_06 | human nasopharyngeal swab | SRR27326915 | 290 |  | Negative | 0.71 | Medium | Correct | 
ht_07 | human induced sputum | SRR27326957 | 542 |  | Negative | 0.73 | Medium | Correct | 
ht_07 | human nasopharyngeal swab | SRR27326947 | 125 |  | Negative | 0.8 | Medium | Correct | 
ht_08 | human induced sputum | SRR27326956 | 367 |  | Negative | 0.7 | Medium | Correct | 
ht_08 | human nasopharyngeal swab | SRR27326946 | 796 |  | Negative | 0.64 | Medium | Correct | 
ht_09 | human induced sputum | SRR27326955 | 146 |  | Negative | 0.66 | Medium | Correct | 
ht_09 | human nasopharyngeal swab | SRR27326945 | 352 |  | Negative | 0.65 | Medium | Correct | 
ht_10 | human induced sputum | SRR27326954 | 568 |  | Negative | 0.61 | Medium | Correct | 
ht_10 | human nasopharyngeal swab | SRR27326944 | 102 |  | Negative | 0.77 | Medium | Correct | 
ht_11 | human induced sputum | SRR27326951 | 2,594 |  | Negative | 0.62 | Medium | Correct | 
ht_12 | human nasopharyngeal swab | SRR27326918 | 139 |  | Negative | 0.71 | Medium | Correct | 

</details>

<details>
<summary>
## Prediction outcomes
</summary>

Sample | Pseudomonas Prediction | Confidence | Certainty
 --- | --- | --- | ---
SRR27326915 | Negative | 0.71 | Medium
SRR27326916 | Negative | 0.62 | Medium
SRR27326917 | Negative | 0.74 | Medium
SRR27326918 | Negative | 0.71 | Medium
SRR27326919 | Negative | 0.72 | Medium
SRR27326920 | Negative | 0.75 | Medium
SRR27326921 | Negative | 0.74 | Medium
SRR27326922 | Positive | 0.71 | Medium
SRR27326923 | Negative | 0.76 | Medium
SRR27326924 | Negative | 0.77 | Medium
SRR27326925 | Negative | 0.54 | Low
SRR27326926 | Negative | 0.55 | Low
SRR27326927 | Positive | 0.53 | Low
SRR27326928 | Negative | 0.68 | Medium
SRR27326929 | Negative | 0.61 | Medium
SRR27326930 | Negative | 0.70 | Medium
SRR27326931 | Negative | 0.73 | Medium
SRR27326932 | Negative | 0.72 | Medium
SRR27326933 | Negative | 0.84 | High
SRR27326934 | Negative | 0.64 | Medium
SRR27326935 | Negative | 0.75 | Medium
SRR27326936 | Negative | 0.72 | Medium
SRR27326937 | Negative | 0.67 | Medium
SRR27326938 | Negative | 0.81 | High
SRR27326939 | Negative | 0.68 | Medium
SRR27326940 | Negative | 0.55 | Low
SRR27326941 | Negative | 0.70 | Medium
SRR27326942 | Negative | 0.55 | Low
SRR27326943 | Negative | 0.62 | Medium
SRR27326944 | Negative | 0.77 | Medium
SRR27326945 | Negative | 0.65 | Medium
SRR27326946 | Negative | 0.64 | Medium
SRR27326947 | Negative | 0.80 | Medium
SRR27326948 | Positive | 0.55 | Low
SRR27326949 | Positive | 0.67 | Medium
SRR27326950 | Negative | 0.72 | Medium
SRR27326951 | Negative | 0.62 | Medium
SRR27326952 | Positive | 0.62 | Medium
SRR27326953 | Negative | 0.51 | Low
SRR27326954 | Negative | 0.61 | Medium
SRR27326955 | Negative | 0.66 | Medium
SRR27326956 | Negative | 0.70 | Medium
SRR27326957 | Negative | 0.73 | Medium
SRR27326958 | Negative | 0.73 | Medium
SRR27326959 | Negative | 0.71 | Medium
SRR27326960 | Negative | 0.72 | Medium
SRR27326961 | Negative | 0.72 | Medium
SRR27326962 | Negative | 0.64 | Medium
SRR27326963 | Positive | 0.76 | Medium
SRR27326964 | Negative | 0.54 | Low
SRR27326965 | Positive | 0.67 | Medium
SRR27326966 | Negative | 0.53 | Low
SRR27326967 | Negative | 0.70 | Medium
SRR27326968 | Negative | 0.78 | Medium
SRR27326969 | Negative | 0.51 | Low
SRR27326970 | Positive | 0.72 | Medium
SRR27326971 | Negative | 0.79 | Medium
SRR27326972 | Positive | 0.80 | High
SRR27326973 | Negative | 0.67 | Medium
SRR27326974 | Negative | 0.81 | High
SRR27326975 | Negative | 0.51 | Low

</details>

## t-SNE
![Comparison of Adelaide and PRJNA1055940 samples by t-SNE](img/PRJNA1055940_Pseudomonas_tSNE.png 'Fig. t-SNE of all the analysed sequence data coloured by whether Pseudomonas is predicted')


## PCA
![This cluster of features are most strongly associated with the presence of Pseudomonas](img/PRJNA1055940_Pseudomonas_PCA.png 'Fig. PCA of the cluster of features most strongly associated with Pseudomonas colonization in PRJNA1055940')


