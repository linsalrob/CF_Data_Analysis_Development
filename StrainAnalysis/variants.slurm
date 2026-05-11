#!/bin/bash
#SBATCH --account=pawsey1018
#SBATCH --job-name=VariantCalling
#SBATCH --time=0-12
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=128G
#SBATCH -o %x-%j.out
#SBATCH -e %x-%j.err

set -euo pipefail
trap 's=$?; echo "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR

eval "$(conda shell.bash hook)"
conda activate /scratch/$PAWSEY_ACCOUNT/$USER/software/miniconda3/strain_analysis

MAG=$(basename "$SLURM_SUBMIT_DIR")

if [[ -e ${MAG}.fna.gz ]] && [[ ! -e ${MAG}.fna ]]; then gunzip -c ${MAG}.fna.gz > ${MAG}.fna; fi
for pwcf in $(find mapped_reads/${MAG}/ -type f -name \*.bam -printf "%f\n" | cut -d '_' -f 1 | awk '!s[$1]++');
do
	if [[ ! -e variants/$pwcf/filtered/$pwcf.${MAG}.snps.qual30.dp20.vcf.gz ]]; then
		echo "Calling variants for $pwcf"
		mkdir -p variants/$pwcf
		BAMS=$(find mapped_reads/${MAG}/ -name ${pwcf}_\*.bam -printf "%p ")

		bcftools mpileup \
		  -f ${MAG}.fna \
		  -Ou $BAMS \
		| bcftools call \
		  -mv \
		  --ploidy 1 \
		  -Oz \
		  -o variants/$pwcf/$pwcf.${MAG}.raw.vcf.gz

		bcftools index variants/$pwcf/$pwcf.${MAG}.raw.vcf.gz

		# create high quality SNPs
		mkdir -p variants/$pwcf/filtered

		bcftools view \
		  -v snps \
		  -m2 -M2 \
		  -i 'QUAL>=30 && INFO/DP>=20' \
		  -Oz \
		  -o variants/$pwcf/filtered/$pwcf.${MAG}.snps.qual30.dp20.vcf.gz \
		  variants/$pwcf/$pwcf.${MAG}.raw.vcf.gz

		bcftools index \
		  variants/$pwcf/filtered/$pwcf.${MAG}.snps.qual30.dp20.vcf.gz
	else
		echo "Skipped $pwcf already done"
	fi
done
