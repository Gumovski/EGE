# Решение
"""
from turtle import*

tracer(0)
screensize(2000,2000)
k = 3

right(180)
for i in range(9):
    forward(59*k)
    left(90)
    forward(84 * k)
    left(90)
up()

forward(18*k)
left(90)
forward(38*k)
right(90)

down()
for i in range(9):
    forward(120 * k)
    right(90)
    forward(99 * k)
    right(90)

up()


exitonclick()
"""
answer = 158

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 62, answer, '06409663226af2f3114485aa4e0a23b4'))