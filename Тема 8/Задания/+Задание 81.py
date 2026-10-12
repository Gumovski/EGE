# Решение
from itertools import product
count = 0
g = 'ОА'
c = 'РСМХ'
for s in product(('РОСМАХ'),repeat = 8):
    line = ''.join(s)
    if line.count('Р') == 1 and line.count('О') == 2 and line.count('А') == 2 and line.count('С') == 1 and line.count('М') == 1 and line.count('Х') == 1:
        f = 0
        for i in range(7):
            if (line[i] in g) == (line[i + 1] in g):
                f = 1

        if f == 0:
            count += 1

print(count)





answer = 288

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 81, answer, '48aedb8880cab8c45637abc7493ecddd'))