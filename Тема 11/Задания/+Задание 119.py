# Решение
#Объект = код + тип
l = 15
N = 36
j = 6
#Тип блока от 1 до 2000
n = 40
#I = ?
c = 32768
tip = 10
bits = l * j
blok = (bits + tip) / 8
blok = 13
I1 = blok * 40
I = I1 * 32768 / 1024
print(I)
answer = 16640

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(11, 119, answer, 'd1aae872c07c10af8bc9918fdb28c28c'))