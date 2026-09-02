from turtle import*
tracer(0)
screensize(2000,2000)
k = 20


for i in range(4):
    for j in range(4):
        forward(6 * k)
        right(90)
    forward(10 * k)
    right(90)
    forward(x * k)
    right(90)






up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*k,y*k)
        dot(3)
exitonclick()