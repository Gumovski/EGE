# Решение
f = {}
g = {}
for n in range(-100,423000):
    if n <= 9:
        g[n] = 3 * n
    elif n > 9:
        g[n] = g[n-4] +2

for n in range(1,423000):
    f[n] = g[n - 1] + g[n - 3]

print(f[42999])

answer = 43032

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1608, answer, '0a44140fcbbf55d76a1dc8953ebecd1b'))