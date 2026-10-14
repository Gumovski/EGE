# Решение
res = []
s = []
for x in '0123456789ABC':
    for y in '0123456789ABC':
        f1 = f'8{x}78{y}'
        f2 = f'79{x}{y}7'

        r = int(f1,13) + int(f2,18)
        if r % 9 == 0:
            res.append([x,y,r//9])
            s.append(r//9)
            break
s.sort()
print(res)
print(s)
#x = 0, y = 6
#113024

answer = 113024

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1401, answer, '436fc6a87245490c1c09148823eec9ff'))