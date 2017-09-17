### containers
# https://www.datacamp.com/community/tutorials/18-most-common-python-list-questions-learn-python/#gs.XS21vCM

## list2 []
'''
Lists are one of the four built-in data structures in Python,
together with tuples, dictionaries, and sets.
They are used to store an ordered collection of items,
which might be of different types but usually they aren’t.
The elements that are contained within a list
are separated by commas and enclosed in square brackets.
'''

# list with the same type of elements
zoo = ['bear', 'lion', 'panda', 'zebra']
print('type(zoo) =', type(zoo))
print(zoo)

# list with the different type of elements
biggerZoo = ['bear', 'lion', 'panda', 'zebra', \
             ['chimpanzees', 'gorillas', 'orangutans', 'gibbons']]
print('type(biggerZoo) =', type(biggerZoo))
print(biggerZoo)

'''
Since lists in Python store ordered collections of items or objects,
we can say that they are sequence types,
exactly because they behave like a sequence.
Other types that are also considered to be sequence types are
strings and tuples.

You might wonder what’s so special about sequence types.
Well, in simple words, it means that
the program can iterate over them!
This is why lists, strings, tuples, and sets are called “iterables”.
'''

# how to select an element
print('')
oneZooAnimal = biggerZoo[0]
print(oneZooAnimal)

# how to get the last element
print('')
monkeys = biggerZoo[-1]
print(monkeys)
zebra = biggerZoo[-2]
print(zebra)

# index out of range error
print('')
# print(biggerZoo[6])

# slice notation
print('')
someZooAnimals = biggerZoo[2:]
print(someZooAnimals)
otherZooAnimals = biggerZoo[:2]
print(otherZooAnimals)

# with step value
print('')
print(biggerZoo[2::2])
print(biggerZoo[1::3])

# how to randomly select an element
print('')
from random import choice
list = ['a', 'b', 'c', 'd']
print(choice(list))

# with randrange()
print('')
from random import randrange
randomLetters = ['a', 'b', 'c', 'd']
randomIndex = randrange(0, len(randomLetters))
print(randomLetters[randomIndex])

## how to transform into other data structures
# how to convert to a string
print('')
listOfStrings = ['One', 'Two', 'Three']
strOfStrings = ''.join(listOfStrings)
print(strOfStrings)

listOfNumbers = [1, 2, 3]
strOfNumbers = ''.join(str(n) for n in listOfNumbers)
print(strOfNumbers)

# to a tuple
print(tuple(listOfStrings))
# to a set
print(set(listOfStrings))

# to a dictionary
# zip()
print('')
smartPhones = ['iPhone', 'apple', 'galaxy', 'samsung']
print(dict(zip(smartPhones[0::2], smartPhones[1::2])))

# iterator
print('')
a = [1, 2, 3, 4, 5]
i = iter(a)
print(dict(zip(i, i)))

# len(), append(), extend()
print('')
shortList = [1, 2, 3]
longerList = [1, 2, 3, 4, 5, 6]
print('len(shortList) =', len(shortList))
print('len(longerList) =', len(longerList))
shortList.append([4, 5])
print(shortList)
longerList.extend([4, 5])
print(longerList)

# how to concatenate
print('')
plusList = shortList + [4, 5]
print(plusList)

# how to sort
# sort(), sorted()
print('')
num1 = [30, 15, 12, 48, 1, 27]
num2 = [46, 75, 64]
num1.sort()
print(num1)
print(sorted(num2))

# how to clone or copy
print('')
phones = smartPhones[0::2]
print(phones)
#smartPhones2 = list(smartPhones)
#print(smartPhones2)
import copy as c
smartPhones3 = c.copy(smartPhones)
print(smartPhones3)
smartPhones4 = c.deepcopy(smartPhones)
print(smartPhones4)

# simple(shallow) vs. deepcopy
# https://www.python-course.eu/python3_deep_copy.php
print('')
objectList = ['a', 'b', ['ab', 'ba']]
print('objectList =', objectList)
copiedList = objectList[:]
print('copiedList =', copiedList)
copiedList[0] = 'c'
copiedList[2][1] = 'd'
print('copiedList =', copiedList)
print('objectList =', objectList)

# list comprehension
# for lambda: https://www.python-course.eu/python3_lambda.php
print('')
print([x ** 2 for x in range(10)])
print([x ** 2 for x in range(10) if x % 2 == 0])
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([(lambda x : x * x)(x) for x in myList])

# counting the occurrences of one item
print('')
print([1, 2, 9, 4, 5, 4, 1].count(4))
list = ["d", "a", "t", "a", "c", "a", "m", "p"]
print(list.count("a"))

# counting all items with count()
print('')
list = ["a", "b", "b"]
print([[x, list.count(x)] for x in set(list)])

# counting all items with counter()
print('')
from collections import Counter
list = ["a", "b", "b"]
print(Counter(list))

# how to split into evenly sized chunks
# print('')
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(x)
# y = zip(*[iter(x)]*3)
# print(y)
# print(list(y))

# how to loop over a list
print('')
myList = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10]]
for x in myList:
    if len(x) == 3:
        print(x)

print('')
myList = [3, 4, 5, 6]
for i, val in enumerate(myList):
    print(i, val)

# how to create flat lists out of lists
print('')
list = [[1, 2], [3, 4], [5, 6]]
print(list)
s = sum(list, [])
print(s)

print('')
from functools import reduce
listOfLists = [[1, 2], [3, 4], [5, 6]]
print(reduce(lambda x, y: x + y, listOfLists))
print([item for sublist in listOfLists for item in sublist])

# iPython
# https://www.datacamp.com/community/blog/ipython-jupyter#gs.5LwDiic
