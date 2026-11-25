m = 0
ans = 0
for x in range(2031,1,-1):
    s = 0
    r = 5**150 + 5**100 - x
    while r > 0:
        if r % 5 == 0:
            s += 1
        r = r // 5
    if s > m:
        m = s
        ans = x

print(ans)