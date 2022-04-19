#!/bin/bash
#SBATCH -N 1
#SBATCH --ntasks-per-node=16
#SBATCH --job-name=mlip
#SBATCH --comment=mlip
#SBATCH --output="out.train.%j"

source ~/.bashrc

rm -f train.cfg
rm -f curr.mtp
rm -f preselected.cfg
rm -f diff.cfg
rm -f selected.cfg
rm -f out.cfg

cp init.mtp curr.mtp
cp train_init.cfg train.cfg

#A. Active set construction
mpirun -np 1 ../../../mlip-2/bin/mlp calc-grade curr.mtp train.cfg train.cfg out.cfg --als-filename=state.als

rm out.cfg

while [ 1 -gt 0 ]
do

#B. MD simulations and extrapolative (preselected) configurations
touch preselected.cfg
# ../../../mlip-2/bin/mlp -in in.nb_md
srun ../../../mylammps/src/lmp_serial -in in.nb_md

n_preselected=$(grep "BEGIN" preselected.cfg | wc -l)

if [ $n_preselected -gt 0 ]; then

#C. Selection
    ../../../mlip-2/bin/mlp select-add curr.mtp train.cfg preselected.cfg diff.cfg --als-filename=state.als
    cp diff.cfg calculate_ab_initio_ef/

    rm -f preselected.cfg
    rm -f selected.cfg

#D and E. Ab initio calculations and merging (updating the training set)
    cd calculate_ab_initio_ef/
    ./ab_initio_calculations.sh
    cd ../

#F. Training
    n_cores=16
    mpirun -n $n_cores ../../../mlip-2/bin/mlp train curr.mtp train.cfg --trained-pot-name=curr.mtp --update-mindist
    
#A. Active set construction
    ../../../mlip-2/bin/mlp calc-grade curr.mtp train.cfg diff.cfg out.cfg --als-filename=state.als
    
    rm -f diff.cfg
    rm -f out.cfg
    
elif  [ $n_preselected -eq 0 ]; then
    exit
fi

done
