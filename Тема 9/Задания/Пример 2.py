ans = 0
d = [{} for j in range(6)]

with open('Пример2.txt') as file:
    for line in file:
        s = list(map(int,line.split('\t')))
        for i in range(6):
            if s[i] not in d[i]:
                d[i][s[i]] = 1
            else:
                d[i][s[i]] += 1

with open('Пример2.txt') as file:
    for line in file:
        s = list(map(int,line.split('\t')))
        x = 0
        for i in range(6):
            if s.count(s[i]) == 1 and d[i][s[i]] > 150:
                x += 1
        if x >= 5:
            ans += 1

print(ans)

#9527

