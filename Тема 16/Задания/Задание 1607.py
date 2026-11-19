# Решение
f = {}

for n in range(0,10000000):
    if n == 0:
        f[n] = 0
    elif n > 0 and n % 4 < 2:
        f[n] = f[n//4] + n%4
    elif n% 4 >= 2:
        f[n] = f[n//4] + n % 4 - 1

for i in range(0,10000000):
    if f[i] == 27 and f[i + 1] == 16:
        print(i)
        break







answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1607, answer, '2a0b3b7b30d11559c931dde71e179f16'))