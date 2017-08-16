import time

print('will pause for 5 seconds')
time.sleep(5)
print('5 seconds have passed')


### using my module
import mylib

ret1 = mylib.add_txt('hi', 'there')
ret2 = mylib.reverse(1, 2, 3)
print(ret1)
print(ret2)
