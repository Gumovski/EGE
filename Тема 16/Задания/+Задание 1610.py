# Решение
f = {}
for n in range(1,2025):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = n * f[n-1]


print((f[2024] - f[2023]) // f[2022])






answer = 4092529

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1610, answer, 'e8b6b9482031792df830fa44bfbeda43'))