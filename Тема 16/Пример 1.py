dp = {}

for n in range(-21,224357):
    if n <= 10:
        dp[n] = n
    elif n > 10:
        dp[n] = n - 12 + dp[n-21]

print((dp[224356] - dp[224272]) / dp[59])
#Ответ 12125


#LIMIT = 5000
#dp = [0] * LIMIT   # dp[n] = F(n)

#for n in range(1, LIMIT):
#    if n % 3 == 2:
#        dp[n] = dp[n - 1] + 1
#    else:
#        dp[n] = dp[(n - n % 3) // 3]

#for i in range(LIMIT):
#    if dp[i] == 6:
#        print(i)  # Результат: 728
#        break






#def f(n):
#    if n == 0:
#        return 0
#    elif n % 3 == 2 and n > 0:
#        return f(n - 1) + 1
#    elif n % 3 < 2 and n > 0:
#        return f((n - n % 3) // 3)
#
#for i in range(1000):
#    if f(i) == 6:
#        print(i)  # Результат: 728
#        break