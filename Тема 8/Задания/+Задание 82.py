# Решение
from itertools import product

count = 1
res = []
for s in product(('АКОРСТ'),repeat = 5):
    line = ''.join(s)
    if (count) % 2  == 0 and line[0] not in 'АСТ' and line.count('О') == 2:
        res.append(count)
    count+=1
print(res)


answer = 5058

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 82, answer, '7ffb4e0ece07869880d51662a2234143'))