import os
import sys
import re
f = open('output1','r')

sum_of_zero_out_degree = 0
#total_user = 0
for line in f:
    raw_data = str(line.strip().split())
    data =  re.findall('[0-9][0-9]*',raw_data)
    field1 = int(data[0])
    field2 = [int(s) for s in data[1:]]
    sum_of_zero_out_degree += 1 if field2[1] == 0 else 0
#    total_user += 1

print sum_of_zero_out_degree
#print total_user
