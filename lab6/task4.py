n = 4050
if n < 0:
    print("Ошибка")
else:
    s = 0
    k = 0
    while n != 0:
        s += n%10
        k += 1
        n //= 10
    print("Цифр:", k)
    print("Сумма цифр:", s)
