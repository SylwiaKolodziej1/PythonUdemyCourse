import math
from enum import IntEnum

Menu_Figures = IntEnum("Menu_Figures", "rectangle, square, triangle, trapeze, circle")

def rectangle_surface(a, b):
    if (a <= 0 or b <= 0):
        return
    return a * b

def square_surface(a):
    if (a <= 0):
        return
    return a ** 2

def triangle_surface(a, h):
    if (a <= 0 or h <= 0):
        return
    return 0.5 * a * h

def trapeze_surface(a, b, h):
    if (a <= 0 or b <= 0 or h <= 0):
        return
    return 0.5 * (a + b) * h

def circle_surface(r):
    if (r <= 0):
        return
    return math.pi * r ** 2

x = int(input("""Choose what surface you want to calculate:
1 - rectangle
2 - square
3 - triangle
4 - trapeze
5 - circle
"""))

if (x == Menu_Figures.rectangle):
    a = int(input("Give a: "))
    b = int(input("Give b: "))
    print(rectangle_surface(a, b))
elif (x == Menu_Figures.square):
    a = int(input("Give a: "))
    print(square_surface(a))
elif (x == Menu_Figures.triangle):
    a = int(input("Give a: "))
    h = int(input("Give h: "))
    print(triangle_surface(a, h))
elif (x == Menu_Figures.trapeze):
    a = int(input("Give a: "))
    b = int(input("Give b: "))
    h = int(input("Give h: "))
    print(trapeze_surface(a, b, h))
elif (x == Menu_Figures.circle):
    r = int(input("Give r: "))
    print(circle_surface(r))
else:
    print("You've chosen wrong option, choose again")
