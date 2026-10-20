# Решение
def f(x,y,a):
    if x == y:
        return 1
    if x > y + 1:
        return 0

    s = f(x + 3,y,0) + f(x * 2,y,0)
    if a == 0:
        s += f(x-1,y,1)
    return s

print(f(3,12,0))

#53





answer = 53

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1304, answer, 'd82c8d1619ad8176d665453cfb2e55f0'))