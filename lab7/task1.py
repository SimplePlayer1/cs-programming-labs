a = [12, -3, 0, 7, -1]
b = a
print("Исходные остатки:", a)
for i in range(len(b)):
    if b[i] < 0:
        b[i] = 0
print("Исправленные остатки:", b)
