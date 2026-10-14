n = 5
odd = 0

for r in range(n):
    spisok = []
    p = 1
    for k in range(r+1):
        spisok.append(p)
        if p % 2 == 1:
            odd += 1
        if 0 <= k < r:
            p = p*(r-k)//(k+1)
    print(*spisok, sep=" ")

print("Нечетных элементов:", odd)
