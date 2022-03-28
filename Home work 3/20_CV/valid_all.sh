#!/bin/bash

dirs=$(ls -d */)

for i in ${dirs}; do
	cd $i
	rm file_tmp desc_tmp
	./sub_valid.sh
	cd ../
done
