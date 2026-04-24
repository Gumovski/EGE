for n in range(22,100000):
    s = bin(n)[2:]
    sl = list(s)
    for i in range(len(sl)):
        if sl[i] == '0':
            sl[i] = '1'
        else:
            sl[i] = '0'
    c = 0
    for i in range(len(sl)):
        if sl[i] == '0':
            c += 1
        else:
            break
    sl = sl[c:]
    if sl == '0':
        sl = '1'

    s = ''.join(sl)
    if s == '':
        s = '1'
    r = int(s,2)
    R = n - r

    if R == 999:
        print(n,R)


    







answer = 1011

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 5, answer, '7f975a56c761db6506eca0b37ce6ec87'))