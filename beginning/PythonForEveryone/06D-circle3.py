import turtle as t

t.bgcolor("black")
t.color("yellow")
t.speed(1)
for x in range(1, 10+1):
    t.circle(5 * x)
    t.right(90)
    t.forward(5 * x)
    t.left(90)
