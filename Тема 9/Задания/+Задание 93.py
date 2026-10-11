# Решение
ans = 1
res = []
with open('Задание93.txt') as file:
    for line in file:
        s = list(map(int,line.split('\t')))
        m = 0
        for i in range(7):
            if s.count(s[i]) == 3:
                m = s[i]

        s1 = s[:]
        while m in s1:
            s1.remove(m)

        if len(set(s)) == 5 and sum(s1) // 4 <= m and max(s) % min(s) != 0:
            res.append([ans,sum(s)])
        ans += 1
print(res)

#3203


answer = 3203

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(9, 93, answer, '799de6d3dae4c924142cf245a1d7f703'))