#!/bin/bash
#SBATCH --account=pawsey1018
#SBATCH --job-name=DiscordantSNPs
#SBATCH --time=0-4
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=32GB
#SBATCH -o %x-%j.out
#SBATCH -e %x-%j.err

set -euo pipefail
trap 's=$?; echo "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR

eval "$(conda shell.bash hook)"
conda activate /scratch/pawsey1018/edwa0468/software/miniconda3/36b7c7c353af

MAG=$(basename "$SLURM_SUBMIT_DIR")
for pwcf in $(find variants/ -maxdepth 1 -mindepth 1 -type d -printf "%f\n" | grep -v ${MAG})
do
	if [[ -e variants/$pwcf/filtered/$pwcf.${MAG}.snps.genotypes.tsv && -s variants/$pwcf/filtered/$pwcf.${MAG}.snps.genotypes.tsv ]]; then
		awk -F'\t' '
		{
		    pattern=$3 "|" $4 "|" $5
		    if (pattern != "1|1|1" && pattern != "1|.|1" && pattern != "1|1|." && pattern != ".|1|1")
			print
		}' variants/$pwcf/filtered/$pwcf.${MAG}.snps.genotypes.tsv \
		  > variants/$pwcf/filtered/$pwcf.${MAG}.discordant_snps.tsv


		DS=$(wc -l variants/$pwcf/filtered/$pwcf.${MAG}.discordant_snps.tsv | cut -d ' ' -f 1)
		echo "There are $DS discordant SNPs in $pwcf. Calculating annotations."

		awk -F'\t' 'BEGIN{OFS="\t"} {print $1, $2-1, $2, $3 "|" $4 "|" $5}' \
		  variants/$pwcf/filtered/$pwcf.${MAG}.discordant_snps.tsv \
		  > variants/$pwcf/filtered/$pwcf.${MAG}.discordant_snps.bed

		echo "Extracting locations"
		bedtools intersect \
		  -a variants/$pwcf/filtered/$pwcf.${MAG}.discordant_snps.bed \
		  -b ${MAG}.gff \
		  -wa -wb \
		  > variants/$pwcf/filtered/$pwcf.${MAG}.discordant_snps.annotated.tsv
	fi
done
