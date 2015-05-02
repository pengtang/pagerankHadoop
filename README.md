# Twitter user/Directed graph analysis using pageRank algorithm based on Hadoop
Using pageRank algorithm to analyze twitter user, implementation based on hadoop streaming
The whole workflow is very similar to http://salsahpc.indiana.edu/csci-b649-spring-2014/projects/project3.html

**********************************************
# Raw data format
1 2

1 3

2 3

2 4

3 4

3 5
***********************************************
# Usage
1. Run job1.sh
2. Run gen_iter_value.py
3. Run job2.sh
4. Run combine_then_update_iter_val.py. If output value(sum of value difference) is greater than the threshold, goes to step 3. 
If the output value is smaller than threshold, goes to step 5.
5. Run sort.py

***********************************************
# Example final result
[4, 0.19241600000000003]

[3, 0.18625066666666665]

[5, 0.16974933333333334]

[2, 0.163584]

[0, 0.14400000000000002]

[1, 0.14400000000000002]

User/Node 4 ranks 1, with the value of 0.192
User/Node 3 ranks 2, with the value of 0.186...