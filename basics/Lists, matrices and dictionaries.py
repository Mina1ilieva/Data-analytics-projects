#Lists and dictionaires 
fruits = ["banana", "apples", "pineapples", "kiwis"]
# index  = [0,1,2,3,4]
print(fruits)
print(type(fruits))
#Accessing elements in the list, keeping in mind its index notation
print(fruits[0])
print(fruits[3])
print(fruits[len(fruits)-1]) #last element of a list 
print(len(fruits)) #just the length 
print(fruits[-1]) #another way to access the last element 
#Changing an element within a list 
fruits[2] = "lemons"
print(fruits)

#MATRIXES: a collection of multiple lists and arrays 
#DVs (observations) represent rows; IDs represent columns 
#rows are elements in a list 
matrix = [[4,5,6], [6,7,8], [10,22,35]]
print(matrix)
#accessing different elements in a matrix: call the column (observation) first, and then the row
print(matrix[0][0])
print(matrix[2][1])

matrix[1][2] = -99
print(matrix)

#Dictionaries: storing information in key values and pairs
resident = {"name": "Mina", "city": "New York"}
print(resident)
#accessing an element in a dictionary: 
print(resident["city"]) #using the key 
#modifying a value 
resident["city"] = "London"
print(resident)

