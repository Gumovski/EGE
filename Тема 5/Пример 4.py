def t(n):
    s = ''
    while n != 0:
        s += str(n % 3)
        n //= 3
    return s


y = []
for n in range(12, 100000):
    s = t(n)
    if n % 3 == 0:
        s += s[-2:]
    else:
        s_l = s.count('1') + s.count('2') * 2
        s += t(s_l * 2)
    r = int(s, 3)
    if r % 2 != 0 and r > 520:
        y.append(r)
print(min(y))
