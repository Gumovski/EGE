# Решение
from ipaddress import ip_network, ip_address

host = ip_address('147.222.222.147')

for prefix in range(32,0,-1):
    net = ip_network(f'147.222.199.75/{prefix}',False)
    if host in net:
        break

print(prefix)
print(sum(1 for ip in net if f'{ip:b}'.count('1') == 14))




answer = 78

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(10, 1003, answer, '35f4a8d465e6e1edc05f3d8ab658c551'))