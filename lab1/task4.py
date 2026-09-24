vremya = int(input())
h = vremya // 3600
vremya = vremya - 3600*h
m = vremya // 60
vremya = vremya - 60*m
s = vremya

print("0"+str(h)+":"+"0"+str(m)+":"+"0"+str(s))
