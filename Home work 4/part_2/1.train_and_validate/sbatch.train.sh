#!/bin/bash
#SBATCH -N 1
#SBATCH --ntasks-per-node=16
#SBATCH --job-name=mlip
#SBATCH --comment=mlip
#SBATCH --output="out.train.%j"

for i in 1 2 3 4 5; do
	mpirun -n 16 ../../../mlip-2/bin/mlp train untrained.12.mtp ../../train_full.cfg  --trained-pot-name=pot.${i}.mtp > train.${i}.report
done
