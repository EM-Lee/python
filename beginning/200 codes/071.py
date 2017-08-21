def getPrime(x):
    for i in range(2, x - 1):
        if x % i == 0:
            #print(i)
            break
    else:
            return x
# http://python-notes.curiousefficiency.org/en/latest/python_concepts/break_else.html

listdata = [117, 119, 1113, 11113, 11119]
ret = filter(getPrime, listdata)
print(list(ret))
