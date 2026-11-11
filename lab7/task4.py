w, h = 2, 3
a = [3,-1,4]
b = [0,5,2]
s = []

s.append(a)
s.append(b)
str = []
sto = []

for i in range(w):
    str.append(sum(s[i]))
    
for j in range(h):
    summ = a[j]+b[j]
    sto.append(summ)
    
print(str)
print(sto)
