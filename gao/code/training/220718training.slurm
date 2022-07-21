#!/bin/bash
#SBATCH --job-name=Jtrain
#SBATCH --account=opencrums
#SBATCH --nodes=1
#SBATCH --gres=gpu:8
#SBATCH --time=24:00:00
#SBATCH -o ./sbatch/output.%a.out # STDOUT

module load anaconda3
source activate pydda_env

python "2022 summer argonne/jupyter/tasks/training/training.py"
