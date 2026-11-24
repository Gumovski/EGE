# Решение
m = 10**50
for x in range(22):
    r1 = f'7418{x}{x}461'
    r2 = f'719625{x}4'
    r3 = f'396{x}99'

    r = int(r1,22) +  int(r2,22) +  int(r3,22)

    if r % 21 == 0:
        m = min(m,r)

print(m//21)




answer = 19614415862

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(14, 1405, answer, '04ffec330b9d276c1c81c59c1d1a4376'))