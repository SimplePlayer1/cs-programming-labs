r = 3
c = 4

row_start = 5
row_end = 1
column_start = 5
column_end = 0

a = [2, 5, 3, 5,
     5, 4, 5, 6,
     0, 2, 1, 3]
b = 5
s = []

for i in range(len(a)):
    if a[i] == b:
        s.append([i//c, (i%c)+1])

if len(s) > 0:
    for i in range(len(s)):
        print(*s[i], sep=" ")
else:
    print("Не найдено")
