# Решение
from turtle import *
# Отключает анимацию черепахи (Рисунок выводится сразу)
tracer(0)
screensize(2000,2000)
# Коэффициент, для увеличения масштаба изображения
koef = 20

# Алгоритм рисования фигуры
for i in range(2):
    forward(10 * koef)
    right(90)
    forward(18 * koef)
    right(90)
up()

forward(5 * koef)
right(90)
forward(7 * koef)
left(90)
down()

for i in range(2):
    forward(10 * koef)
    right(90)
    forward(7 * koef)
    right(90)

# Алгоритм рисования сетки
up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)

exitonclick()
