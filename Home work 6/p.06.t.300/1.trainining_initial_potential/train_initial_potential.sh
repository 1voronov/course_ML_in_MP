#!/bin/bash
#SBATCH -N 1
#SBATCH --ntasks-per-node=16
#SBATCH --job-name=mlip
#SBATCH --comment=mlip
#SBATCH --output="out.train.%j"

export OMP_NUM_THREADS=1

mpirun -np 16 ../../../mlip-2/bin/mlp train 06.mtp train_init.cfg --trained-pot-name=init.mtp
