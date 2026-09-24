from ipaddress import ip_network

for mask in range(32,-1,-1):
    net = ip_network(f'121.96.174.205/{mask}',False)
    c = 0
    for ip in net:
        if f'{ip:b}'.count('1') == 12:
            c += 1

    if c == 10:
        #print(net.network_address)
        print(mask)
        break

