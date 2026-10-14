# Решение
x = 343**5 + 343**4 + 49**6 - 7**13 - 21

k = 7
res = []
s= ''
while x > 0:
    s = str(x % k) + s
    x //= k

print(s)




answer = 4

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1407, answer, 'a87ff679a2f3e71d9181a67b7542122c'))