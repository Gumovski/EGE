# Решение
I1 = 2*56000*15 * (27*60 + 27) / 8 / 1024
I2 = 367217732*332 / 1024 / 8
I = (I2 - I1) / 28
print(I1)
print(I2)
print(I)



answer = 519450

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(7, 74, answer, 'a546436d8834bbe5a21e510e6665a448'))