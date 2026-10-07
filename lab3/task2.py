#vvod = input()
vvod = "  иВАНОВ иВАН иВАНОВИЧ"

vvod = vvod.strip().lower().title().split(" ")
vvod[1] = vvod[1][0] + "."
vvod[2] = vvod[2][0] + "."
vvod = " ".join(vvod)
print(vvod)
