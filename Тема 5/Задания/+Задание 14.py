# Решение
def f(n,k):
    s = ''
    while n > 0:
        s = str(n%k) + s
        n //= k
    return s

s = set()

for n in range(1,1000):
    t = f(n,2)
    g = f(n%4,2)
    if n % 4 == 0:
        g = '0'
    t = t + g
    s.add(int(t,2))

res = 0
for a in range(1,2000):
    c = 0
    for x in range(a,a + 49):
        if x in s:
            c += 1
    res = max(res,c)
print(res)
#19

answer = 19

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 14, answer, '1f0e3dad99908345f7439f8ffabdffc4'))