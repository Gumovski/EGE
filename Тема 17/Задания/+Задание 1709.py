# Решение
s = list(map(int,open('Задание 1709.txt').readlines()))
c = 0
res = []
m = - 1000000
for j in range(len(s)):
    st = str(s[j])
    if st[-2] == '1' and st[-1] == '3' and m < s[j]:
        m = s[j]
for i in range(len(s)-2):
    s1 = len(str(s[i]))
    s2 = len(str(s[i+1]))
    s3 = len(str(s[i+2]))
    k = 0
    if s1 == 3:
        k += 1
    if s2 == 3:
        k += 1
    if s3 == 3:
        k += 1

    if k == 2 and s[i] +s[i+1] + s[i+2] <= m:
        c += 1
        res.append(s[i] +s[i+1] + s[i+2])

print(c)
print(max(res))







answer1 = 959
answer2 = 97471

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1709, f'{answer1} {answer2}', 'd5e09552bb0c4ea62e6672def4cf1b38'))