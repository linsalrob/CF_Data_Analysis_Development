#!/bin/bash
#SBATCH --account=pawsey1018
#SBATCH --job-name=adelaide_strains
#SBATCH --time=0-4
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=128GB
#SBATCH -o %x-%j.out
#SBATCH -e %x-%j.err

set -euo pipefail
trap 's=$?; echo "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR

eval "$(conda shell.bash hook)"
conda activate /scratch/$PAWSEY_ACCOUNT/$USER/software/miniconda3/strain_analysis

MAG=$(basename "$SLURM_SUBMIT_DIR")

# These are the high-depth candidates

mkdir -p variants/${MAG}_adelaide

bcftools mpileup \
  -f ${MAG}.fna \
  -Ou \
  mapped_reads/${MAG}_sorted/1128691_20171206_S.${MAG}.sorted.bam \
  mapped_reads/${MAG}_sorted/639354_20171206_S.${MAG}.sorted.bam \
  mapped_reads/${MAG}_sorted/1162967_20180116_S.${MAG}.sorted.bam \
  mapped_reads/${MAG}_sorted/983493_20180123_S.${MAG}.sorted.bam \
  mapped_reads/${MAG}_sorted/1282052_20180206_S.${MAG}.sorted.bam \
  mapped_reads/${MAG}_sorted/1593973_20180504_S.${MAG}.sorted.bam \
  mapped_reads/${MAG}_sorted/895293_20180502_S.${MAG}.sorted.bam \
| bcftools call \
  -mv \
  --ploidy 1 \
  -Oz \
  -o variants/${MAG}_adelaide/${MAG}.adelaide.raw.vcf.gz

bcftools index variants/${MAG}_adelaide/${MAG}.adelaide.raw.vcf.gz

mkdir -p variants/${MAG}_adelaide/filtered

bcftools view \
  -v snps \
  -m2 -M2 \
  -i 'QUAL>=30 && INFO/DP>=20' \
  -Oz \
  -o variants/${MAG}_adelaide/filtered/${MAG}.adelaide.snps.qual30.dp20.vcf.gz \
  variants/${MAG}_adelaide/${MAG}.adelaide.raw.vcf.gz

bcftools index \
  variants/${MAG}_adelaide/filtered/${MAG}.adelaide.snps.qual30.dp20.vcf.gz



bcftools query \
  -f '%CHROM\t%POS[\t%GT]\n' \
  variants/${MAG}_adelaide/filtered/${MAG}.adelaide.snps.qual30.dp20.vcf.gz \
  > variants/${MAG}_adelaide/filtered/${MAG}.adelaide.snps.genotypes.tsv


awk -F'\t' '
{
    pattern = $3
    for (i = 4; i <= NF; i++) {
        pattern = pattern "|" $i
    }
    count[pattern]++
}
END {
    OFS = "\t"
    print "genotype_pattern", "sites"
    for (p in count) print p, count[p]
}' variants/${MAG}_adelaide/filtered/${MAG}.adelaide.snps.genotypes.tsv \
  | sort -k2,2nr \
  > variants/${MAG}_adelaide/filtered/${MAG}.adelaide.snp_patterns.tsv



awk -F'\t' '
{
    pattern = $3
    target = "1"

    for (i = 4; i <= NF; i++) {
        pattern = pattern "|" $i
        target = target "|1"
    }

    if (pattern == target) {
        print
    }
}' variants/${MAG}_adelaide/filtered/${MAG}.adelaide.snps.genotypes.tsv \
  > variants/${MAG}_adelaide/filtered/${MAG}.adelaide.shared_all_snps.tsv

CT=$(wc -l variants/${MAG}_adelaide/filtered/${MAG}.adelaide.shared_all_snps.tsv)
echo "There are $CT shared SNPs"

# Make a BED file

awk -F'\t' '
BEGIN { OFS="\t" }
{
    pattern = $3
    for (i = 4; i <= NF; i++) {
        pattern = pattern "|" $i
    }

    print $1, $2-1, $2, pattern
}' variants/${MAG}_adelaide/filtered/${MAG}.adelaide.shared_all_snps.tsv \
  > variants/${MAG}_adelaide/filtered/${MAG}.adelaide.shared_all_snps.bed


## annotate them

bedtools intersect \
  -a variants/${MAG}_adelaide/filtered/${MAG}.adelaide.shared_all_snps.bed \
  -b ${MAG}.gff \
  -wa -wb \
  > variants/${MAG}_adelaide/filtered/${MAG}.adelaide.shared_all_snps.annotated.tsv
