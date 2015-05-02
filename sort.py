# After running the job2.sh, if difference<threshold. And then run combine_then_update_iter_val.py
# This is the last script file, which outputs the top 20 Twitter users based on pageRank algorithm.

import sys
import re
import operator

f1 = open('iterative_value', 'r')
for line in f1:
    raw_data1 = str(line.strip().split())
    data1 = re.findall('[0-9]\.[0-9]*', raw_data1)
    p = [float(s) for s in data1]
f1.close()

def getKey(x):
    return float(x[1])

record = []
for i in range(len(p)):
    record.append([i, p[i]])

record.sort(key = getKey, reverse = True)

for i in range(20):
    print record[i]
    

#dic = {}
#for i in range(len(p)):
#    dic[i] = p[i]

#sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
#print sorted_dic
