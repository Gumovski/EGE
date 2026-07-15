count_rows = []
row = []
c = 0
with open('Пример 1.txt','r', encoding='utf-8') as file:
    for line in file:
        c += 1
        s = list(map(int,line.split('\t')))
        s.sort()
        n = 0
        ma = max(s)
        mi = min(s)
        for num in set(s):
            if s.count(num) == 3:
                n = num

        if n!= 0 and len(set(s)) == 5:
            if (sum(set(s)) - n) // 4 <= n:
                if ma % mi != 0:
                    count_rows.append((sum(s),c))
print(max(count_rows[1]))
