# Решение
ans = 0
with open('Задание91.txt') as file:
    for line in file:
        s = list(map(int,line.split('\t')))
        s1 = s[:4]
        s2 = s[4:]
        m = max(s)
        if (s.count(m) == 1) and (m in s1) and sum(s1) / 4 < sum(s2) / 4:
            ans += 1

print(ans)

answer = 1246

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(9, 91, answer, '905056c1ac1dad141560467e0a99e1cf'))