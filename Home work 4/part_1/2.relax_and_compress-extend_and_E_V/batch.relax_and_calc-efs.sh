#!/bin/bash

for i in 1 2 3 4 5; do
	../../../mlip-2/bin/mlp relax relax.${i}.ini --cfg-filename=../../init.cfg --save-relaxed=relaxed.${i}.cfg
	../../../mlip-2/bin/mlp compress-extend relaxed.${i}.cfg_0 deformed.${i}.cfg
	../../../mlip-2/bin/mlp calc-efs ../1.train_and_validate/pot.${i}.mtp deformed.${i}.cfg deformed_efs.${i}.cfg
    python3 cfg-to-energy-volume.py deformed_efs.${i}.cfg E_V.${i}.txt
done
