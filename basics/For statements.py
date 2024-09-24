#For loops 
#Help you go through different arrays, etc; 
fruits = ["banana", "apples", "pineapples", "kiwis"]
for i in fruits:
    print(i + " is a fruit")

#we can also loop through a string. (e.g. we want to see all the chars 
# defining the string)   
string_= "banana"
for i in string_:
    print(i)
#nested for loops:
for fruit in fruits:
    print("first for loop. We are spelling out the following fruit:" + fruit)
    for char in fruit: 
        print(char)

for num in range(1, 10):
    print(num)
#using for loops with range 
for num in range(10): #it does not include the last value of the range
    print("This statement to be printed 10 times") #ENUMERATING the values from 1 to 10 

#Enumerate two types of loops:

for i in range(1, 15):
    for j in range (1, 15):
        print("i = ", i, "j = ", j)
        print(i + j)    
#takes a value for i, then combines with all possible values for j; 


    
