# Решение
'''
from turtle import*
tracer(1)
screensize(2000,2000)
k = 10

left(90)
for i in range(2):
    forward(23*k)
    right(90)
    forward(10*k)
    right(90)

forward(3*k)
left(90)
forward(12*k)
right(90)

for i in range(2):
    forward(9*k)
    right(90)
    forward(32*k)
    right(90)
up()

exitonclick()
'''





answer = 110

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 65, answer, '5f93f983524def3dca464469d2cf9f3e'))