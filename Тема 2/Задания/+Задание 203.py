# Решение
print('x y w z u')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                for u in range(2):
                    F = ((x <= y) and (z == (not w))) <= (u == (x or z))
                    if F == 0:
                        print(x,y,w,z,u)

answer = 'wzyxu'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 203, answer, 'b83215ff76ddd410e32571919b78d0eb'))