s = 0
k = 0
while True:
    x = input()
    if x == "stop":
        break
    else:
        x = int(x)
    s += x
    k += 1
print("Покупок:", k)
print("Общая стоимость:", s, "руб")
print("Средняя стоимость:", f"{(s/k):.2f}", "руб")
