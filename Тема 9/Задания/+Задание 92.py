# Решение
ans = 1
res = []
with open('Задание92.txt') as file:
    for line in file:
        s = list(map(int,line.split('\t')))
        m = 0
        for i in range(6):
            if s.count(s[i]) == 3:
                m = s[i]
        s1 = s[:]
        while m in s1:
            s1.remove(m)
        if len(set(s)) == 4 and m > sum(s1) // 3:
            res.append(ans)

        ans+=1
print(max(res))




answer = 24959

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(9, 92, answer, '18b8ea83d814103c4a8f379165ce9a62'))