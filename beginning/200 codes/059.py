import time
count = 1
try:
    while True:
        print(count)
        count += 1
        time.sleep(.5)
except KeyboardInterrupt:
    print('program stopped by a user')
