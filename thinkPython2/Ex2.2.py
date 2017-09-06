### old Q&A
### https://en.wikibooks.org/wiki/Think_Python/Answers
### https://github.com/epequeno/ThinkPy-Solutions


#01 The volume of a sphere with radius r is (4/3)πr^3.
### What is the volume of a sphere with radius 5?
print('Q1 -----')
import math

pi = math.pi
r = 5
v = (4/3) * pi * math.pow(r, 3)
print(v)

#02 Suppose the cover price of a book is $24.95,
### but bookstores get a 40% discount.
### Shipping costs $3 for the first copy and
### 75 cents for each additional copy.
### What is the total wholesale cost for 60 copies?
print('')
print('Q2 -----')
cvrPrice = 24.95 #price before discount
dscntRate = 0.4 #discount rate
firstShpPrice = 3 #shipping cost for the first copy
exShpPrice = 0.75 #shipping cost for the next
nCopy = 60 #number of copies to order

priceCopies = cvrPrice * nCopy * (1 - dscntRate)
print("Price excluding delivery: ", priceCopies)
priceDlvr = firstShpPrice + (nCopy - 1) * exShpPrice
print("Price for delivery: ", priceDlvr)

totalPrice = priceCopies + priceDlvr
print("Total Price: ", totalPrice)


#03 If I leave my house at 6:52 am and
### run 1 mile at an easy pace (8:15 per mile),
### then 3 miles at tempo (7:12 per mile) and
### 1 mile at easy pace again, what time do I get home for breakfast?
print('')
print('Q3 -----')
easyP = 8 * 60 + 15 #seconds
regP = 7 * 60 + 12 #seconds

tWalked = (easyP + regP * 3 + easyP)
hhmm = divmod(tWalked, 60)
print(hhmm[0], hhmm[1])
if hhmm[0] < 8:
    print(6, ":", 52 + hhmm[0], ":", hhmm[1], " arrived.")
else:
    print(7, ":", 52 + hhmm[0] - 60, ":", hhmm[1], " arrived.")

### another way from
### https://en.wikibooks.org/wiki/Think_Python/Answers#Exercise_2.2
print('')
print('Q3 ----- another way')

start_time_hr = 6 + 52 / 60.0
easy_pace_hr = (8 + 15 / 60.0 ) / 60.0
tempo_pace_hr = (7 + 12 / 60.0) / 60.0
running_time_hr = 2 * easy_pace_hr + 3 * tempo_pace_hr
breakfast_hr = start_time_hr + running_time_hr
breakfast_min = (breakfast_hr-int(breakfast_hr))*60
breakfast_sec= (breakfast_min-int(breakfast_min))*60

print ('breakfast_hr', int(breakfast_hr) )
print ('breakfast_min', int (breakfast_min) )
print ('breakfast_sec', int (breakfast_sec) )
