from turtle import*
tracer(0)
screensize(2000,2000)
k = 10

for i in range(2):
    forward(3*k)
    left(90)
    right(180)
    forward(10*k)
    right(180)
    left(90)

up()

right(180)
forward(10*k)
right(180)
right(90)
forward(8*k)
left(90)

down()

for i in range(2):
    forward(16 * k)
    right(90)
    forward(8 * k)
    right(90)

up()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*k,y*k)
        dot(3)

exitonclick()



answer = 185

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 6, answer, 'eecca5b6365d9607ee5a9d336962c534'))