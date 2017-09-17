### containers
# https://www.programiz.com/python-programming/set

## set2 {}
'''
A set is an unordered collection of items. 
Every element is unique (no duplicates) and 
must be immutable (which cannot be changed).

However, the set itself is mutable. 
We can add or remove items from it.

Sets can be used to perform mathematical set operations 
like union, intersection, symmetric difference etc.
'''

## how to create
# set of integers
my_set = {1, 2, 3}
print(my_set)
# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set does not have duplicates
print('')
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# my_set = {1, 2, [3, 4]}

# we can make set from a list
print('')
my_set = set([1, 2, 3, 2])
print(my_set)

# Creating an empty set is a bit tricky.

# Empty curly braces {} will make an empty dictionary in Python. 
# To make a set without any elements 
# we use the set() function without any argument.
print('')
a = {}
print(type(a))
a = set()
print(type(a))

## how to change a set
# add(), update()
# Sets are mutable. 
# But since they are unordered, indexing have no meaning.
# We cannot access or change an element of set 
# using indexing or slicing. Set does not support it.
print('')
my_set = {1, 3}
print(my_set)

# my_set[0]
# add an element
my_set.add(2)
print(my_set)
# add multiple elements
my_set.update([2, 3, 4])
print(my_set)
# add list & set
my_set.update([4, 5], {1, 6, 8})
print(my_set)

## how to remove elements
# discard(), remove()
print('')
my_set = {1, 3, 4, 5, 6}
print(my_set)
my_set.discard(4)
print(my_set)
my_set.remove(6)
print(my_set)
my_set.discard(2)
print(my_set)
# my_set.remove(2)

# pop(): remove & return an element
# Set being unordered, there is no way of determining 
# which item will be popped. 
# It is completely arbitrary.
# We can also remove all items from a set using clear().
print('')
my_set = set("HelloWorld")
print(my_set)
print(my_set.pop())
my_set.pop()
print(my_set)
my_set.clear()
print(my_set)

## set operations
print('')
A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8}
print('A =', A)
print('B =', B)
print(A | B)
print(A.union(B))
print(B.union(A))
print(A & B)
print(A.intersection(B))
print(B.intersection(A))
print(A - B)
print(A.difference(B)) #A-B
print(B - A)
print(B.difference(A)) #B - A
print(A ^ B)
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

## test if an item exists
print('')
my_set = set("apple")
print('a' in my_set)
print('p' not in my_set)

## iterating throug a set
print('')
for letter in set("apple"):
    print(letter)

## frozenset
# Frozenset is a new class that has the characteristics of a set, 
# but its elements cannot be changed once assigned. 
# While tuples are immutable lists, frozensets are immutable sets.
# Sets being mutable are unhashable, so they can't be used as dictionary keys. 
# On the other hand, frozensets are hashable and can be used as keys to a dictionary.
# Frozensets can be created using the function frozenset().
# This datatype supports methods like copy(), difference(), intersection(), 
# isdisjoint(), issubset(), issuperset(), symmetric_difference() and union(). 
# Being immutable it does not have method that add or remove elements.
print('')
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
print('A =', A)
print('B =', B)
print(A.isdisjoint(B)) #isdisjoint(): return True if two sets have a null intersection
print(A.difference(B))
print(A | B)
# A.add(3)










