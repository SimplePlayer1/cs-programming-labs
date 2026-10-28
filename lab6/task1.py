a = 84
b = 30
res = 0

if a < 0 or b < 0 or (a == 0 and b == 0):
    print("Ошибка")
else:
    for i in range(1, max(a, b)+1):
        if a % i == 0 and b % i == 0:
            res = i
print(res)
