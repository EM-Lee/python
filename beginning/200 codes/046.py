from time import sleep
from mypackage import mylib
from mypackage.mylib import reverse

sleep(1)
print(mylib.add_txt('나는', '파이썬이다'))
print(reverse(1, 2, 3))
