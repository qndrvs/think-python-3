## EXERCISES
import time
import turtle
t = turtle.Turtle()


# 1. Ask a virtual assistant
"""
a)
There are multiple uses for the modulo operator, such as:
- Extracting the last n digits of a number: number % pow(10, n_last_digits)
- Checking the parity of a number: number % 2 Among others.

b)
For boolean values, we can use: a != b, where a and b are boolean values.

c)
if x == y:
    print('x and y are equal')
elif x < y:
    print('x is less than y')
else:
    print('x is greater than y')

d)
if 0 < x < 10:
    print('x is a positive single-digit number.')

e)
def countdown_by_two(n):
    if n == 0:
        print('Blastoff!')
    else:
        print(n)
        countdown_by_two(n - 2)
The bug would occur when n is odd, since n would skip past 0 (going straight from 1 to -1) and the base case n == 0 would never be reached, causing infinite recursion. The fix is to use n <= 0 as the base case instead of n == 0, as shown below.

def countdown_by_two(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown_by_two(n - 2)
"""


# 2. Exercise
print("\nEXERCISE 2")
days = time.time() // (24 * 60 * 60)
print(days)   # days since January 1, 1970
clean_day = time.time() % (24 * 60 * 60)
hours = int(clean_day // (60 * 60))
minutes = int((clean_day % (60 * 60)) // 60)
seconds = int((clean_day % (60 * 60)) % 60)
print(str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s")


# 3. Exercise
print("\nEXERCISE 3")
def is_triangle(a: float, b: float, c: float) -> None:
    """
    Print whether three side lengths can form a valid triangle, based on the triangle inequality.

    Parameters
    ----------
    a : float
        First side length.
    b : float
        Second side length.
    c : float
        Third side length.

    Returns
    -------
    None
    """
    if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
        print("Yes")
    else:
        print("No")
is_triangle(2, 12, 5)


# 4. Exercise
"""
iteration 1:
    recurse(2, 3)
iteration 2:
    recurse(1, 5)
iteration 3:
    recurse(0, 6)
iteration 4:
    print(s = 6)
"""


# 5. Exercise
"""
Draws a shape of progressively smaller "root-like" branches (down to a minimum no smaller than or equal to 5).
"""
print("\nEXERCISE 5")
def draw(length: float) -> None:
    """
    Recursively draw a branching root-like pattern using turtle graphics.

    Parameters
    ----------
    length : float
        Length of the current branch. Recursion stops once the branch length is 5 or smaller.

    Returns
    -------
    None
    """
    angle = 50
    factor = 0.6
    if length > 5:
        t.forward(length)
        t.left(angle)
        draw(factor * length)
        t.right(2 * angle)
        draw(factor * length)
        t.left(angle)
        t.back(length)
draw(50)
t.reset()
print("done\n")


# 6. Exercise
print("\nEXERCISE 6")
def koch(length: float) -> None:
    """
    Recursively draw one side of a Koch curve/snowflake using turtle graphics.

    Parameters
    ----------
    length : float
        Length of the current segment. Recursion stops once the segment length drops below 5.

    Returns
    -------
    None
    """
    if length < 5:
        t.forward(length)
        return
    koch(length/3)
    t.left(60)
    koch(length/3)
    t.right(120)
    koch(length/3)
    t.left(60)
    koch(length/3)
koch(120)
t.reset()
print("done\n")


# 7. Exercise
print("\nEXERCISE 7")
def sierpinski(t: turtle.Turtle, order: int, length: float) -> None:
    """
    Recursively draw a Sierpinski triangle using turtle graphics.

    Parameters
    ----------
    t : turtle.Turtle
        The turtle instance used to draw.
    order : int
        Recursion depth. order == 0 draws a single filled-in triangle outline; higher values subdivide it further.
    length : float
        Side length of the current triangle.

    Returns
    -------
    None
    """
    if order == 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
    else:
        sierpinski(t, order - 1, length / 2)
        t.forward(length / 2)
        sierpinski(t, order - 1, length / 2)
        t.backward(length / 2)
        t.left(60)
        t.forward(length / 2)
        t.right(60)
        sierpinski(t, order - 1, length / 2)
        t.left(60)
        t.backward(length / 2)
        t.right(60)
def main() -> None:
    """
    Set up the turtle screen and draw a Sierpinski triangle.

    Returns
    -------
    None
    """
    screen = turtle.Screen()
    screen.title("Sierpinski Triangle")
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)           # maximum speed
    t.hideturtle()
    t.penup()
    t.goto(-200, -150)   # starting position (bottom-left corner)
    t.pendown()
    ORDER = 4            # change this value (0-6 recommended)
    LENGTH = 400         # base triangle size
    sierpinski(t, ORDER, LENGTH)
    screen.mainloop()
main()
print("done\n")