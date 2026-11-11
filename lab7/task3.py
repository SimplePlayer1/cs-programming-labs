a = [4, 7, 4, 4, 9]
b = 4
c = []

for i in range(len(a)):
    if a[i] == b:
        c.append(i)
print(c)
