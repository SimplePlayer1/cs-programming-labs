#cost = float(input())
#age = int(input())
cost = 1800
age = 16

if cost > 0:
    if 0 <= age <= 120:
        if 0 <= age <= 5:
            print(cost*0)
        elif 6 <= age <= 17:
            print(cost*0.5)
        elif 18 <= age <= 59:
            print(cost)
        else:
            print(cost*0.7)
    else:
        print("Ошибка")
else:
    print("Ошибка")
