a = 2
b = 4
ret1 = a + b
ret2 = a - b
ret3 = a * b
ret4 = a / b
ret5 = a ** b
ret6 = a + a * b / a
ret7 = (a + b) * (a - b)
ret8 = a * b ** a

#string = "ret"
#varList = [string + str(i) for i in range(1, 9)]
varList = [ret1, ret2, ret3, ret4, ret5, ret6, ret7, ret8]
for i in varList:
    print(i)
