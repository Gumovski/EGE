# Решение
print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F1 = (x or (not y)) <= (w == z)
                F2 = (x or (not y)) == (w <= z)
                if F1 == 0:
                    print(x,y,w,z)






answer = '.w..'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 201, answer, '7379de4777f5748aa568b8d0bf8c3795'))