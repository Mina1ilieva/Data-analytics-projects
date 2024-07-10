import matplotlib.pyplot as plt

#1. Line plots - a great way to visualize TRENDS AND TIME SERIES 
#x_values = [1,2,3,4,5,6,7,8,9,10]
#y_values = [1,4,6,9,10,11,12,54,10,21]

#plt.plot(x_values, y_values, color = 'green')

#plt.xlabel('Time (hours)')
#plt.ylabel('Stock prices (USD)')
#plt.title("Title Placeholder")

#plt.show()

#2. Scatterplots - a relationship between two variables
#plt.scatter(x_values, y_values, color = 'red')

#plt.xlabel('Number of albums in a playlist')
#plt.ylabel('Weekly active users')
#plt.title("Title Placeholder")

#plt.show()

#3. Bar charts - comparing different values (e.g. for categorical data)
#animals = ["cat", "dog", "horse", "mouse"]
#animal_weight = [10, 30, 200, 1]

#plt.bar(animals, animal_weight, color = "forestgreen")

#plt.xlabel('Animal')
#plt.ylabel('Weight of animal')
#plt.title("Weight per animal")

#plt.show()

#4. Histograms - distribution of numerical data
import numpy as np
x_normal = np.random.normal(0,1,10000) #generating a normal distribution
plt.hist(x_normal, color = "forestgreen")
plt.xlabel("X")
plt.ylabel("Probability")
plt.title("Randomly Sampled data from standard normal distribution")
plt.show()

#Population distribution 
from scipy.stats import norm
x_values = np.arange(-5, 5, 0.01)
y_values = norm.pdf(x_values)
