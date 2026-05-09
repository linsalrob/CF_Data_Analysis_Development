#!/bin/bash
#SBATCH --account=pawsey1018
#SBATCH --job-name=mergebam
#SBATCH --time=0-4
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=64GB
#SBATCH -o %x-%j.out
#SBATCH -e %x-%j.err

set -euo pipefail
trap 's=$?; echo "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR

eval "$(conda shell.bash hook)"
conda activate /scratch/$PAWSEY_ACCOUNT/$USER/software/miniconda3/strain_analysis

MAG=$(basename "$SLURM_SUBMIT_DIR")
mkdir -p merged
for BAM in $(find bam -type f ! -name "*nanopore*"); do
    NP=${BAM/.bam/.nanopore.bam}
    if [[ -e $NP ]]; then
        OUT=$(basename $BAM)
        echo "Merging $NP and $BAM"
        samtools merge -o - $NP $BAM | samtools sort -@ 16 -o merged/$OUT -
    else
        cp $BAM merged/
    fi
done
find merged -type f -name "*.bam" | parallel samtools index {}

