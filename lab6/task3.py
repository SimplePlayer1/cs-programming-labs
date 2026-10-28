def prost(n):
    d = 2
    while d*d <= n:
        if n % d == 0:
            return 0
        d += 1
    return 1

n = 60
s = []
if n < 0:
    print("Ошибка")
else:
    for i in range(2, n):
        if prost(i) == 1:
            s.append(i)

s2 = []
while n != 1:
    for i in s:
        if n % i == 0:
            n = n / i
            s2.append(i)
s2.sort()
print(*s2, sep=" ")
