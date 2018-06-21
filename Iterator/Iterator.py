"""
Created on Wed Jun 20 09:21:33 2018

Summing up an iterator in python:
    When you call the for loop in a container/aggregate/collection
    of an iterable container, it will call its method __iter__(), which 
    will return an iterator. The created iterator will have a method called 
    __next__() which will be called to iterate over the iterator.
    
    These are four different ways you can iterate over a iterable container in python:

@author: Matheus Schaly
"""


print(type([1]))

myList1 = [1, 2, 3]
iter1 = myList1.__iter__()
print(type(iter1))

for myInt in iter1:
    print(myInt)

print()
for myInt in myList1:
    print(myInt)


print()
myList2 = [2, 4, 6]
iter2 = iter(myList2)
print(type(iter2))

for myInt in iter2:
    print(myInt)
    
for myInt in iter2: # Iterator has been exhausted
    print(myInt)


print()
myList3 = [3, 6, 9]
iter3 = myList3.__iter__()
print(type(iter3))
print(iter3.__next__())
print(iter3.__next__())
print(iter3.__next__())
# print(iter3.__next__()) # Iterator has been exhausted


print()
myList4 = [4, 8, 12]
print(type(myList4.__iter__()))
for myInt in myList4.__iter__():
    print(myInt)