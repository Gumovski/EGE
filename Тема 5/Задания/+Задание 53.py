# Решение
def f(v,k):
    s = ''
    while v > 0:
        s = str((v%k)) + s
        v//= k
    return s

res = []
for n in range(1,1000):
    t = f(n,3)
    j = (n % 3) * 4
    g = f(j,3)
    if n % 3 == 0:
        t = '1' + t + '02'
    if n % 3 != 0:
        t = t + g
    r = int(t,3)
    res.append([n,r])
print(res)


answer = 26

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 53, answer, '4e732ced3463d06de0ca9a15b6153677'))