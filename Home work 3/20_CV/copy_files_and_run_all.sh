#!/bin/bash


dirs_2=$(ls -d *2/)
dirs_3=$(ls -d *3/)

for i in ${dirs_2}; do
	cp 43_samples/SISSO.in run.sh valid.sh sub_run.sh sub_valid.sh SISSO SISSO_predict SISSO_predict_para calc.sh calc.py $i
	cd $i
	#./sub_run.sh
	cd ../
done

for i in ${dirs_3}; do
	cp 42_samples/SISSO.in run.sh valid.sh sub_run.sh sub_valid.sh SISSO SISSO_predict SISSO_predict_para calc.sh calc.py $i
	cd $i
	#./sub_run.sh
	cd ../
done
