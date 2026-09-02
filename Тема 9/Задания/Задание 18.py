# Решение
count_rows = 0
with open('Задание 18.txt') as file:
    mat = []
    for line in file:
        s = list(map(int,line.split('\t')))
        mat.append(s)
    st = []
    for i in range(len(mat[0])):
        ss = []
        for row in mat:
            ss.append(row[i])
        st.append(ss)
    for i in range(len(st)):
        for j in range(len(st[0])):
            c = 0
            t = st[i][j]
            for k in range(len(st[0])):
                if st[0][k] == t:
                    c += 1
                if 170 <= c:
                    continue
                else:
                    mat[j][i] = '+'

for row in mat:
    print(mat)






answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(9, 18, answer, '67388f1834f7d6243b753ec33584a8df'))