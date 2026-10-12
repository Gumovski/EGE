# Решение
N = 800
j = 10
#bits = j * l

I1 = 2 * 1024
n = I1/(11 + 1)
f = I1 - (170 * 12)
f -=1
bats = 170 * 11 + f
bits = bats * 8
l = bits / j
print(l)
#1501




answer = 1501

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(11, 117, answer, '5cbdfd0dfa22a3fca7266376887f549b'))