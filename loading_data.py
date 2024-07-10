import pandas as pd 
data_csv = pd.read_csv("Student_performance_data _.csv") #always put the name as a string 
print(data_csv)
#data_excel = pd.read_excel("Student_performance_data _ - Copy.xlsx", sheet_name= "Student_performance_data _ - Copy")
#print(data_excel)

#data_json = pd.read_json("file_name.json")

#load SQL databases 
#import sqlite3 
#connection_db = sqlite3.connect("database_name.db")
#query_1 = "SELECT col_1 FROM table_name" #query will select the column from the table 
#query_2 = "SELECT * FROM table_name " #* SELECTS ALL COLUMNS WITHIN A TABLE
#data_sql = pd.read_sql(query_2, connection_db) #specify the query and connection 

#Exploring and preprocessing the data 
#identify and drop missing values, etc 

#1. Get a snapshot of the data
print(data_csv.head())
print(data_csv.head(100)) #print the first 100 observations
print(data_csv.head(20)) #print the first 20 observations
print(data_csv.tail(20)) #print the last 20 rows from the bottom up 

#2. More info about the data 
print(data_csv.info())
print(data_csv.dropna())
print(data_csv.fillna("NULL"))

#dropping duplicates
print(data_csv.drop_duplicates())

#How to access certain rows in a dataframe depending on their index type 
print(data_csv.iloc[10]) #fetching the 10th row of the dataframe 
print(data_csv.loc[:, 'A2'])

data = pd.DataFrame({'A1': [1,2,3],
                    'A2' : [4,5,6],
                    'A3' : [7,8,9]},
                    index=['X', 'Y', 'Z'])
print(data)

print(data.loc["X"])
print(data.loc['Y', 'A2']) #specifying the index of the row and the column 

