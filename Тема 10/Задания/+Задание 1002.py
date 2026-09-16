# Решение
from ipaddress import ip_network
net = ip_network(f'122.159.136.144/255.255.255.248',False)
c = 0
for ip in net:
    if f'{ip:b}'.count('1') % 4 != 0:
        c += 1
print(c)


answer = 5

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(10, 1002, answer, 'e4da3b7fbbce2345d7772b0674a318d5'))