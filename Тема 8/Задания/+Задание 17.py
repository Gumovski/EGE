# Решение
from itertools import*
count = 0
for item in product('1357','2468','1357','2468','1357','2468','1357','2468','1357','2468','1357'):
    line = ''.join(item)
    if line.count('1') <= 4 and line.count('2') <= 4  and line.count('3') <= 4 and line.count('4') <= 4 and line.count('5') <= 4 and line.count('6') <= 4 and line.count('7') <= 4 and line.count('8') <= 4:
        count += 1
print(count*2)






answer = 8200800

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 17, answer, 'd67d496249f30f93dd6a7a6d84701d60'))