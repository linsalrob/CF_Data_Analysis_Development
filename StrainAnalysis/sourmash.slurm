#!/bin/bash
#SBATCH --account=pawsey1018
#SBATCH --job-name=sourmash
#SBATCH --time=1-0
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=128GB
#SBATCH -o %x-%j.out
#SBATCH -e %x-%j.err

set -euo pipefail
trap 's=$?; echo "$0: Error on line "$LINENO": $BASH_COMMAND"; exit $s' ERR

eval "$(conda shell.bash hook)"
conda activate /scratch/$PAWSEY_ACCOUNT/$USER/software/miniconda3/strain_analysis

MAG=$1
SIG=${MAG/.fna/.sig}
if [[ $MAG -eq $SIG ]]; then SIG=$SIG.sig; fi

echo "Sketching $MAG";
sourmash sketch dna -p k=31,scaled=1000 -o $SIG $MAG; fi
sourmash search sepsigs/$SIG gtdb-reps-rs226-k31.dna.zip --threshold 0.01 -o $MAG.search.csv
sourmash gather sepsigs/$SIG gtdb-reps-rs226-k31.dna.zip -o $MAG.gather.csv
