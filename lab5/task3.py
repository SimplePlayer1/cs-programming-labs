x = 5
s0 = 0
s1 = 0
s2 = 0

for i in range(x):
    y = float(input())
    if y < 0:
        s0 += 1
    elif y == 0:
        s1 += 1
    else:
        s2 += 1
print("Ниже нуля", s0)
print("Равны нулю", s1)
print("Выше нуля", s2)
