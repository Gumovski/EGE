# Решение
ans = 0
d = [{} for j in range(6)]
with open('Задание 18.txt') as file:
    for line in file:
        s = list(map(int,line.split('\t')))
        for i in range(6):
            if s[i] not in d[i]:
                d[i][s[i]] = 1
            else:
                d[i][s[i]] += 1

with open('Задание 18.txt') as file:
    for line in file:
        s = list(map(int,line.split('\t')))
        x = 0
        for i in range(6):
            if s.count(s[i]) == 1 and d[i][s[i]] > 150:
                x += 1

        if x >= 5:
            ans += 1

print(ans)




answer = 9527

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(9, 18, answer, '67388f1834f7d6243b753ec33584a8df'))