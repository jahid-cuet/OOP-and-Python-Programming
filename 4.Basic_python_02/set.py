# list --> []
# tuple --> ()
# set --> {}
# set: unique items collection. No duplicate
numbers = [12, 56 , 98, 78, 56 , 12 , 6, 98]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(55)
numbers_set.add(12)
numbers_set.add(12)
numbers_set.add(12)
print(numbers_set)
numbers_set.remove(6)
print(numbers_set)
# numbers_set[1] = 5
for item in numbers_set:
    print(item)

if 9 in numbers_set:
    print('9 exists')
elif 98 in numbers_set:
    print('98 exists')

A = {1, 3, 5, 7}
B = {1, 2, 3, 4, 5}
print(A & B)
print( A | B) #AUB

#From concenptual session
""" 
add() || clear() || copy() || pop() || remove() || update() 

"""

#add()
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

#copy
original_set = {1, 2, 3}
copied_set = original_set.copy()
print(original_set)

#clear
my_set = {1, 2, 3}
my_set.clear()
print(my_set)

#update
my_set = {1, 2, 3}
my_set.update({3, 4, 5})
print(my_set)

#union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)
