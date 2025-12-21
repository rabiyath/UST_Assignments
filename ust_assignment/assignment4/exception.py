#Write a Python program to handle a ZeroDivisionError.
try:
    num1 = int(input("enter a number:"))
    num2 = int(input("Enter 2nd number:"))
    
    result = num1 / num2
    print("Result=",result)
    
except ZeroDivisionError:
    print("Division by zero not acceptable!!🤦‍♂️")

finally:
    print("Program completed")
    
    
#Write a program that accepts user input and handles a ValueError if the input is not an integer.
try:
    num1 = int(input("Enetr any value:"))
    
except ValueError:
    print("Fool...enter a integer value....🤷‍♂️")
    
else:
    print("Number:",num1)
    
finally:
    print("Completed...!!!")
    
#Write a program to open a file and handle a FileNotFoundError.
try:
    f = open("abc.txt")
except FileNotFoundError:
    print("File not found...choose anouther one...👍")
    
else:
    a = f.read(5)
    print(a)
finally:
    print("Completed....")
    
#Write a Python program that uses try, except, else, and finally blocks.
try:
    num1 = int(input("Enetr any value:"))
    
except ValueError:
    print("Fool...enter a integer value....🤷‍♂️")
    
else:
    print("Number:",num1)
    
finally:
    print("Completed...!!!")
    
#Write a program to handle multiple exceptions in a single try block.
try:
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter 2nd number:"))

except (ZeroDivisionError,ValueError):
    print("Enter a value or division by zero is not possible 🤦‍♂️ ")

else:
    result = num1 / num2
    print("Result = ",result)
    
finally:
    print("Completed...👌")
    