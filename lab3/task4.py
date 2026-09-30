#vvod = input()
vvod = "T-18;Владивосток;Хабаровск;08:45;1850.5"

vvod = vvod.split(";")
print("Поезд:", vvod[0])
print("Маршрут:", vvod[1] + "-" + vvod[2])
print("Отправление:", vvod[3])
print("Цена:", f"{float(vvod[4]):.2f}")
