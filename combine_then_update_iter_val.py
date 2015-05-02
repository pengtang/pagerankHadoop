# This program combine the p_value generated by all the reducers
# 1.Write the new p in file iterative_value
# 2.Print the sum of p difference on screen
import os
import re

# open last iteration p, should be just one line
f1 = open('iterative_value', 'r')
for line in f1:
    raw_data1 = str(line.strip().split())
    data1 = re.findall('[0-9]\.[0-9]*', raw_data1)
    p = [float(s) for s in data1]
f1.close()
previous_p = list(p)

# open p generated by reducer job
f2 = open('output2', 'r')
# read previous_p value                                                                                     
new_p_list = []
for line in f2:
    raw_data2 = str(line.strip().split())
    data2 = re.findall('[0-9]\.[0-9]*',raw_data2)
    current_reducer_p = [float(s) for s in data2]
    new_p_list.append(current_reducer_p)
f2.close()

# Computation part, combine
for single_reducer_p in new_p_list:
    for i in range(len(single_reducer_p)):
        if single_reducer_p[i] != 0:
            p[i] = single_reducer_p[i]

print sum(abs(p[i]-previous_p[i]) for i in range(len(p)))

# Overwrite to the file
f3 = open('iterative_value', 'w')                                                                     
t = str(p)                                                                                                   
f3.write(t)                                                                                 
f3.close()  
