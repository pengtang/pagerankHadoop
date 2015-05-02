import os
import sys
import re
#import numpy

# EVERY COPY OF REDUCER JOB HAS THE GLOBAL DATA LIKE THIS

TOTAL_ZERO_OUT_DEGREE = int(os.environ.get('TOTAL_ZERO'))
TOTAL_USER = int(os.environ.get('TOTAL_USER'))
#TOTAL_ZERO_OUT_DEGREE = 2
#TOTAL_USER = 300000

S = 0.85
# TOLERANCE = 0.1

f1 = open('output1','r')

# This will be run sequentially(from node 1 to the last one)
KEYS = {}
IN_LINKS = {}
OUT_LINK_NUM = {}
for line in f1:
    raw_data = str(line.strip().split())
    data =  re.findall('[0-9][0-9]*',raw_data)
    field1 = int(data[0])
    field2 = [int(s) for s in data[1:]]
    KEYS[field1] = field2
    IN_LINKS[field1] = field2[2:] if len(field2)>2 else []
    OUT_LINK_NUM[field1] = field2[1]
f1.close()
#print IN_LINKS
#print OUT_LINK_NUM

f2 = open('iterative_value', 'r')
# read previous_p value
for line in f2:
    raw_data2 = str(line.strip().split())
    data2 = re.findall('[0-9]\.[0-9]*',raw_data2)
    previous_p = [float(s) for s in data2]
# print previous_p
p = list(previous_p)
f2.close()

# BELOW IS THE SPECIFIC JOB FOR EACH REDUCER
keys = []
for line in sys.stdin:
    raw_data = str(line.strip().split())
    data =  re.findall('[0-9][0-9]*',raw_data)
    key = int(data[0])
    keys.append(key)

v = [0] * TOTAL_USER
for j in keys:
    #v[j] = S * TOTAL_USER * sum(previous_p[k]
    v[j] = S * sum(p[k]/OUT_LINK_NUM[k] for k in IN_LINKS[j]) + S * TOTAL_ZERO_OUT_DEGREE/TOTAL_USER + (1-S)/TOTAL_USER
v_sum = sum(v)
#print v_sum
for j in keys:
    p[j] = v[j] / v_sum

# entries to the p(as key), and the updated p(as value) with the same format as one of the input to this job, send to the next job.
# in the next job, it collects all the updates

#print sum(abs(p[i]-previous_p[i]) for i in range(TOTAL_USER))
print p
#f3 = open('iterative_value', 'w')
#t = str(p)
#f3.write(t)
#f3.close()
