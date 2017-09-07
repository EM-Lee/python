### A function object is a value you can assign
### to a variable or pass as an argument.
### For example, do_twice is a function that takes a function object
### as an argument and calls it twice:
# def do_twice(f):
#     f()
#     f()
### Here’s an example that uses do_twice to call a function named
### print_spam twice.
# def print_spam():
#     print('spam')
#     do_twice(print_spam)

#01. Type this example into a script and test it.
print('Q1 ----- ')
def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')
    do_twice(print_spam)

# print_spam() #endless loop

#02. Modify do_twice so that it takes two arguments,
### a function object and a value,
### and calls the function twice, passing the value as an argument.
print('')
print('Q2 ----- ')
def do_twice2(f, s):
    f(s)
    f(s)

def print_spam2(s):
    print(s)
    do_twice2(print_spam2, 'spam')

# print_spam2('spam') #endless loop

#03. Copy the definition of print_twice from earlier in this chapter
### to your script.
print('')
print('Q3 ----- ')
def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('hi')

#04. Use the modified version of do_twice to call print_twice twice,
### passing 'spam' as an argument.
print('')
print('Q4 ----- ')
def do_twice4(f, s):
    f(s)
    f(s)

do_twice4(print_twice, 'spam')

#05. Define a new function called do_four that takes a function object
### and a value and calls the function four times,
### passing the value as a parameter.
### There should be only two statements in the body of this function,
### not four.
print('')
print('Q5 ----- ')
def do_four(f, s):
    do_twice4(f, s)
    do_twice4(f, s)

do_four(print_twice, 'spam')
