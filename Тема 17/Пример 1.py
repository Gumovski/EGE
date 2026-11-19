s = list(map(int,open('Пример 1.txt').readlines()))
res = []
c = 0
for i in range(len(s) - 1):
    if (s[i] * s[i + 1]) % 15 == 0 and (s[i] + s[i + 1]) % 7 == 0:
        res.append(s[i] + s[i + 1])
        c += 1

print(c,max(res))