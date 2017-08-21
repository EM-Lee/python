# why bitwise operation?
# https://m.blog.naver.com/PostView.nhn?blogId=clowstar&logNo=110096631099&proxyReferer=https%3A%2F%2Fwww.google.com%2F
# https://code.tutsplus.com/articles/understanding-bitwise-operators--active-11301

### bitwise example: speed matters
# import time

## x를 1024번 더해주다
# x = 4938
# t0 = time.time() #time.clock() for process time
# x = x * 1024
# t1 = time.time() - t0
# print(x)
# print(t1)

## x 곱하기 2를 10회 반복, 즉 비트상에서 왼쪽으로 10번 옮기다
# y = 4938
# t0 = time.time()
# y = y << 10
# t1 = time.time() - t0
# print(y)
# print(t1)

a = 107
print(hex(a))
b = a & 0x0f
print(b)
