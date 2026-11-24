# Решение
r = 4 * 625**9 - 25**15 + 2 * 5**11 - 7
s = 0
while r > 0:
    if r % 5 == 4:
        s += 1
    r = r // 5
print(s)







answer = 15

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1408, answer, '9bf31c7ff062936a96d3c8bd1f8f2ff3'))