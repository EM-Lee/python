### basic data types
# http://cs231n.github.io/python-numpy-tutorial/#python-basic

## booleans
t = True
f = False
print(type(t))
print(t and f)
print(t or f)
print(not t)
print(t != f)

# https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Boolean_Expressions
print('')
a = 6
b = 7
c = 42
print(1, a == 6)
print(2, a == 7)
print(3, a == 6 and b == 7)
print(4, a == 7 and b == 7)
print(5, not a == 7 and b == 7)
print(6, a == 7 or b == 7)
print(7, a == 7 or b == 6)
print(8, not (a == 7 and b == 6))
print(9, not a == 7 and b == 6)

print('')
"""
When the Python interpreter looks at an or expression,
it takes the first statement and checks to see if it is true.
If the first statement is true,
then Python returns that object's value
without checking the second statement.
This is because for an or expression,
the whole thing is true if one of the values is true;
the program does not need to bother with the second statement.

On the other hand,
if the first value is evaluated as false
Python checks the second half and returns that value.
That second half determines the truth value of the whole expression
since the first half was false.
This "laziness" on the part of the interpreter is called
"short circuiting" and is a common way of evaluating boolean expressions
in many programming languages.

Similarly, for an and expression,
Python uses a short circuit technique to speed truth value evaluation.
If the first statement is false then the whole thing must be false,
so it returns that value.
Otherwise if the first value is true
it checks the second and returns that value.
"""
print('a' or 'b')
print('a' and 'b')

"""
One thing to note at this point is
that the boolean expression returns a value
indicating True or False,
but that Python considers a number of different things
to have a truth value assigned to them.
To check the truth value of any given object x,
you can use the fuction bool(x) to see its truth value.
"""
print('a' == ('a' or 'b'))
print('b' == ('a' or 'b'))
print('a' == ('a' and 'b'))
print('b' == ('a' and 'b'))
x = ('a' == ('a' or 'b'))
y = ('a' == ('a' and 'b'))
print(bool(x))
print(bool(y))

## example: password.py
name = input("What is your name? ")
password = input("What is the password? ")
if name == "Josh" and password == "Friday":
    print("Welcomd Josh!")
elif name == "Fred" and password == "Rock":
    print("Welcome Fred!")
else:
    print("I don't know you.")

## boolean strings
# http://www.pythonforbeginners.com/basics/boolean
print('')
my_string = "Hello World"
print(my_string.isalnum())		#check if all char are numbers
print(my_string.isalpha())		#check if all char in the string are alphabetic
print(my_string.isdigit())		#test if string contains digits
print(my_string.istitle())		#test if string contains title words
print(my_string.isupper())		#test if string contains upper case
print(my_string.islower())		#test if string contains lower case
print(my_string.isspace())		#test if string contains spaces
print(my_string.endswith('d'))		#test if string endswith a d
print(my_string.startswith('H'))	#test if string startswith H


