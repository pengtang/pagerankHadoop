# Calculate the pageRank value.
# Current version needs to run job manually and see if it's less than the threshold(after running job2.sh, run combine_then_update_iter_val.py see the difference)
# //TODO  Need to figure out how to use bc in order to enable the floating point condition in shell script.

hadoop fs -rm -r output2
#!/bin/bash                                                                                         
# running the filter and max using hadoop-streaming API                                             
# using default configuration: pseudo-distributed mode                                              
#export HADOOP_CLASSPATH=../target/classes/                                                       

#TOTAL_ZERO=$(python total_zero_degree.py)
#echo $TOTAL_ZERO
      
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar\
        -cmdenv TOTAL_ZERO=$(python total_zero_degree.py)\
        -cmdenv TOTAL_USER=$(python total_user.py)\
        -input output1/output1 -output output2\
        -file job2reducer.py\
        -file output1\
        -file iterative_value\
        -mapper "cat" -reducer "python job2reducer.py"

rm output2
hadoop fs -getmerge output2 output2
hadoop fs -copyFromLocal output2 output2/output2
#hadoop fs -copyToLocal output2/p* output2
