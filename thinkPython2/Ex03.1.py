#01 Write a function named right_justify that takes a string
### named s as a parameter and prints the string
### with enough leading spaces so that
### the last letter of the string is in column 70 of the display.
print('Q1 -----')
def right_justify(s):
    if type(s) == str:
        length = len(s)
        print(' ' * (70 - length), s)
    elif type(s) == int:
        length = len(str(s))
        print(' ' * (70 - length), s)
right_justify('hello')
right_justify(12345)

print('')
print('Q1 ----- another way')
def right_justify2(s):
    if type(s) == str:
        print(s.rjust(70))
    if type(s) == int:
        print(str(s).rjust(70))
right_justify('hello')
right_justify(12345)

print('')
print('Q1 ----- one more way')
# http://thomas-cokelaer.info/tutorials/python/print.html
# see section 6.6.4. The width option
def right_justify3(s):
    if type(s) == str:
        print("%70s" % s)
    if type(s) == int:
        print("%70s" % str(s))
right_justify('hello')
right_justify(12345)
