#Write a Python program using filter() to extract all even numbers from a list.
num = [x for x in range(1,11)]
even = list(filter(lambda x:x%2==0,num))
print("Even List=",even)

#Write a program using filter() to select all words from a list that start with a vowel.
words = ["Apple","Banana","Eat","Ice","Mango"]
vowel = list(filter(lambda x:x[0].lower() in "aeiou",words))
print("Starting with Vowels:",vowel)

#Given a list of integers, use filter() to remove all negative numbers.
num1 = [-1,-2,4,5,-7,10]
positive = list(filter(lambda x:x if x>0 else None,num1))
print("Positive list:",positive)

#Write a program using filter() to find numbers greater than 50 from a list.
num2 = [10,30,50,51,66,77,88,90,22]
grt50 = list(filter(lambda x:x>50,num2))
print("Number > 50:",grt50)

#Use filter() to extract all palindromic strings from a list.
string1 = ["malayalam","english","ardra","hindhi"]
pal = list(filter(lambda x:x==x[::-1],string1))
print("Palindrome:",pal)
