### basic data types
# http://cs231n.github.io/python-numpy-tutorial/#python-basic

## strings
hello = 'hello'
world = "world"
print(hello)
print(len(hello))
hw = hello + ' ' + world
print(hw)
hw12 = '%s %s %d' %(hello, world, 12)
print(hw12)

# useful methods
print('')
s = "hello"
print(s.capitalize())
print(s.upper())
print(s.rjust(7))
print(s.center(7))
print(s.replace('l', '(ell)'))
print('   world '.strip())

## more about string
# https://www.programiz.com/python-programming/string

# how to creat a string
print('')
my_string = 'Hello'
print(type(my_string))
print(my_string)
my_string = "Hello"
print(my_string)
my_string = '''Hello'''
print(my_string)
my_string = '''Hello, welcome to
            the world of Python'''
print(my_string)

# how to access a characters in a string
print('')
str = 'programiz'
print('str =', str)
print('str[0] =', str[0]) #first character
print('str[-1] =', str[-1]) #last character
print('str[1:5] =', str[1:5]) #slicing 2nd to 5th character
print('str[5:-2] =', str[5:-2]) #slicing 6th to 2nd last character

# how to change or delete a string
'''
Strings are immutable.
This means that elements of a string cannot be changed
once it has been assigned.
We can simply reassign different strings to the same name.

We cannot delete or remove characters from a string.
But deleting the string entirely is possible using the keyword del.
'''
# my_sting[5] = 'a' #TypeError: 'str' does not support item assignment
# del my_string[1] #TypeError: 'str' does not support item deletion
del my_string

## string operations
# concatenation of two or more strings
print('')
str1 = 'Hello'
str2 = 'World!'
print('str1 + str2 =', str1 + str2)
print('str1 * 3 =', str1 * 3)

'''
Writing two string literals together also
concatenates them like + operator.
If we want to concatenate strings in different lines,
we can use parentheses.

>>> # two string literals together
>>> 'Hello ''World!'
'Hello World!'

>>> # using parentheses
>>> s = ('Hello '
...      'World')
>>> s
'Hello World'
'''

# iterating through string
print('')
count = 0
for letter in 'Hello World':
    if (letter == 'l'):
        count += 1
        #print(count, 'letters found')
    #print(count, 'letters found')
print(count, 'letters found') #diferent printing depending on the location

# string membership test
print('')
print('a' in 'program')
print('at' not in 'battle')

# built-in functions to work with
print('')
str = 'cold'
list_enumerate = list(enumerate(str))
print('list(enumerate(str) =', list_enumerate)
print('len(str) =', len(str))
