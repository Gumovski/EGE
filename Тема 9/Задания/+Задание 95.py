# Решение
ans = 1
res = []
with open('Задание95.txt') as file:
    for line in file:
        s = list(map(int,line.split('\t')))

        s1 = s[:]
        s1.sort()
        x = 0
        y = 0
        for i in range(6):
            if s[i] % 2 == 0:
                x += 1
        for i  in range(6):
            if s[i] == s1[i]:
                y += 1
        if x == 3 and y == 6 and len(set(s)) == 6:
            res.append([ans,sum(s)])
        ans += 1
print(res)

#1509


answer = 1509

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(9, 95, answer, '1cd3882394520876dc88d1472aa2a93f'))