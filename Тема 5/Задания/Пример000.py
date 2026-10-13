def to_base(n, k):
    s = ''
    while n > 0:
        s = str(n % k) + s
        n //= k
    return s

best = 10**9
for n in range(1, 1000):
    t = to_base(n, 3)
    if n % 2 == 0:
        t = '11' + t + '11'
    else:
        t = '1' + t + '00'
    r = int(t, 3)
    if r > 95:
        best = min(best, r)
print(best)