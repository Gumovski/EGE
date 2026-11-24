# Решение
m = 10**8
for x in '0123456':
    for y in '0123456':
        r1 = f'{y}{x}320'
        r2 = f'1{x}3{y}3'

        r = int(r1,7) + int(r2,9)

        if r % 181 == 0:
            m = min(m,r)

print(m//181)





answer = 148

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1402, answer, '47d1e990583c9c67424d369f3414728e'))