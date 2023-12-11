# Capitalize()| upper()| lower() |casefold() |find() |replace
# immutable+iterable
# a="hello"
# a[0]="G"  indexing NOt possible
# for ch in a:
#     print(ch,end="")  #print in one line for iterable and iterable possible
# print()  #its used for space
#Cpitalize
# print(a.capitalize()) #1st character will be capital
# print(a.upper())
# print(a.lower())
# print(a.casefold())
# text="hello,jahid"
# print(text.find('j')) # find use for finding a letter or something
a="phiiiitron"
print(a.count('i'))

from collections import Counter #module is built in function
print(Counter(*a))