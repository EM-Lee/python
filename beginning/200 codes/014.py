x = 0
while x <= 10:
    x = x + 1
    if x < 3:
        continue
    print(x)
    if x > 7:
        break
print("-----")

x = 1
total = 0
while 1:
    total = total + x
    if total > 100000:
        print(x)
        print(total)
        break
    x = x + 1
print("-----")

s = 0
for i in range(448):
    s = s + i
print(s)
