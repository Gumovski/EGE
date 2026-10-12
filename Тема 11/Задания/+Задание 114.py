# Решение
l = 6
I = 480 * 1024 / 2048
j = 6
bats = 36
I = I / 40
I = I * 8
res = I-bats
print(2**res)

answer = 4096

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(11, 114, answer, 'f7efa4f864ae9b88d43527f4b14f750f'))