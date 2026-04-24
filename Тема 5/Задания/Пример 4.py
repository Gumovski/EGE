def t(n):
    s = ''
    while n != 0:
        s += str(n % 3)
        n = n // 3
    s = s[::-1]
    return s

y = []
for n in range(12,100000):
    s = t(n)
    if n % 3 == 0:
        s += s[-2:]
    else:
        s_l = list(s)
        for i in range(len(s_l)):
            s_l[i] = int(s_l[i])
        summ = sum(s_l)
        summ = summ*2
        e = t(summ)
        s += e

    r = int(s,3)

    if r % 2 != 0 and r > 520:
        y.append(r)
print(min(y))


