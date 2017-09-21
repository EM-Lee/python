def sum_sq(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i * i
    return s

print(sum_sq(10))   # 1부터 10까지 제곱의 합(입력:10, 출력:385)
print(sum_sq(100))  # 1부터 100까지 제곱의 합(입력:100, 출력:338350)
