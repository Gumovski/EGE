# Решение
from itertools import product
count = 1
res = []
for s in product(('АГМНСТУ'),repeat = 6):
    line = ''.join(s)
    if line[0] != 'У' and line.count('М') == 2 and line.count('Г') <= 1:
        res.append(count)

    count+=1

print(res[-1])
#100810



answer = 100810

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 85, answer, '4f41663a6f277ab55c6b626aff28784a'))