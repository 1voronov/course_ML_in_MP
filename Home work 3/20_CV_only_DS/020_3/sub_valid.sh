#!/bin/bash

source ~/.bashrc
# Launch MPI-based executable
src=$(pwd)
cd $src
pwd

export OMP_NUM_THREADS=1

sbatch -J valid -o valid.out -e valid.err -N 1 -n 1 --time=720:00:00 --partition=RT --comment="SISSO" ./valid.sh
