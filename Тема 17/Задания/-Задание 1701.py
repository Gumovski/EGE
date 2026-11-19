# Решение

s = list(map(int,open('Задание 1701.txt').readlines()))
c = 0
res = []
m = -10000
for i in range(len(s)):
    if -999 > s[i] > -10000  and s[i] % 9 == 0 and s[i] > m:
        m = s[i]
for i in range(len(s) - 1):
    flag = 0
    if ((s[i] < 0 and s[i+1] >= 0) or (s[i] > 0 and s[i+1] <= 0)) and s[i] + s[i+1] > m:
        c += 1
        res.append(s[i] ** 2 + 2 *s[i]*s[i+1] + s[i+1]**2)
res.sort()
print(c,res[0])


answer1 = 2628
answer2 = 81

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1701, f'{answer1} {answer2}', 'b73de31c02e01cfc4508d15f2cf61e69'))