#vvod = input()
vvod = "AB-204"

print("Длина:", len(vvod))

if vvod.isalpha():
    print("Только буквы: True")
else:
    print("Только буквы: False")

if vvod.isdigit():
    print("Только цифры: True")
else:
    print("Только цифры: False")

if vvod.isalnum():
    print("Буквенно-цифровая: True")
else:
    print("Буквенно-цифровая: False")

if vvod.count("-") >= 1:
    print("Содержит дефис: True")
else:
    print("Содержит дефис: False")
print()
