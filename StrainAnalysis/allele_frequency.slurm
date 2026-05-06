#!/bin/bash
#SBATCH --account=pawsey1018
#SBATCH --job-name=AlleleFrequency
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
echo -e "near_ref_<0.05\tnear_alt_>0.95\tintermediate_0.2_to_0.8\tother_0.05_to_0.2_or_0.8_to_0.95\tNA" > ${MAG}_allele_frequencies.tsv
for pwcf in $(find variants/ -maxdepth 1 -mindepth 1 -type d -printf "%f\n" | grep -v ${MAG})
do
	echo "Allele frequency for $pwcf"
	mkdir -p variants/$pwcf/allele_frequency

	if [[ ! -e variants/$pwcf/allele_frequency/$pwcf.$MAG.snps.AD.tsv ]]; then
		bcftools query \
			-f '%CHROM\t%POS\t%REF\t%ALT[\t%SAMPLE:%GT:%DP:%AD]\n' \
			variants/$pwcf/filtered/$pwcf.$MAG.snps.qual30.dp20.vcf.gz \
			> variants/$pwcf/allele_frequency/$pwcf.$MAG.snps.AD.tsv
	fi

	if [[ ! -e variants/$pwcf/allele_frequency/$pwcf.$MAG.snps.allele_frequency.tsv ]]; then
		awk -F'\t' '
		BEGIN {
			OFS="\t"
			print "contig", "pos", "ref", "alt", "sample", "gt", "dp", "ref_depth", "alt_depth", "alt_freq"
		}
		{
			contig=$1
			pos=$2
			ref=$3
			alt=$4

			for (i=5; i<=NF; i++) {
				split($i, a, ":")
				sample=a[1]
				gt=a[2]
				dp=a[3]
				ad=a[4]

				split(ad, d, ",")
				ref_depth=d[1]+0
				alt_depth=d[2]+0
				total=ref_depth+alt_depth

				if (total > 0) {
					alt_freq=alt_depth/total
				} else {
					alt_freq="NA"
				}

			print contig, pos, ref, alt, sample, gt, dp, ref_depth, alt_depth, alt_freq
			}
		}' variants/$pwcf/allele_frequency/$pwcf.$MAG.snps.AD.tsv \
		> variants/$pwcf/allele_frequency/$pwcf.$MAG.snps.allele_frequency.tsv
	fi


	awk -F'\t' '
	NR==1 {next}
	$10 != "NA" && $10 >= 0.2 && $10 <= 0.8 {
		count[$5]++
	}
	END {
		OFS="\t"
		print "sample", "intermediate_frequency_sites_0.2_to_0.8"
		for (s in count) print s, count[s]
	}' variants/$pwcf/allele_frequency/$pwcf.$MAG.snps.allele_frequency.tsv

	echo -ne "$MAG\t$pwcf\t" >> ${MAG}_allele_frequencies.tsv
	awk -F'\t' '
	NR == 1 { next }

	$NF == "NA" {
	    na++
	    next
	}

	{
	    af = $NF + 0

	    if (af < 0.05) {
		near_ref++
	    } else if (af > 0.95) {
		near_alt++
	    } else if (af >= 0.2 && af <= 0.8) {
		intermediate++
	    } else {
		other++
	    }
	}

	END {
	    OFS = "\t"
	    print near_ref + 0, near_alt + 0, intermediate + 0, other + 0, na + 0
	}' variants/$pwcf/allele_frequency/$pwcf.$MAG.snps.allele_frequency.tsv >> ${MAG}_allele_frequencies.tsv


done
