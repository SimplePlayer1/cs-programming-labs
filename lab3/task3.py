#vvod = input()
vvod = "+7 (924) 123-45-67"

vvod = vvod.replace(" ", "").replace("-", "").replace("+", "").replace("(", "").replace(")", "")
print(vvod)
