# Решение
B =  11 * 12 / (2 * 44000 * 16 / 8 / 1024 / 1024)
A = (2 * 66000 * 32 /8 / 1024/ 1024 * B) / 2



print(B)
print(A)



answer = 198

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(7, 75, answer, '0e65972dce68dad4d52d063967f0a705'))