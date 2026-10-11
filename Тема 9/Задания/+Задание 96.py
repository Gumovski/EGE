# Решение
ans = 1
res = []
with open('Задание96.txt') as file:
    for line in file:
        s = list(map(int,line.split('\t')))

        s1 = s[:]
        s1.sort()
        s1.reverse()
        y = 0
        m = sum(s1[1:6]) / 5
        for i in range(7):
            if s1[i] == s[i]:
                y += 1
        if len(set(s)) == 7 and y == 7 and (s1[0] + s1[-1]) / 2 > m:
            ans += 1

print(res)



answer = 652

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(9, 96, answer, '30ef30b64204a3088a26bc2e6ecf7602'))