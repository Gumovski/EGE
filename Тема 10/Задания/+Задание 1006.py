# Решение
from ipaddress import ip_network
net = ip_network('205.182.128.0/255.255.192.0',False)

c = 0
for ip in net:
    packed = ip.packed
    byte3 = packed[2]
    b3 = f'{byte3:b}'
    if b3.count('1') == b3.count('0'):
        c += 1
print(c)



answer =5120

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(10, 1006, answer, '6aadca7bd86c4743e6724f9607256126'))