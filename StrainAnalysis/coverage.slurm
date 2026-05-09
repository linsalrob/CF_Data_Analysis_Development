#!/bin/bash
#SBATCH --account=pawsey1018
#SBATCH --job-name=Coverage
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



mkdir -p tables/${MAG}_coverage

for bam in mapped_reads/${MAG}/*.${MAG}.bam
do
    sample=$(basename "$bam" .${MAG}.bam)
    if [[ ! -e tables/${MAG}_coverage/${sample}.coverage.tsv ]]; then
	    echo "$bam --> $sample"
	    samtools coverage "$bam" \
		> tables/${MAG}_coverage/${sample}.coverage.tsv
    fi
done

mkdir -p tables/${MAG}_coverage_summary
for f in $(find tables/${MAG}_coverage -type f)
do
    sample=$(basename "$f" .coverage.tsv)
    pwcf=$(basename $f .coverage.tsv | cut -d'_' -f 1)
    echo "Summarising $pwcf $sample"
    awk -v sample="$sample" 'NR==1 {next} {print sample "\t" $0}' "$f" >> tables/${MAG}_coverage_summary/$pwcf.${MAG}.coverage.tsv
done 
