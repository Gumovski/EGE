# Решение

from turtle import*

tracer(0)
screensize(2000,2000)
k = 20

x = 3
forward((x + 2) * k)
for i in range(4):
    forward(x * k)
    right(90)
    forward((x + 2) * k)
right(90)
forward((x * 2) * k)
for i in range(4):
    right(90)
    forward(((x * 3) - 1) * k)

penup()
for z in range(-20,100):
    for y in range(-20, 100):
        goto(z * k, y*k)
        dot(3)

exitonclick()

s = []
for x in range(1,100):
    s1 = (x+2 + x)**2
    s2 = ((x*3)-1)**2
    s3 = 2 * x * (x + 2)
    res = s1 + s2 - s3
    s.append(res)
    if res > 2000:
        print(x)
        print(s)
        break



answer = 14

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 61, answer, 'aab3238922bcc25a6f606eb525ffdc56'))