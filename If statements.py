#If statements 
number = 7 
if number % 2 == 0: #if you divide the number by 2 and the leftover is 0
    print("the number is even")
else: 
    print("the number is odd")
 
#Extending the idea of ifelse statements: ELIF
age = 89
#program goes and checks if age is under 90; 
if age >= 90:
     age_cat = "90+" #you can define a new variable within a loop
elif age >=80:
    age_cat = "80+"
elif age >= 70: 
    age_cat = "70-80"
elif age >=60:
    age_cat = "60-70"
else: 
    age_cat = "60-"

print("Your age category is", age_cat)

#nested ifelse statements (conditions)
number = 11
if number > 0: 
    print("the number is positive", number)
    if number % 2 == 0: #if you divide the number by 2 and the leftover is 0
       print("the number is even")
    else: 
       print("the number is odd")
else:
    print("the number is negative or 0", number)

age = 18 
income = 10000
if age >= 16 and income >= 5000:
    print("person is allowed to buy a car")
else:
    print("Person is not allowed to buy a car")

#Breaking a for loop 

for num in range(1,10):
    if num == 5:
        print(num)
        break
fruits = ["apples", "bananas", "kiwis", "strawberries", "tomato"]

for fruit in fruits:
    if fruit == "kiwis":
        print(fruit)
    elif fruit == "strawberries":
        print("this is strawberries, you are allergic!") 
        break   
    
