#How does the map() function work in Python? Give an example where you square each number in a list.
#map() function works like map(function, iterable)
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))

print(squared)


#What is the output of the following code?
from functools import reduce
result = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(result)
#output=24

#How would you use the map() function to convert all string elements of a list to uppercase?
words = ["python", "java", "fastapi"]
upper_words = list(map(lambda x: x.upper(), words))
print(upper_words)


#Write a Python program that uses reduce() to find the greatest common divisor (GCD) of a list of numbers.
from functools import reduce
from math import gcd

numbers = [24, 36, 60]
result = reduce(gcd, numbers)
print("GCD of the list is:", result)

#Difference between map() and filter()
#map()         vs      filter()
#change data         Remove unwanted data



