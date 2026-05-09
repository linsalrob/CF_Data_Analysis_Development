#!/bin/bash
#SBATCH --account=pawsey1018
#SBATCH --job-name=GenotypeCounts
#SBATCH --time=0-4
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=32GB
#SBATCH -o %x-%j.out
#SBATCH -e %x-%j.err

set -euo pipefail
trap 's=$?; echo "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR

eval "$(conda shell.bash hook)"
conda activate /scratch/$PAWSEY_ACCOUNT/$USER/software/miniconda3/strain_analysis

MAG=$(basename "$SLURM_SUBMIT_DIR")
for pwcf in $(find variants/ -maxdepth 1 -mindepth 1 -type d -printf "%f\n" | grep -v ${MAG})
do
	if [[ -e variants/$pwcf/filtered/$pwcf.${MAG}.snps.qual30.dp20.vcf.gz ]]; then


		NS=$(find mapped_reads/${MAG} -name ${pwcf}_*.bam | wc -l);
		LQ=$(bcftools view -H variants/$pwcf/$pwcf.${MAG}.raw.vcf.gz | wc -l)
		HQ=$(bcftools view -H variants/$pwcf/filtered/$pwcf.${MAG}.snps.qual30.dp20.vcf.gz | wc -l)

		if [[ $HQ -gt 0 ]]; then 
			if [[ ! -e variants/$pwcf/filtered/$pwcf.${MAG}.snps.genotypes.tsv ]]; then
				bcftools query \
				  -f '%CHROM\t%POS[\t%GT]\n' \
				  variants/$pwcf/filtered/$pwcf.${MAG}.snps.qual30.dp20.vcf.gz \
				  > variants/$pwcf/filtered/$pwcf.${MAG}.snps.genotypes.tsv
			fi

			echo -e "\n$pwcf\nNumber of samples: $NS\nLow Quality (all) SNPs: $LQ\nHigh quality SNPs: $HQ\nGenotype\tSites"
			awk -F'\t' '
			{
			    pattern = $3
			    for (i = 4; i <= NF; i++) {
				pattern = pattern "|" $i
			    }
			    count[pattern]++
			}
			END {
			    OFS="\t"
			    for (p in count) print p, count[p]
			}' variants/$pwcf/filtered/$pwcf.${MAG}.snps.genotypes.tsv \
			  | sort -k2,2nr
		else
			echo -e "\n$pwcf\nNumber of samples: $NS\nLow Quality (all) SNPs: $LQ\nHigh quality SNPs: $HQ\n"
		fi
	fi
done > ${MAG}_genotype_counts.txt
