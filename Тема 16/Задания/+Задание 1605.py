# Решение
f = {}

for n in range(-10,185735):
    if n <= 10:
        f[n] = n
    elif n > 10:
        f[n] = n-7 + f[n-21]

print((f[185734] - f[185650]) // f[40])






answer = 17274

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1605, answer, 'ff413935bfae4f0e2d8dce0e0dacfdcd'))