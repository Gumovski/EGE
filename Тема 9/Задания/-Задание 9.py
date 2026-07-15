# Решение
count_rows = 0
with open('Задание 9.txt') as file:
    for line in file:
        s = list(map(int,line.split('\t')))
        s.sort()
        m = s[-1]
        c = 0
        suma = 0
        for i in range(len(s)):
            suma += s[i]
            if s[i] == m:
                c += 1
        if c != 1:
            continue
        if len(set(s)) > 5:
            continue
        suma =  suma - m
        if (m * 3) > (suma):
            count_rows += 1

print(count_rows)




answer = 485

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(9, 9, answer, '812b4ba287f5ee0bc9d43bbf5bbe87fb'))