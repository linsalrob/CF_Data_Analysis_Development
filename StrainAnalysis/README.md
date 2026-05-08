# Extracting genotypes from metagenomes.


We have created MAGs, so now lets map our reads to them, identify good quality genomes,
calculate the SNPs, and identify where they are in the genomes.

## The MAG 12 Example

mag\_12 is our best Pseudomonas bin, so we're doing a bit of a deeper dive into it

To identify additional samples suitable for strain-level analysis of the mag\_12
Pseudomonas MAG, reads were extracted from previously merged sample BAM files
using the list of contigs assigned to mag\_12. For each sample, reads mapping to
any mag\_12 contig were extracted with samtools view, generating sample-specific
mag\_12 BAM files. These BAMs were subsequently coordinate-sorted and indexed
before downstream coverage and variant analyses, because the initial
region-based extraction could emit records in contig-list order rather than
BAM-header order.

Read recruitment to mag\_12 was quantified for each sample using samtools
idxstats, summing mapped reads across all mag\_12 contigs. Samples were
prioritised for strain-level analysis based on the number of recruited reads
and whether multiple longitudinal samples were available from the same pwCF.

For each sample, per-contig coverage was calculated using samtools coverage,
and the coverage output was filtered to retain only contigs with non-zero
coverage. For each sample, we summarised the number of covered contigs, total
covered contig length, total recruited reads, mean percentage of covered bases,
and weighted mean depth.

Variants were called jointly across each sample using bcftools mpileup against
the mag\_12 reference sequence, followed by bcftools call. The raw VCF was
filtered to retain only biallelic SNPs with QUAL >= 30 and total depth INFO/DP
>= 20. Genotype patterns across each time point were then tabulated to
distinguish SNPs shared across all samples from SNPs that differed among time
points. Discordant SNPs were defined as high-confidence SNPs in which the
genotype pattern varied across. These discordant SNPs were converted to BED
format and intersected with gene annotations derived from the BV-BRC annotated
GenBank file mag\_12.gb.


# Analysis Steps

0. Create a mamba environment with bcftools and bedtools

```
mamba env create -f env.yaml
```

_Note:_ if you are doing this on Pawsey, do it this way:

```
TMP=$(for i in {1..12}; do printf "%x" $((RANDOM % 16)); done)
mamba create -y --prefix=/scratch/pawsey1018/edwa0468/software/miniconda3/$TMP -f env.yaml --channel-priority flexible
mamba activate /scratch/pawsey1018/edwa0468/software/miniconda3/$TMP
```

1. Make a sourmash index of your MAG(s) and search against the database.

Check [the sourmash page](https://sourmash.readthedocs.io/en/latest/databases-md/) for the latest GTDB release 31-mers
and download that, and then update sourmash.slurm with the file.

```
sbatch sourmash.slurm MAG.fna
```

2. Download the top hit from the sourmash sketch using [NCBI Datasets](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/reference-docs/data-packages/genome/)

```
datasets download genome accession GCF_001457615.1 --include gbff
```

3. Convert the gbff to gff3 and fasta

This python code does both in one go and creates gziped fasta and gff3 files

```
python /home/edwa0468/GitHubs/CF_Data_Analysis_Development/StrainAnalysis/gbk2gff_fna.py -i  GCF_002209555.1.gbff
```

This will create the output files `GCF_002209555.1.gff.gz` and `GCF_002209555.1.fna.gz`


4. Map the reads in the folder `reads` to the fasta file:



1. Create a list of the contigs that contribute to the MAG:

```
zgrep '^>' ../../MixedAssemblies/cross_assembly/bins/2.fna.gz  | sed 's/^>//' | awk '{print $1}' > mag_2.contigs.txt
```

2. Extract the reads that map to the MAG from each of the bam files

```
sbatch ../slurm/extract_mapped_reads.slurm
```

3. Summarise the number of reads per bam file

```
sbatch ../slurm/count_tables.slurm
```

***Output:*** read\_counts.tsv

4. Calculate the coverage per sample

```
sbatch ../slurm/coverage.slurm
```

4. Summarise the coverage per sample

```
sbatch ../slurm/summarise_coverage.slurm
```

***Output:*** coverage\_summary.tsv

5. Calculate the variants per genome

Copy the MAG fasta file:

```
cp ../../MixedAssemblies/cross_assembly/bins/2.fna.gz mag_2.fna.gz
gunzip mag_2.fna.gz
samtools faidx mag_2.fna
```

and then calculate variants

```
sbatch ../slurm/variants.slurm
```

6. Calculate the genotypes per sample

```
sbatch ../slurm/genotype_counts.slurm
```

***Outputs:*** genotype\_counts.txt

7. [Optional]

Convert the GenBank file to a GFF file

```
python gbk2gff_fna.py <mag.gbk> <mag.gff>
```

For example:
```
python ../slurm/gbk2gff.py ../../MixedAssemblies/cross_assembly/annotations/bin_2.gb.gz mag_2.gff
```

7. Extract the annotations for the discordant SNPs

```
sbatch ../slurm/extract_discordant_snps.slurm
```

***Outputs:*** Each sample has a `.discordant\_snps.annotated.tsv` file with the annotations of the discordant SNPs.

8. tar the outputs

```
tar zcf outputs.tgz read_counts.tsv coverage_summary.tsv genotype_counts.txt
```
