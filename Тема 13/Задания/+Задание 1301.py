# Решение
def f(x,y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x + 1,y) + f(x * 2, y) + f(x * 3, y)

I24 = f(9, 24) * f(24, 81)
I27 = f(9, 27) * f(27, 81)
I2427 = f(9, 24) * f(24, 27) * f(27, 81)

res = (I24 + I27) - I2427
print(res)
#142

answer = 142

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1301, answer, 'a8baa56554f96369ab93e4f3bb068c22'))