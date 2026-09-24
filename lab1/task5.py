distance = int(input())
consumption = float(input())
cost = int(input())

print("Топливо:", (consumption/100)*distance, "л")
print("Стоимость:", cost*((consumption/100)*distance), "руб")
