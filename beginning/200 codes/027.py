strdata = "Time is money!!"
listdata = [1, 2, [1, 2, 3]]
print(strdata[5])
print(strdata[-2])
print("-----")
no = 0
for i in strdata:
    print(i)
    print(no)
    no += 1
    
print("-----")
print("-----")

print(listdata[0])
print(listdata[-1])
print(listdata[2][-1])
print("-----")
no = 0
for i in listdata:
    print(i)
    print(no)
    no += 1

