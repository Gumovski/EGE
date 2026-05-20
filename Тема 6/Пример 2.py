'''
from turtle import*
tracer(0)
screensize(2000,2000)
k = 20


x = 4
for i in range(4):
    forward(x * k)
    right(90)
    forward(x * k)
    left(90)
    forward(x * k)
    right(90)






up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k,y*k)
        dot(3)
exitonclick()
'''
for x in range(1,100):
    res = (5 * (x-1)**2) + ((x-1) * 4)
    if res > 1000:
        print(x)
        exit()