# Решение

from itertools import product

count = 0
for s in product('0123456789ABCDEF', repeat=6):
    line = ''.join(s)
    t = line.replace('D', 'x').replace('E', 'x').replace('F', 'x')
    if line[0] != '0' and '5' in line and t.count('x') == 2 and 'xx' in t:
        count += 1
print(count)





answer = 335241

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 84, answer, '85705f54f8b912d25a2eac2583e7093d'))