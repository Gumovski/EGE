# Решение
from ipaddress import ip_network

a1 , a2 = '157.220.185.237', '157.220.184.230'

for prefix in range(32, 0, -1):
    net1 = ip_network(f'{a1}/{prefix}', False)
    net2 = ip_network(f'{a2}/{prefix}', False)
    if net1.network_address == net2.network_address:
        break

net = ip_network(f'{a1}/{prefix}', False)
print('Сеть:', net)

count = 0
for ip in net:
    if f'{ip:b}'.count('1') == 15:
        count += 1
print('Ответ:', count)


answer = 9

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(10, 1001, answer, '45c48cce2e2d7fbdea1afc51c7c6ad26'))