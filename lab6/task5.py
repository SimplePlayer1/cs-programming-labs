def res(s, n, x):
    d = n - 1
    for i in range(len(s)):
        if s[i] != 0:
            s[i] = n
    for y in range(x-1, -1, -1):
        s[y] = abs(s[y] - d)
        for z in range(x+1, len(s)):
            s[z] = abs(s[z] - d)
            d -= 1
    if set(s) != 2:
        return s
    return 0

n = 4
r = 1
s = [n] * n
result = []

if not(1 <= n <= 10):
    print("Ошибка")
else:
    for i in range(n):
        for j in range(len(s)):
            d = i
            s[d] = 0
            if i > 0:
                s[i-1] = n
        for x in range(len(s)):
            if s[x] == 0:
                s = res(s, n, x)
                
        result.append(s.copy())
        
result = result[1:len(result)-1]
first_str = [0] * n
for i in range(n):
    first_str[i] = i

last_str = first_str[::-1]
result.insert(0, first_str)
result.insert((n-1), last_str)
for n in result:
    print(*n, sep=" ")
