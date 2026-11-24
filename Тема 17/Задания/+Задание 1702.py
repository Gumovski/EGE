# Решение
s = list(map(int,open('-Задание 1702.txt').readlines()))
c = 0
res = []
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if abs(s[i] - s[j]) % 60 == 0 and (s[i] % 15 == 0 or s[j] % 15 == 0):
            c += 1
            res.append(abs(s[i]-s[j]))

print(c,max(res))






answer1 = 63517
answer2 = 9960

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1702, f'{answer1} {answer2}', '1f1b321d4ee0f8a0a2de5ccf29035748'))