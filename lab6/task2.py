x = 49
d = 0
for i in range(2, x):
    if x % i == 0:
        d += 1
if d == 0:
    print("Простое")
else:
    print("Не простое")
