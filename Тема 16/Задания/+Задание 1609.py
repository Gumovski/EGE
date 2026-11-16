# Решение
f = {}

for n in range(1,1000000):
    f[0] = 0
    if n % 2 != 0:
        f[n] = f[n-1] +2*n-1
    elif n % 2 == 0:
        f[n] = 4 * f[n//2]
s = []
for i in range(10000):
    print(i,f[i])
    s.append(f[i])
for i in range(10000):
    for j in range(10000):
        if s[i] - s[j] == 1001:
            print(f'Ответы {abs(i - j)}')

answer = 13

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1609, answer, 'c51ce410c124a10e0db5e4b97fc2af39'))