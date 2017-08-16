import time
import mylib
import mypackage.mylib

time.sleep(1)
print(mylib.add_txt('나는', '파이썬이다'))
print(mypackage.mylib.reverse(1, 2, 3))
