# This program is used to generate the iterative_value for the first time
# Write the initial value to iterative_value
import os

# need to obtain this value through some other ways                                     
N = 300000
p = [1./N] * N

f = open('iterative_value', 'w')

#t = str(p) + '\n'                                                                               
t = str(p)
f.write(t)
f.close()
