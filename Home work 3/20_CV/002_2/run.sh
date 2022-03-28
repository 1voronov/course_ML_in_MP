#!/bin/bash
export OMP_NUM_THREADS=1
src=$(pwd)
cd $src
./SISSO SISSO.in train.dat
