#!/bin/bash
export OMP_NUM_THREADS=1
src=$(pwd)
cd $src
./SISSO_predict SISSO_predict_para
