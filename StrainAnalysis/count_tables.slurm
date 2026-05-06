#!/bin/bash
#SBATCH --account=pawsey1018
#SBATCH --job-name=counttables
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

echo -e "sample\t${MAG}_mapped_reads" > ${MAG}_read_counts.tsv

for bam in mapped_reads/${MAG}/*.${MAG}.bam
do
    sample=$(basename "$bam" .${MAG}.bam)

    reads=$(samtools idxstats "$bam" \
        | awk '$1 != "*" {sum += $3} END {print sum+0}')

    echo -e "${sample}\t${reads}" >> ${MAG}_read_counts.tsv
done
