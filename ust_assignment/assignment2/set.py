#Remove all elements from a set
s = {1, 2, 3}
s.clear()
print(s)

# a - b means elements in a but not in b
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a - b)
# output = {1,2}

#check element in a set
s = {1,2,3,4,5}
n = int(input("Eneter the elementt to check:"))

if n in s:
    print("Elemrnt exists😍👍")
else:
    print("Not present😒")
    
    
#intersection of 2 sets:Prints common elements in two sets
a = {1,2,3,4,5}
b = {2,4,6}
result = a.intersection(b)
print("Intersected sets=",result)

#set handle duplicate value and remove it when we add it in to a set
s = {1,2,3,4}
s.add(3)
print(s)
#output {1,2,3,4}
