# you should visit this website : https://docs.python.org/3/tutorial/datastructures.html

# list, array, collection is same (simple terms)

# index =   0   1   2   3   4  5   6   7   8   9  
numbers = [45, 56, 12, 89, 87, 32, 84, 59, 46, 93]
# index = -10  -9  -8  -7  -6  -5  -4  -3  -2  -1  

print(numbers[3], numbers[-3]) 

# list( start : end ) # start from the start index and stops before the end index
print(numbers[2:6])
print(numbers[1:7])

# list(start : end : step)
print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[2:7:-1])
print(numbers[7:2:-1])
print(numbers[7:2:-2])
print(numbers[4:])
print(numbers[:5])
print(numbers[:]) # shortcut to copy a list
print(numbers[::-1]) #shortcut to reverse a list

print(b,c)


#count
my_list = [1, 2, 2, 3, 4, 2]
count = my_list.count(2)
print(count)  # Output: 3


#insert (expected two argument must)
my_list = [1, 2, 3, 4]
my_list.insert(2, 5)  # Insert 5 at index 2
print(my_list)  # Output: [1, 2, 5, 3, 4]

#pop
my_list = [1,2,3,4]
popped_element = my_list.pop(1)  # Remove and return element at index 1 (2)
popped_element_w = my_list.pop()  # Remove and return element last index
print(popped_element)  # Output: 2
print(popped_element_w)  # Output: 4
print(my_list) #[1, 3]

#reverse
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]

print(my_list[::-1]) #shortcut to reverse a list

#sort
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
my_list.sort()
print(my_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]