# Решение
f = {}
for n in range(1,1000000):
    if n < 4000:
        f[n] = n
    elif n >= 4000 and n % 7 == 0:
        f[n] = n + f[n//7]
    elif n >= 4000 and n % 7 != 0:
        f[n] = 567 + f[n-3]

for i in range(1,1000000):
    if f[i] > 80000:
        print(i)
        break





answer = 62962

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1606, answer, 'c664ec48cfb940b2ce2386c8fb7f9be8'))