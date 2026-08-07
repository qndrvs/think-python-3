## EXERCISES
import turtle
t = turtle.Turtle()


# 1. Exercise
print("\nEXERCISE 1")
def rectangle(wide: float, tall: float) -> None:
    """
    Draw a rectangle using turtle graphics.

    Parameters
    ----------
    wide : float
        Width of the rectangle.
    tall : float
        Height of the rectangle.

    Returns
    -------
    None
    """
    for i in range(2):
        t.forward(wide)
        t.left(90)
        t.forward(tall)
        t.left(90)
rectangle(80, 40)
t.reset()
print("done\n")


# 2. Exercise
print("\nEXERCISE 2")
def rhombus(length: float, angle: float) -> None:
    """
    Draw a rhombus using turtle graphics.

    Parameters
    ----------
    length : float
        Length of each side.
    angle : float
        Interior angle, in degrees, at the starting vertex.

    Returns
    -------
    None
    """
    for i in range(2):
        t.forward(length)
        t.left(angle)
        t.forward(length)
        t.left(180 - angle)
rhombus(50, 60)
t.reset()
print("done\n")


# 3. Exercise
print("\nEXERCISE 3")
def parallelogram(l1: float, l2: float, angle: float) -> None:
    """
    Draw a parallelogram using turtle graphics.

    Parameters
    ----------
    l1 : float
        Length of the first pair of sides.
    l2 : float
        Length of the second pair of sides.
    angle : float
        Interior angle, in degrees, at the starting vertex.

    Returns
    -------
    None
    """
    for i in range(2):
        t.forward(l1)
        t.left(angle)
        t.forward(l2)
        t.left(180 - angle)
parallelogram(80, 50, 60)
t.reset()
print("done\n")


# 4. Exercise
print("\nEXERCISE 4")
import math
def polygon(sides: int, length: float) -> None:
    """
    Draw a regular star-like polygon using turtle graphics, alternating the main side length with a computed external side.

    Parameters
    ----------
    sides : int
        Number of main sides/points of the polygon.
    length : float
        Length of each main side.

    Returns
    -------
    None
    """
    central_angle = 360 / sides
    external_side = length * math.sqrt(2 * (1 - math.cos(central_angle * math.pi / 180)))
    for i in range(sides):
        if i == 0:
            t.right(central_angle / 2)
        t.forward(length)
        t.left((180 + central_angle) / 2)
        t.forward(external_side)
        t.left((180 + central_angle) / 2)
        t.forward(length)
        t.left(180)
polygon(5, 100)
t.reset()
polygon(6, 100)
t.reset()
polygon(7, 100)
t.reset()
print("done\n")


# 5. Exercise
print("\nEXERCISE 5")
import math
turtle.tracer(0)
def petal(angle: float, radius: float) -> None:
    """
    Draw a single flower petal (two mirrored circular arcs) using turtle graphics.

    Parameters
    ----------
    angle : float
        Opening angle of the petal, in degrees.
    radius : float
        Radius of the arcs that form the petal.

    Returns
    -------
    None
    """
    n = 360
    circle_length = 2 * math.pi * radius * angle / 360
    for i in range(n):
        if round(angle) == i: break
        t.forward(circle_length / angle)
        t.left(360 / n)
    t.left(180 - angle)
    for i in range(n):
        if round(angle) == i: break
        t.forward(circle_length / angle)
        t.left(360 / n)
    t.left(angle)
def flower(n_petals: int, angle: float, radius: float) -> None:
    """
    Draw a flower made of n_petals identical petals arranged in a circle.

    Parameters
    ----------
    n_petals : int
        Number of petals to draw.
    angle : float
        Opening angle of each petal, in degrees.
    radius : float
        Radius of the arcs that form each petal.

    Returns
    -------
    None
    """
    for i in range(n_petals):
        petal(angle, radius)
        t.left(360 / n_petals)
flower(7, 90, 150)
turtle.update()
input("Press enter")   # So the user can look at it carefully, since we set turtle.tracer(0) (instant drawing)
t.reset()
flower(9, 90, 150)
turtle.update()
input("Press enter")   # So the user can look at it carefully, since we set turtle.tracer(0) (instant drawing)
t.reset()
print("done\n")


# 6. Ask a virtual assistant
"""
It wasn't necessary, since I was able to work through it properly with Python's "turtle" library, so I didn't run into issues with any differences compared to the "jupyter turtle" library.
"""