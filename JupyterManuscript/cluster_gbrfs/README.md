# Autoencoded Data

Most of this data was made by the autoencoder.

The [cluster virulence score](cluster_virulence_score.tsv.gz) was made by matching to the Virulence Factor Database. The Enrichment Score column is an enrichment-based metric (inspired by Fisher's Exact Test)
Instead of raw overlap, it compares the observed number of virulence matches to what would be expected by chance.

Why is this better?
- Accounts for both cluster size and VFDB size.
- Penalizes small clusters if their match rate isn't unusually high.
- Highlights clusters enriched for virulence terms beyond what would happen by random chance.


