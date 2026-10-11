# Решение
from itertools import product, permutations

def f1(x,y,z,w):
    return 1 if (((x <= y) or (z <= w)) and ((z == y) <= (w == x))) else 0

for a0,a1,a2,a3 in product((0,1),repeat = 4):
    s = [(a0,1,0,a1,0),
         (0,1,0,1,0),
         (a2,1,0,a3,0)]
    if len(set(s)) == len(s):
        for x,y,z,w in permutations((0,1,2,3)):
            if all([f1(i[x],i[y],i[z],i[w]) == i[-1] for i in s]):
                print(f'x = {x + 1},y = {y + 1},z = {z + 1},w = {w + 1}')
                break

#yxwz



answer = 'yxwz'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 204, answer, '1ed5bb3720986c091b8dc2704366e53d'))