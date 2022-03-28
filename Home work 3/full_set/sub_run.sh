#!/bin/bash

source ~/.bashrc
# Launch MPI-based executable
src=$(pwd)
cd $src
pwd

export OMP_NUM_THREADS=1

sbatch -J run -o run.out -e run.err -N 3 --exclusive --time=720:00:00 --partition=RT --comment="SISSO" ./run.sh
