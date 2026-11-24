# Решение
s = list(map(int,open('Задание 1703.txt').readlines()))
m = 10 ** 4
c = 0
res = []
for i in range(len(s)):
    t1 = str(s[i])
    if t1[-1] == t1[-2] and m > s[i]:
        m = s[i]

for i in range(len(s)-1):
    s1 = str(s[i])
    s2 = str(s[i+1])
    k = 0
    if s[i] % 13 == 0:
        k += 1
    if s[i+1] % 13 == 0:
        k += 1
    if (s1[-1] == s2[-2] or s1[-2] == s2[-1])  and k == 1 and (s[i]**2 + s[i+1]**2) <= (m**2):
        c += 1
        res.append(s[i]**2 + s[i+1]**2)
print(c)
print(max(res))


answer1 = 115
answer2 = 96944186

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1703, f'{answer1} {answer2}', '1b1a3f384b8b6bddea7c6e63fad46024'))