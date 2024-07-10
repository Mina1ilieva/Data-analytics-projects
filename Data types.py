#data types and variables
#integer
integer1 = 1
#float 
float1 = 1.3
#string 
string1 = "This is a string"
#boolean
bool = True
#--- excercise ---
#Integers
x_int = -110 
print(x_int)
x_int2 = 12
print(x_int2)
x_int_sum = x_int + x_int2
x_int_subs = x_int - x_int2
print("Sum of two integer values is:", x_int_sum)

#Floats:
x_float = -0.25 
x_float_int_sum = x_float+x_int
print(x_float_int_sum)
print(type(x_float_int_sum))

#strings
x_string = "Hello to the world of data science"
strings_combined = string1 + x_string
print(strings_combined)

#Arrays
x_array = [1.0, 0.25, 20, -0.009]
y_array = [3,4,4000, -0.45]
print(x_array, y_array) #you can print stuff side by side

#Lists: ELEMENTS OF DIFFERENT DATA TYPES 
x_list = [2, "a string", True, False, 45, x_int]
print(x_list)

