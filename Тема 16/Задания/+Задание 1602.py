# Решение
'''
dp = {}
for n in range(0,1000000000):
    if n == 0:
        dp[n] = 0
    elif n % 2 != 0:
        dp[n] = dp[n-1] + 1
    elif n % 2 == 0 and n > 0:
        dp[n] = dp[n//2]


c = 0
for i in range(1,1000000000):
    if dp[i] == 2:
        c += 1
print(c)
#
'''





answer = 435

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1602, answer, 'ddb30680a691d157187ee1cf9e896d03'))