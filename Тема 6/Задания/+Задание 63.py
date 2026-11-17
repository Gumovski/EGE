# Решение
'''
from turtle import*
tracer(0)
screensize(20000,20000)
k = 10

left(90)
for i in range(7):
    forward(17*k)
    right(90)
    forward(26*k)
    right(90)
up()

forward(4*k)
right(90)
forward(6*k)
left(90)
down()

for i in range(7):
    forward(278*k)
    right(90)
    forward(345*k)
    right(90)
up()

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k, y * k)
        dot(3)

exitonclick()

#21*14 = 294
#27*18 - 294 = 192
279*346 - 294 = 96240
#96240 + 294 + 192 = 96726
'''



answer = 96726

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 63, answer, '35495f83adcdab84ab446b313a3e0cb4'))