import sys
#import numpy as np

elastic_constant =[]

fnm = open("ElasticConstants.txt", "r")
next_lines_with_elastic_constants = 'no'
idx_global=0

for line in fnm:
    if 'Components of the Elastic Constant Tensor' in line:
        next_lines_with_elastic_constants = 'yes'
        continue
    if 'yes' in next_lines_with_elastic_constants:
        if (idx_global == 1 or idx_global == 4 or idx_global == 7):
            idx=0
            for x in line.split():
                if (idx == 4):
                    elastic_constant.append(float(x))
                    break
                idx +=1          
        idx_global+=1

fnm.close()

f = open("ElasticConstants.txt", "w")

for k in range (0,3):
    f.write(str(elastic_constant[k]) + ' ')
f.write("\n")

f.close()
