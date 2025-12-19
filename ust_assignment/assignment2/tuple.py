#we can't modify tuple after its creation, bcz tuple are immutable,cant change its elements and size

#accessing second last element
t = (1,2,3,4,5)
print(t[-2])
#output = 4

#Differences bw List and tuple
# list are mutable while tuple are immutable, tuple are faster than list,tuple required less memmory than list

#Given the tuple t = (1, 2, 3, 4), how can you change the value 3 to 100?
t = (1,2,3,4)
l = list(t)
l[2] = 100
t = tuple(l)
print(t)

#Write a Python function that takes a tuple of numbers and returns the sum of all its elements.
def tuple_sum(t):
    total = 0
    for a in t:
        total += a
        
    return total