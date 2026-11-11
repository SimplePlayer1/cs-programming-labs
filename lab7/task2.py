a = [-3, 5, 0, 2, 1, 5]
b = []

for i in a:
    if ((i**2)**0.5)%1 == 0 and i > 0 and i % 2 == 1:
        b.append(i**2)
print(b)
