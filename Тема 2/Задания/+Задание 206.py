# Решение
from itertools import product, permutations

def f1(x,y,z,w):
    return 1 if ((not x)  and z and (not y) and (not w)) or ((not x) and z and y and (not w)) or ((not x) and z and y and w) else 0

for a0,a1,a2,a3,a4,a5,a6 in product((0,1),repeat = 7):
    s = [(a0,1,0,a1,1),
         (0,0,a2,a3,1),
         (a4,a5,1,a6,1)]

    if len(set(s)) == len(s):
        for x,y,z,w in permutations((0,1,2,3)):
            if all([f1(i[x],i[y],i[z],i[w]) == i[-1] for i in s]):
                print(f' x = {x + 1},y = {y + 1},z = {z + 1},w = {w + 1}')






answer = 'xywz'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 206, answer, '00e936354216c4a6823136059258f377'))