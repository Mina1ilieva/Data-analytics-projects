#Often, we get our data not in one file, but in multiple files 
import pandas as pd
import numpy as np
data1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D', 'E', 'F'],
                      'value1': [1, 2, 3, 4, 5, 6]})
data2 = pd.DataFrame({'key': ['C', 'D', 'E', 'F', 'G', 'H'], 
                      'value2': [8,9,10,11,12,13]})

#print(data1)
#print(data2)

merge_innerjoin = pd.merge(data1, data2, on = 'key', how = "inner")
print(merge_innerjoin) #merge data in terms of inner joins; 

merge_leftjoin = pd.merge(data1, data2, on = 'key', how = "left")
print(merge_leftjoin) #getting all the values/keys in innerjoin + the ones from the left join

merge_rightjoin = pd.merge(data1, data2, on = 'key', how = "right")
print(merge_rightjoin) 

merge_leftantijoin = pd.merge(data1, data2, on = 'key', how = "left", indicator= True) #shows whether the observation belongs to left table only 
#or matching part; 
print(merge_leftantijoin) 

merge_leftantijoin_ready = merge_leftantijoin[merge_leftantijoin["_merge"] == 'left_only'] #will give us all the observations on the left 
#merge_leftantijoin_ready = merge_leftantijoin_ready.drop("merge_", axis=1)
print(merge_leftantijoin_ready)

merge_rightantijoin = pd.merge(data1, data2, on = "key", how = "right", indicator= True)
merge_rightantijoin_ready = merge_rightantijoin[merge_rightantijoin["_merge"] == "right_only"]
print(merge_rightantijoin_ready)
