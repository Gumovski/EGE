# Решение
for a in range(1000,0,-1):
    if all(((y > a) or (152 != 2*y + 3*x) or (a < x)) for x in range(1,100) for y in range(1,100)):
        print(a)
        break






answer = 30

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(15, 1504, answer, '34173cb38f07f89ddbebc2ac9128303f'))