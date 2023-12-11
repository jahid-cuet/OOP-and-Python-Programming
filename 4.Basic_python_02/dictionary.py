numbers = [12, 56 , 98, 78, 56, 12, 26, 98]
person1 = ['Kala Chan', 'kalipur', 23, 'student']
# key value pair
# dictionary
# object
# hash table
# overlap with set
# {key: value, key: value, key: value}
person = {'name': 'Kala Pakhi', 'address': 'Kaliapur', 'age': 23, 'job': 'facebooker'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language'] = 'python'
person['name'] = 'sada pakhi'
del person['age']
print(person)

# special dictionary looping
for key, value in person.items():
    print(key, value)



    # From conceptual session
    """ 
clear() || copy() || keys() || values() || items() || pop() || fromkeys() || get()
"""

#clear()
my_dict = {"name": "Alice", "age": 30}
my_dict.clear()
print(my_dict)

#copy
original_dict = {"name": "Alice", "age": 30}
copied_dict = original_dict.copy()
print(copied_dict)

#keys
my_dict = {"name": "Alice", "age": 30}
keys = my_dict.keys()
for key in keys:
    print(key)

#values
my_dict = {"name": "Alice", "age": 30}
values = my_dict.values()
for val in values:
    print(val)

#items
my_dict = {"name": "Alice", "age": 30}
items = my_dict.items()

for p in items:
    for val in p:
        print(val)