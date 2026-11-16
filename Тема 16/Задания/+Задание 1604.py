# Решение
f = {}
for n in range(1,29):
    if n < 3:
        f[n] = 1
    elif n > 2 and n % 2 != 0:
        f[n] = f[n-1] + 3 * f[n-2]
    elif n > 2 and n % 2 == 0:
        f[n] = sum(f[i] for i in range(1,n))

print(f[28])






answer = 814893696

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1604, answer, 'e31a2673da538481c8408e028f67a70a'))