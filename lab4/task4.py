#a = int(input())
#b = int(input())
#c = int(input())
a = 5
b = 5
c = 8

x = a+b
y = a+c
z = b+c

if a <0 or b < 0 or c < 0 or x<=c or y<=b or z<=a:
    print("Треугольник не существует")
elif a == b == c:
    print("Равносторонний")
elif a == b or a == c or b == c:
    print("Равнобедренный")
else:
    print("Разносторонний")
