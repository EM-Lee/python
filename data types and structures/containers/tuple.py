### containers
# http://cs231n.github.io/python-numpy-tutorial/#python-containers

## tuple ()
'''
A tuple is an (immutable) ordered list of values. 
A tuple is in many ways similar to a list; 
one of the most important differences is that 
tuples can be used as keys in dictionaries and 
as elements of sets, while lists cannot.
'''
d = {(x, x + 1): x for x in range(10)} #create a dictionary with tuple keys
print(d)
t = (5, 6)
print(type(t))
print(d[t]) #d[5, 6]
print(d[(1, 2)])

## tuple 2
# https://www.programiz.com/python-programming/tuple
'''
A tuple is similar to a list. 
The difference between the two is that we cannot change the elements of a tuple 
once it is assigned whereas in a list, elements can be changed.
'''

# advantages of tuple over list
'''
Since, tuples are quite similiar to lists, b
oth of them are used in similar situations as well.

However, there are certain advantages of implementing a tuple over a list. 
Below listed are some of the main advantages:

- We generally use tuple for heterogeneous (different) datatypes and 
list for homogeneous (similar) datatypes.
- Since tuple are immutable, iterating through tuple is faster than with list. 
So there is a slight performance boost.
- Tuples that contain immutable elements can be used as key for a dictionary. 
With list, this is not possible.
- If you have data that doesn't change, 
implementing it as tuple will guarantee that it remains write-protected.

'''

# how to create
print('')
my_tuple = ()
print(my_tuple)
my_tuple = (1, 2, 3)
print(my_tuple)
my_tuple = (1, "Hello", 3.4)
print(my_tuple)
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
my_tuple = 3, 4.6, "dog" #can be created without parentheses, aka tuple packing
print(my_tuple)
a, b, c = my_tuple #tuple unpacking
print(a)
print(b)
print(c)

# Creating a tuple with one element is a bit tricky.
# Having one element within parentheses is not enough. 
# We will need a trailing comma to indicate that it is in fact a tuple.
print('')
my_tuple = ("hello")
print(type(my_tuple))
my_tuple = ("hello", ) #need a comma at the end
print(type(my_tuple))
my_tuple = "hello", #parentheses is optional
print(type(my_tuple))

# indexing
print('')
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])
print(my_tuple[5])
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3)) #nested tuple
print(n_tuple[0][3])
print(n_tuple[1][1])

# negative indexing
print('')
print(my_tuple[-1])
print(my_tuple[-6])

# slicing
print('')
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[1:4])
print(my_tuple[:-7])
print(my_tuple[7:])
print(my_tuple[:])

# changing
# Unlike lists, tuples are immutable.
# This means that elements of a tuple cannot be changed once it has been assigned. 
# But, if the element is itself a mutable datatype like list, 
# its nested items can be changed.

# We can also assign a tuple to different values (reassignment).
print('')
my_tuple = (4, 2, 3, [6, 5])
print(my_tuple)
my_tuple[3][0] = 9
print(my_tuple)
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple)

# concatenation & repeat
print('')
print((1, 2, 3) + (4, 5, 6))
print(("repeat") * 3)
print(("repeat", ) * 3)

# deleting
# As discussed, we cannot change the elements in a tuple. 
# That also means we cannot delete or remove items from a tuple.
# But deleting a tuple entirely is possible using the keyword del.
print('')
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
#del my_tuple[3] #TypeError
del my_tuple
#print(my_tuple)

# tuple methods
# count(), index()
print('')
my_tuple = ('a', 'p', 'p', 'l', 'e')
print(my_tuple.count('p'))
print(my_tuple.index('l'))

# membership test
print('')
my_tuple = ('a', 'p', 'p', 'l', 'e')
print('a' in my_tuple)
print('b' in my_tuple)
print('g' not in my_tuple)

# iterating
print('')
for name in ('John', 'Kate'):
    print("Hello", name)














