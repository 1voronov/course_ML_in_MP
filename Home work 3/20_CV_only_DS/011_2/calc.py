import numpy as np
import math

f_read = open('file_tmp', 'r')
f = open('desc_tmp', 'w')

for line in f_read:
    #print(line)
    line_new = line
    line_new = line_new.replace('exp','np.exp')
    line_new = line_new.replace('log','np.log')
    line_new = line_new.replace('cbrt','np.cbrt')
    line_new = line_new.replace('sqrt','np.sqrt')
    line_new = line_new.replace('^','**')
    #print(line_new)
    #print(eval(line_new))
    f.write(str(eval(line_new))+"\n")
    
f_read.close()
f.close()
