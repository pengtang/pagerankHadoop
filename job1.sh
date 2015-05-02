#!/bin/bash
# job1 is used to format the data, prep step to do the pagerank

# Example:
# Original data:
# 1 2
# 1 3
# 2 3
# 2 4
# 3 4
# 3 5

# After running job1
# new data:
# 0 [0, 0]	
# 1 [1, 2]	
# 2 [1, 2, 1]	
# 3 [1, 2, 1, 2]	
# 4 [1, 0, 2, 3]	
# 5 [1, 0, 3]

# Data explanation:
# where the first column is the node for the key, the list is all the information about the node
# In the list, the first column is meaningless :(, the second column means the total number of out-degree, starting from the third column, they are the in-degree nodes

hadoop fs -rm -r output1

# running the filter and max using hadoop-streaming API
# using default configuration: pseudo-distributed mode 
#export HADOOP_CLASSPATH=../target/classes/
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar\
	-input input_final/less_million -output output1\
	-file job1reducer.py\
	-mapper "cat" -reducer "python job1reducer.py"

rm output1
hadoop fs -getmerge output1 output1
hadoop fs -copyFromLocal output1 output1/output1
#hadoop fs -copyToLocal output1/p* output1

