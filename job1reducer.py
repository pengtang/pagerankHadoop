import sys

#SIZE = 11316811
SIZE = 300000
keys = {}
keys[0] = [0, 0]
for i in range(1, SIZE):
    values = [1, 0]
    keys[i] = values

#n = 1
for line in sys.stdin:
    data = line.strip().split()
    key, value = data
    keys[int(key)][1] += 1 # one more out degree
    values = keys[int(value)]
    values.append(int(key))
    keys[int(value)] = values

# 0 is used to store importance weight sum of nodes that havs no out-degree
#for i in range(1, SIZE):
#    if keys[i][1] == 0:
#        keys[0][0] += keys[i][0]

#print keys 
for i in range(SIZE):
    print i, keys[i]
