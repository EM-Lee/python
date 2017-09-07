#01 Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
print('Q1 ----- ')
fLine = '+' + ' - ' * 4 + '+' + ' - ' * 4 + '+'
sLine = '|' + ' ' * 12 + '|' + ' ' * 12 + '|'

print(fLine)
for i in range(1, 5): print(sLine)
print(fLine)
for i in range(1, 5): print(sLine)
print(fLine)

#02 Write a function that draws a similar grid
### with four rows and four columns.
print('')
print('Q2 ----- ')
fLine = '+' + ' - ' * 4
sLine = '|' + ' ' * 12

for i in range(1, 5):
    print(fLine * 4, '+')
    for j in range(1, 5): print(sLine * 4, '|')
print(fLine * 4, '+')
