#year = int(input())
year = 2100

if not(1 <= year <= 9999):
    print("Ошибка")
elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Високосный")
else:
    print("Невисокосный")
