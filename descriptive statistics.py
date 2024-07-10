import numpy as np
import pandas as pd
data = [100, 20, 56, 234, -45, 0.98]
print(len(data))
#1. Calculating the average
print("Mean of array:", np.mean(data))

#2. Calculating the median (as a better representation if the distribution is left-or rght )
#median - the 2nd quantile and the 15th percentile;
median_ = np.median(data)
mean_ = np.mean(data)
print("Median of array:", median_)
#mean and median are not very close, so we might be dealing with a skewed distribution; 
import scipy
from scipy import stats 
mode_ = stats.mode(data)
print("Mode of array:", mode_)
#you get the value and how many times it appears; 

#3. Variance and stdev 
#3.1. Variance - the dispersion of the data. Quantifies how far the data is from the mean. Higher variance indicates greater data variability; 
#3.2. STDEV - quare root of the variance; Makes it more preferred whenever it comes to results interpretation; 
#STDEV - PREFERRED AS THE AVERAGE DISTANCE FROM THE MEAN;

variance_ = np.var(data)
std_ = np.std(data)
print("Variance of array:", variance_)
print("Standard deviation of array", std_)

data_csv = pd.read_csv("Student_performance_data _ - Copy.csv")
print(data_csv.describe()) #this describes all the different columns;
#print(data_csv.describe(np.number)) #can include a certain data type only
print(data_csv.info())
#mean, standard deviation, min value, 25th percentile - the first quantile, 50%th percentile - the median; 
#50th percentile - the 2nd quantile; 75th percentile - the third quantile;

#For a single specific column: 
data_csv['Age'].describe()
