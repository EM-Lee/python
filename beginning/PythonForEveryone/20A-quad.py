import math
import sys

print("ax^2 + bx + c = 0")

a = float(input("a?"))
b = float(input("b?"))
c = float(input("c?"))

if a == 0:
    print("a = 0: not a quadratic equation")
    sys.exit()

D = (b * b) - (4 * a * c)
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("two values: ", x1, x2)
if D == 0:
    x = -b / (2 * a)
    print("one value: ", x)
if D < 0:
    print("no value")
