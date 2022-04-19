#!/bin/bash

n_selected=$(grep "BEGIN" diff.cfg | wc -l)
../../../../mlip-2/bin/mlp convert-cfg diff.cfg lammps_input --output-format=lammps-datafile

for ((i=0; i<n_selected; i++))
do
    if [ $n_selected -eq 1 ]; then 
        cp lammps_input input.pos
    elif [ $n_selected -gt 1 ]; then
        cp lammps_input"$i" input.pos
    fi
#D. Ab initio calculation
    ../../../../mylammps/src/lmp_serial -in calc_ef.in
#E. Merging (updating the training set)
    python convert_lammps_dump_to_cfg.py
    cat output_ef.cfg >> ../train.cfg
done

rm diff.cfg 
rm output_ef*
rm lammps_input*
rm log.lammps
rm input.pos
