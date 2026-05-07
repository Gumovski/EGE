# Решение
from turtle import *
tracer(0)
screensize(2000,2000)
koef = 40

for i in range(4):
    forward(14 * koef)
    right(90)
for i in range(5):
    forward(5 * koef)
    right(45)

up()

for x in range(-20,20):
    for y in range(-20,20):
        goto(x*koef, y * koef)
        dot(2)

exitonclick()


answer = 59

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 15, answer, '093f65e080a295f8076b1c5722a46aa2'))