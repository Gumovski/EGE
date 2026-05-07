# Решение
c = 0
for n in range(13,100000):
    s = bin(n)[2:]
    n1 = n % 3
    n2 = bin(n1)[2:]
    s +=  '0' + n2
    t = int(s,2)
    t1 = t % 5
    t2 = bin(t1)[2:]
    s += '0' + t2

    r = int(s,2)
    f = int(s)
    if f > 1111111110  and f < 1444444416:
        c += 1
print(c)







answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 51, answer, '389499b02f30212486e408cd73a5bc50'))