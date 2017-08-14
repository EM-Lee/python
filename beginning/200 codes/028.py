strdata = "Time is money!!"
print("Length of the string: ", len(strdata))
print(strdata[1:5])
print(strdata[:7])
print(strdata[9:])
print(strdata[:-3])
print(strdata[-3:])
print(strdata[:])
print(strdata[::2])
print("-----")
for s in range(0, len(strdata)):
    print(s)
    print(strdata[s])
