#Write a Python program using map() to convert a list of integers into their squares.
l = [1,2,3,4]
squared = list(map(lambda x:x**2 , l))
print("Squared list:",squared)

#Write a program using map() to convert all strings in a list to uppercase.
name = ["messi","ronaldo","neymar"]
upper_name = list(map(lambda x:x.upper(),name))
print(upper_name)

#Given a list of temperatures in Celsius, use map() to convert them to Fahrenheit.
temp = [100,40,50,30,20]
cels = list(map(lambda x:(x*9/5)+32 ,temp))
print(cels)

#Write a program using map() to calculate the length of each word in a list of strings.
word = ["Apple","Banana","Grape","Avocado"]
len_word = list(map(len,word))
print(len_word)

#Use map() to add 10 to each element of a given list of numbers.
number = [1,2,3,4,5]
added10 = list(map(lambda x:x+10 , number))
print(added10)
