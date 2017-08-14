import random

n = random.randint(1, 30)

while True:
    x = input("Guess from 1 to 30: ")
    g = int(x)

    if g == n:
        print("Correct!")
        break
    if g < n:
        print("Try bigger.")
    if g > n:
        print("Try smaller.")
