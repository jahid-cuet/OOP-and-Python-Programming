def multiple():
    return 3, 4
# print(multiple())
things = 'pen','tripod', 'water bottle', 'charger', 'phone', 'web cam', 'sunglass'
# print(type(things))
# print(things[0])
# print(things[-2])
# print(things[3:6])
if 'phone' in things:
    print('exists')
for item in things:
    print(item)

# things[0]='wagon'
# print(things)

items = ('book', 'monitor')

# ignore
print(len(things))
mega = ([2, 3,4], [6,8,9,5])
# print(type(mega))
print(mega[0])
mega[0][1]=666
print(mega)

# From conceptual
""" 
append() || clear() || copy() || count() || insert() || pop() || remove() || sort() || reverse()


append(): Not valid for tuples because it modifies the tuple, and tuples are immutable.

clear(): Not valid for tuples because it modifies the tuple, and tuples are immutable.

copy(): Valid for tuples. It creates a shallow copy of the tuple, which means it returns a new tuple with the same elements.

count(): Valid for tuples. It counts the number of occurrences of a specified element in the tuple.

insert(): Not valid for tuples because it modifies the tuple, and tuples are immutable.

pop(): Not valid for tuples because it modifies the tuple, and tuples are immutable.

remove(): Not valid for tuples because it modifies the tuple, and tuples are immutable.

sort(): Not valid for tuples because it modifies the tuple, and tuples are immutable.

reverse(): Not valid for tuples because it modifies the tuple, and tuples are immutable.

"""
