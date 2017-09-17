### basic data types
# http://cs231n.github.io/python-numpy-tutorial/#python-basic

## string formatting

# escape sequence
'''
If we want to print a text like -He said, "What's there?"-
we can neither use single quote or double quotes.
This will result into SyntaxError
as the text itself contains both single and double quotes.

One way to get around this problem is to use triple quotes.
Alternatively, we can use escape sequences.

An escape sequence starts with a backslash and is interpreted differently. 
'''
print('''He said, "What's there?''') #using triple quotes
print('He said, "What\'s there?"') #escaping single quotes
print("He said, \"What's there?\"") #escaping double quotes

'''
Escape Sequence	Description
\newline	Backslash and newline ignored
\\	        Backslash
\'	        Single quote
\"	        Double quote
\a	        ASCII Bell
\b	        ASCII Backspace
\f	        ASCII Formfeed
\n	        ASCII Linefeed
\r	        ASCII Carriage Return
\t	        ASCII Horizontal Tab
\v	        ASCII Vertical Tab
\ooo	        Character with octal value ooo
\ #see the linked page
'''

# some examples
print('')
print("C:\\Python32\\Lib")
print("This is printed\nin two lines.")
print("This is \x48\x45\x58 representation.")

# format method
print('')
default_order = "{}, {}, and {}".format('John', 'Bill', 'Sean')
print('\n--- Default Order ---')
print(default_order)

positional_order = "{1}, {0}, and {2}".format('John', 'Bill', 'Sean')
print('\n--- Positional Order ---')
print(positional_order)

keyword_order = "{s}, {b}, and {j}".format(j = 'John', b = 'Bill', s = 'Sean')
print('\n--- Keyword Order ---')
print(keyword_order)

# formatting integers
print("Binary representation of {0} is {0:b}".format(12))
# formatting floats
print("Exponent representation: {0:e}".format(1566.345))
# round off
print("One third is: {0:.3f}".format(1/3))
# string alignment
print("|{:<10}|{:^10}|{:>10}|".format('butter', 'bread', 'ham'))
      
# common string methods
print('')
print("PrOgRaMiZ".lower())
print("PrOgRaMiZ".upper())
print("This will split all words into a list.".split())
print(' '.join(['This', 'will', \
                'split', 'all', 'words', 'into', 'a', 'string.']))
print("Happy New Year".find('ew'))
print("Happy New Year".replace("Happy", "Brilliant"))

      
