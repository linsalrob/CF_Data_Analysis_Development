#!/bin/bash
#SBATCH --account=pawsey1018
#SBATCH --job-name=extractreads
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

mkdir -p mapped_reads/${MAG}

for bam in ../../MixedAssemblies/cross_assembly/mapped_reads/merged/*.bam
do
    sample=$(basename "$bam" .bam)

    echo "Extracting ${MAG} reads from $sample"

    samtools view -b "$bam" $(cat ${MAG}.contigs.txt) -o "mapped_reads/${MAG}/${sample}.${MAG}.bam"
    samtools index "mapped_reads/${MAG}/${sample}.${MAG}.bam" &

done

