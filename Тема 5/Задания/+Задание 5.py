for n in range(1, 100000):
    s = bin(n)[2:]
    sl = list(s)
    s = s.replace('0', '*').replace('1', '0').replace('*', '1')
    s = s.lstrip('0')
    if s != '':
        r = int(s, 2)
        R = n - r
        if R == 999:
            print(n, R)

answer = 1011

#

from tests.conftest import result_register

if answer is not Ellipsis:
    print(result_register(5, 5, answer, '7f975a56c761db6506eca0b37ce6ec87'))
