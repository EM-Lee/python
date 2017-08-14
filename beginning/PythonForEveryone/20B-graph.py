import turtle as t

x_min = -5
x_max = 5

y_min = -5
y_max = 5

space = 0.1

func_list = ["y = x * x", "y = abs(x)", "y = 0.5 * x + 1"]
color_list = ["green", "red", "blue"]

t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.speed(10)
t.pensize(2)

# drawing x axis
t.up()
t.goto(x_min, 0)
t.down()
t.goto(x_max, 0)

# drawing y axis
t.up()
t.goto(0, y_min)
t.down()
t.goto(0, y_max)

# drawing graphs
# https://www.dotnetperls.com/zip-python
# https://www.programiz.com/python-programming/methods/built-in/zip
for func, color in zip(func_list, color_list):
    x = x_min
    exec(func)
    t.up()
    t.goto(x, y)
    t.down()
    t.color(color)
    while x <= x_max:
        x = x + space
        exec(func)
        t.goto(x, y)
