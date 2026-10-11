# Решение
ans = 0
d = [{} for j in range(6)]
with open('Задание94.txt') as file:
    for line in file:
        s = list(map(int,line.split('\t')))

        for i in range(6):
            if s[i] not in d[i]:
                d[i][s[i]] = 1
            else:
                d[i][s[i]] += 1

with open('Задание94.txt') as file:
    for line in file:
        s = list(map(int,line.split('\t')))
        x = 0
        for i in range(6):
            if s.count(s[i]) == 1 and d[i][s[i]] - 1 >= 330 and s[i] > sum(s) / 6:
                x += 1

        if x == 1:
            ans += 1

print(ans)
#4175




answer = 4175

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(9, 94, answer, '97008ea27052082be055447be9e85612'))