#!/bin/bash
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --job-name=mlip
#SBATCH --comment=mlip
#SBATCH --output="out.ElConst.%j"
export OMP_NUM_THREADS=1

rm -f ElasticConstants.txt

cd ElConst

for i in 1 2 3 4 5; do
    rm -f mlip.ini
    echo "mtp-filename    ../../1.train_and_validate/pot.${i}.mtp" > mlip.ini

    ../../../../mlip-2/bin/mlp convert-cfg ../../2.relax_and_compress-extend_and_E_V/relaxed.${i}.cfg_0 input.pos --output-format=lammps-datafile

    ../../../../mylammps/src/lmp_mpi -log log.${i}.lammps -in in.elastic > ElasticConstants.txt

    python3 read-ElasticConstants-create-file.py

    cat ElasticConstants.txt >> ../ElasticConstants.txt
done

cd ../


