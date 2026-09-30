def remove_space(vvod):
    vvod = vvod.split(" ")
    s = ""
    for i in range(len(vvod)):
        if len(vvod[i]) >= 1:
            s = s + vvod[i] + " "
    s = s.split(" ")
    s3 = s[0] + " "
    s2 = ""
    for i in range(1, len(s)):
        if len(s[i]) >= 1:
            s[i] = s[i][0:1] + ". "
            s2 = s2 + s[i]
    s4 = s3 + s2
    return s4.title()

#vvod = input()
vvod = "  иВАНОВ иВАН иВАНОВИЧ"
vvod = vvod.lower()
vvod = remove_space(vvod)
print(vvod)
