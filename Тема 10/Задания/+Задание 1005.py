# Решение
from ipaddress import ip_network

net = ip_network('191.128.66.83/255.192.0.0',False)
largest = list(net.hosts())[-1]
print(largest)
#191.191.255.254
#191191255254

answer = 191191255254

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(10, 1005, answer, 'e02030d89e606e5f68c55c7aed0a8e23'))