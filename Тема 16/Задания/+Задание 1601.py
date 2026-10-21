# Решение
'''
dp = {}

for n in range(1,100000000):
    if n % 2 == 0:
        dp[n] = dp[n//2] + 3
    elif n % 2 != 0 and n % 3 == 0:
        dp[n] = dp[n//3] + 2
    elif n % 2 != 0 and n % 3 != 0:
        dp[n] = 0

for i in range(1,100000000):
    if dp[i] == 67:
        print(i)
        break
'''
#18874368



answer = 18874368

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(16, 1601, answer, 'd43416548c620037459b5607111f8eb5'))