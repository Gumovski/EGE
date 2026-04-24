s = [0] * 10000
c = 0
for n in range(2,500):
    t = bin(n)[2:]
    y = n % 4
    y2 = bin(y)[2:]
    t += y2
    r = int(t,2)
    s[r] = 1
res = []
for i in range(len(s) - 65):
    w = s[i:i + 65].count(1)
    res.append(w)

print(max(res))
