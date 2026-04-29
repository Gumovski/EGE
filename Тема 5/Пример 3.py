# Ответ: 123441358

def f(n):
    b = bin(n)[2:]
    for _ in range(3):
        c = str(n).count('2') + str(n).count('4') + str(n).count('6') + str(n).count('8') + str(n).count('0')
        nc = str(n).count('1') + str(n).count('3') + str(n).count('5') + str(n).count('7')
        if c > nc:
            b += '1'
        elif c < nc:
            b += '0'
        else:
            if n % 2 == 0:
                b += '0'
            else:
                b += '1'
        n = int(b, 2)
    return n

'''
for i in range(1, 1000):
    print(i, f(i), f(i) // i)
'''

# 8

print(f(123456789))

count = 0
start = 123459 # Ближайшее число (слева), результат алгоритма которого попадает в диапазон
finish = 987654316 # Ближайшее число (справа), результат алгоритма которого попадает в диапазон
while start <= finish:
    count += 1
    start += 8
print(count)


