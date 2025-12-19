#add elements to the end of a list
l = [1,2,3,4,5]
l.append(6)
print("Updated List:",l)

#removing of an element by index
l.pop(2)
print("List after removing an element:",l)

#list indexing
lst = [1, 2, 3, 4, 5]
lst[1:3] = [10, 20]
print(lst)
#Output= [1,10,20,4,5]

#is elment exists in a list
n = int(input("enter the elements to be search:"))
if n in lst:
    print("Element exists!!!😍")
else:
    print("element not exist😒")
    

#function to remove duplicates
def duplicate_rm(l):
    new_list = []
    for elements in l:
        if elements not in new_list:
            new_list.append(elements)
    return new_list
 