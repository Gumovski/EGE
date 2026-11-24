# Решение
s = list(map(int,open('Задание 1706.txt').readlines()))
count = 0
res = []
m = - 1000000
for j in range(len(s)):
    t = str(s[j])
    if t[-1] == '3' and t[-2] == '3' and s[j] > m:
        m = s[j]

for i in range(len(s)-2):
    a = s[i]
    b = s[i+1]
    c = s[i+2]
    s1 = str(abs(a))
    s2 = str(abs(b))
    s3 = str(abs(c))
    k = 0
    if len(s1) == 2:
        k += 1
    if len(s2) == 2:
        k += 1
    if len(s3) == 2:
        k += 1
        
    if k >= 2 and (a + b + c) ** 2 <= m:
        count  += 1
        res.append(a + b + c)

print(count)
print(max(res))






answer1 = 28
answer2 = 237

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1706, f'{answer1} {answer2}', 'ca4d656e61cf4b93ff4db984ee35e5dc'))