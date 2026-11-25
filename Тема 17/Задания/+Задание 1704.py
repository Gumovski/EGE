# Решение
s = list(map(int,open('Задание 1704.txt').readlines()))
c = 0
res = []
m = 10 ** 6
for i in range(len(s)):
    sr = abs(s[i])
    st = str(sr)
    if len(st) == 3 and st[-1] == '5' and m > s[i]:
        m = s[i]
for i in range(len(s) - 1):
    s1 = len(str(abs(s[i])))
    s2 = len(str(abs(s[i+1])))
    k = 0
    if s1 == 3:
        k += 1
    if s2 == 3:
        k += 1
    if k == 1 and (s[i] + s[i+1]) % m == 0:
        c += 1
        res.append(s[i]+s[i+1])

print(c)
print(min(res))

answer1 = 2
answer2 = 33120

#

from tests.conftest import result_register
if answer1 is not Ellipsis and answer2 is not Ellipsis:
    print(result_register(17, 1704, f'{answer1} {answer2}', 'f3c45887478efcf9fcf722ab4708387d'))