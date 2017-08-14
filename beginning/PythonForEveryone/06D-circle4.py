import turtle as t

t.bgcolor("black")
t.color("green")
t.speed(10)
for x in range(1, 10+1):
    t.circle(10 * x)
    t.right(90)
    t.forward(10)
    t.left(90)
