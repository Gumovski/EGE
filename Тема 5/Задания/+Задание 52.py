# Решение
res = []
for n in range(1,9999):
    t = bin(n)[2:]
    c1 = 0
    c0 = 0
    for i in range(len(t)):
        if t[i] == '1' and (i + 1) % 2 == 0:
            c1 += 1
        if t[i] == '0' and (i + 1) % 2 != 0:
            c0 += 1
    ma = max(c0,c1)
    mi = min(c0,c1)
    r= ma - mi
    res.append([n,r])

for part in res:
    if part[1] == 5:
        print(part)
        break
#1023



answer = 1023

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 52, answer, 'ce5140df15d046a66883807d18d0264b'))