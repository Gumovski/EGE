for n in range(12,1000):
    t = bin(n)[2:]
    f = t.count('1')
    t += str(f % 2)
    f = t.count('1')
    t += str(f % 2)
    r = t
    r = int(r,2)
    if r > 97:
        print(r)
