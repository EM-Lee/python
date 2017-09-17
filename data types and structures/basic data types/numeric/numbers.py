### basic data types
# http://cs231n.github.io/python-numpy-tutorial/#python-basic

## numbers
x = 3
print(type(x))
print(x)
print(x + 1)
print(x - 1)
print(x * 2)
print(x ** 2)

x += 1
print(x)
x *= 2
print(x)
y = 2.5
print(type(y))
print(y, y + 1, y * 2, y **2)

## complex numbers
# http://xahlee.info/python/complex_numbers.html
print('')
cc = complex(3, 4)
print(cc)
cc2 = 3 + 4j
print(cc2)
print(cc == cc2)
print(cc.real)
print(cc.imag)

print(complex(2, 3) + complex(4, 5))
print(complex(1, 0) * complex(0, 1))
print(complex(3, 4) * 2)
print(complex(3, 4) + 1)

## length of a complex number; that is, sqrt[i ^ 2 + j ^ 2]
print(abs(complex(3, 4)))
