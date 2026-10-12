# Решение
from itertools import combinations
count = 0

for l in range(2,13):
    for s in combinations(('0123456789AB'),l):
        line = ''.join(s)
        if line[0] != '0':
            count += 1

print(count)
#2036


answer = 2036

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 86, answer, 'f48c04ffab49ff0e5d1176244fdfb65c'))