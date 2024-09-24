import pandas as pd 
data_csv = pd.read_csv("Student_performance_data _.csv")
print(data_csv)

#data exploration and preprocessing 
print(data_csv.info())
print(data_csv.head()) #prints all 5 rows but not all columns
print(data_csv.head(100)) #top 100 observations in the data 
print(data_csv.tail(20)) #print the last 20 columns 

#data aggegation, filtering, sorting and grouping 
#use pandas

#create a dataframe with simple data: 
data = pd.DataFrame({'Name' : ["Anna", "Karen", "John", "Alice", "Kevin", "Sanna", "Bob", "Emily"],
                     'Age' : [35, 30, 57, 65, 25, 19, 20, 65],
                     'Salary' : [2000, 6000, 145000, 17000, 30000, 1000, 12000, 10000], 
                     'Department': ["Tech", "Tech", "Tech", "Healthcare", "Operations", "Operations", "Tech", "Sales"]})

#ascending: smallest values at the top and values increasing;
print("\n", data.sort_values(by = "Salary", ascending=True)) #"\n" is a newline character 
print("\n", data.sort_values(by = "Salary", ascending=False)) #descending, highest on top 

#Grouping data 
#What is the number of employees per department? 
print(data.groupby("Department")["Name"].count()) #count the number of employees by department
print(data.groupby("Department")["Salary"].mean()) #what is the salary mean per department 
print(data.groupby("Department")["Salary"].min()) #what is the salary min per department 
print(data.groupby("Department")["Age"].max()) #what is the age max per department 

#selecting observations based on criteria 
#select people whose salary is larger than 100k 

print(data[data["Salary"] > 2000]) #remove all observations that are below 1000
#add an extra condition: 
print(data[(data["Salary"] > 2000) and (data["Salary"] < 145000)]) #satisfying multiple conditions 
#how to filter your data not based on larger/smaller, but specific values 
print("\n", data[data["Age"].isin([30,65])])

#Descriptive statistics 
print(data_csv) 
#sample should be a true and unbiased representation of the population -> you establish this via looking at the distribution; 
#can also visualize data in order to show it to stakeholders; 
#represent data in a clear way; 

data1 = [100, 20, 5, 67, 40, -55, 134, 0.98]

print(len(data1))
