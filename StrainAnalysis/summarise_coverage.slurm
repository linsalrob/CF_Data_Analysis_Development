#!/bin/bash
#SBATCH --account=pawsey1018
#SBATCH --job-name=SummariseCoverage
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
echo -e "sample\tcovered_contigs\tcovered_contig_len\treads\tmean_coverage_pct\tweighted_mean_depth" > coverage_summary.tsv
for f in $(find tables/${MAG}_coverage_summary/ -type f -name \*coverage.tsv); do
	NZ=${f/coverage.tsv/coverage.nonzero.tsv}

	cat $f | awk -F'\t' '$5 > 0 || $6 > 0'  > $NZ
	pigz $f

	awk -F'\t' '
	{
	    sample=$1
	    contigs[sample]++
	    total_len[sample]+=$4
	    total_reads[sample]+=$5
	    covered_bases[sample]+=$6
	    depth_sum[sample]+=$8*$4
	}
	END {
	    OFS="\t"
	    for (s in contigs) {
		print s,
		      contigs[s],
		      total_len[s],
		      total_reads[s],
		      100*covered_bases[s]/total_len[s],
		      depth_sum[s]/total_len[s]
	    }
	}' $NZ >> coverage_summary.tsv
done
