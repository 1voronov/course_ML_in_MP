#!/usr/bin/python
import os, sys, re
import random

with open(os.path.join(os.getcwd(), 'train.dat'), 'r') as inputfile:
	lines = inputfile.readlines()
	
	titlea = lines[0].strip('\n')
	
	index__property = {}
	a = 0
	for line in lines[1:]:
		a += 1
		index__property[a] = line.strip('\n')

# divide list into several groups
def chunkIt(seq, num):
	avg = len(seq) / float(num)
	out = []
	last = 0.0
	
	while last < len(seq):
		out.append(seq[int(last):int(last + avg)])
		last += avg
	
	return out

index_list = []
for i in range(a):
	index_list.append(i+1)

random.shuffle(index_list)

out_list = chunkIt(index_list, 20)

folder_num = 0
for sub_list in out_list:
	folder_num += 1
	folder_name = str('{:03d}'.format(folder_num)) +'_' + str(len(sub_list))
	
	if not os.path.exists(folder_name):
		os.makedirs(os.path.join(os.getcwd(), folder_name))
	
	with open(os.path.join(os.getcwd(), folder_name, 'predict.dat'), 'w') as choose:
		choose.write(titlea + '\n')
		for i in sub_list:
			choose.write(index__property[i] + '\n')
	
	with open(os.path.join(os.getcwd(), folder_name, 'train.dat'), 'w') as remaining:
		remaining.write(titlea + '\n')
		
		for i in range(a):
			j = i+1
			if j not in sub_list:
				remaining.write(index__property[j] + '\n')
	

