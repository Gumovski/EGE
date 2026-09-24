from ipaddress import ip_network


for mask in range(32,-1,-1):
    net = ip_network(f'68.30.20.77/{mask}' ,False)
    count = 0
    if f'{net.network_address:b}'.count('1') == f'{net.netmask:b}'.count('0'):
        for ip in net:
            if f'{ip:b}'.count('1') == 10:
                count+= 1
        print(count)
