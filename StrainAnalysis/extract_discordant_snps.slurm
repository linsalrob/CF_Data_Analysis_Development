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
conda activate /scratch/$PAWSEY_ACCOUNT/$USER/software/miniconda3/strain_analysis

MAG=$(basename "$SLURM_SUBMIT_DIR")
for pwcf in $(find variants/ -maxdepth 1 -mindepth 1 -type d -printf "%f\n" | grep -v ${MAG})
do
	echo -n "Checking $pwcf ... " >&2

	genotype_file="variants/$pwcf/filtered/$pwcf.${MAG}.snps.genotypes.tsv.gz"
	output_file="variants/$pwcf/filtered/$pwcf.${MAG}.discordant_snps.tsv"
	bed_output_file="variants/$pwcf/filtered/$pwcf.${MAG}.discordant_snps.bed"
	variant_ouput_file="variants/$pwcf/filtered/$pwcf.${MAG}.discordant_snps.annotated.tsv"

	if [[ -e "$genotype_file" && -s "$genotype_file" ]]; then
		echo "Calculating" >&2

		gunzip -c "$genotype_file" | \
			awk -F'\t' '
		{
			all_called_are_one = 1
			n_called = 0

			for (i = 3; i <= NF; i++) {
				if ($i == ".") {
					continue
				}

				n_called++

				if ($i != "1") {
					all_called_are_one = 0
					break
				}
			}

			if (!(n_called > 0 && all_called_are_one)) {
				print
			}
		}' \
		> "$output_file"

		DS=$(wc -l variants/$pwcf/filtered/$pwcf.${MAG}.discordant_snps.tsv | cut -d ' ' -f 1)
		echo "There are $DS discordant SNPs in $pwcf. Calculating annotations."

		awk -F'\t' 'BEGIN{OFS="\t"} {print $1, $2-1, $2, $3 "|" $4 "|" $5}' \
			$output_file \
			> $bed_output_file

		echo "Extracting locations"
		bedtools intersect \
			-a $bed_output_file \
			-b ${MAG}.gff \
			-wa -wb \
			> $variant_ouput_file
	else
		echo "Skipped" >&2
	fi
done
