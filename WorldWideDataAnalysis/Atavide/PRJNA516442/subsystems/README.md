# Subsystem counts for Bioproject PRJNA516442

This sample comes from the [NCBI BioProject PRJNA516442](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA516442).

Subsystems were generated using [atavide_lite](https://github.com/linsalrob/atavide_lite).



# NORMALIZATIONS

Currently we perform three normalizations:

1. \*\_raw.tsv

This is the non-normalised data, so just the raw counts. For each sequence, if it appears in one subsystem we incremenet that count by 1, but if it occurs in more than one subsystem, we increment that count by 1/n (1/2 for 2 subsystems, 1/3 for 3 subsystems, etc).

2. \*\_norm\_all.tsv

This data is normalised for _all_ reads, regardless of whether they are in a subsystem or not. This makes smaller numbers. 

3. \*\_norm\_ss.tsv

This data is normalised only to the number of reads that match to subsystems, so if there is a lot of other stuff we ignore it.


