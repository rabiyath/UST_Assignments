#How can you add a new key-value pair to an existing dictionary in Python?
student = {"name": "Rabiyath", "age": 24}
student["marks"] = 85
print(student)

#What happens if you try to access a key that does not exist in a dictionary?
#it shows a KeyError

#Write a Python function that takes a dictionary and returns a list of keys that have values greater than 50.
def greater50(d):
    result = []
    for key, value in d.items():
        if value > 50:
            result.append(key)
    return result

#How would you iterate over both keys and values of a dictionary in Python?
student = {"name": "Rabiyath", "age": 24, "marks": 85}

for key, value in student.items():
    print(key, ":", value)
    
#Write a Python function that merges two dictionaries.
def merge_dict(d1, d2):
    d1.update(d2)
    return d1


