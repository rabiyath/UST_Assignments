#Write a Python program to create a text file and write multiple lines into it.
l = ["Apple","Banana","Mango","Cherry"]
f = open("word.txt","w")
for element in l:
    f.write(element + '\n')
    
f.close()

#Write a program to read the contents of a text file line by line.
f = open("word.txt")
for element in f:
    print(element,end="")
    
f.close()

#Write a Python program to count the number of lines, words, and characters in a text file.
f = open("word.txt", "r")

line_count = 0
word_count = 0
char_count = 0

for line in f:
    line_count += 1
    word_count += len(line.split())
    char_count += len(line)

f.close()

print("Number of lines:", line_count)
print("Number of words:", word_count)
print("Number of characters:", char_count)

#Write a program to copy the contents of one text file into another file.
f1 = open("word.txt")
f2 = open("copy.txt","w")
for element in f1:
    f2.write(element)
    
f1.close()
f2.close()

#Write a Python program to search for a specific word in a text file and display the line numbers where it appears.
word = input("Eneter specific word to be search:")
f1 = open("word.txt","r")
line = 1
found = False
for element in f1:
    if word in element:
        print("Element found at:",line)
        found = True
    line += 1
    
if not found:
    print("Element not found 😒")
        
f1.close()
