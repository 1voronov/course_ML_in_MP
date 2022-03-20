import sys
# import numpy as np

total_args = len(sys.argv)
if(total_args != 3):
    sys.stderr.write('Error: 2 arguments required\n')
    exit(1)

f_to_load=open(sys.argv[1], "r")
f_to_save=open(sys.argv[2], "w")
curr_keyword = ''
a = []
idx_curr = 0
idx = 0
volume = 0
energy = 0

for line in f_to_load: 
    if 'Supercell' in line.split():
        curr_keyword = 'Supercell'
        continue
    if (curr_keyword == 'Supercell'):
        for x in line.split():
            a.append(float(x))
            idx_curr += 1
        idx += 1
        if (idx == 3):
            curr_keyword = ''
            idx = 0
            idx_curr = 0
            volume = a[0]*a[4]*a[8] + a[1]*a[5]*a[6] + a[2]*a[3]*a[7] - a[2]*a[4]*a[6] - a[0]*a[5]*a[7] - a[1]*a[3]*a[8]
            a = []
    if 'Energy' in line.split():
        curr_keyword = 'Energy'
        continue
    if (curr_keyword == 'Energy'):
        for x in line.split():
            energy = float(x)
            curr_keyword = ''  
            f_to_save.write(str(volume)+" "+str(energy)+"\n")
	    
f_to_load.close()
f_to_save.close()
