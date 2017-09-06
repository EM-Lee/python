### https://github.com/epequeno/ThinkPy-Solutions/blob/master/ch01/1.04.py
"""
distKm = 10.0
distMi = (distKm * (1.0 / 1.61))
seconds = ((43.0 * 60.0) + 30.0)
hours = (43.5 / 60.0)

def timePerMile(distMi, seconds):
   print(seconds / distMi, 'seconds per mile')

def avgSpeed(distMi, hours):
   print(distMi / hours, 'miles per hour')

timePerMile(distMi, seconds)
avgSpeed(distMi, hours)
"""

# If you run a 10 kilometer race in 43 minutes 30 seconds,
# what is your average time per mile?
# What is your average speed in miles per hour?
# (Hint: there are 1.61 kilometers in a mile).


dKm = 10
dMi = dKm / 1.61
sec = (43 * 60) + 30
hr = sec / 3600

avgT = sec / dMi
avgV = dMi / hr

print("My average time per mile is %.2f seconds." %(avgT))
print("My average speed in miles per hour is %.2f." %(avgV))
