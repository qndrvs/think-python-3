import turtle

class MyTurtle:
    def __init__(self, x=0, y=0):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0) # Maximum speed
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
    
    def jumpto(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
    
    def moveto(self, x, y):
        self.t.goto(x, y)
    
    def circle(self, radius):
        self.t.circle(radius)
    
    def clear_screen(self):
        self.t.clear()
        self.t.reset()

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        if not isinstance(other, Point): return False
        return abs(self.x - other.x) < 0.001 and abs(self.y - other.y) < 0.001

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Line({self.p1}, {self.p2})"

    def draw(self, t: MyTurtle):
        t.jumpto(self.p1.x, self.p1.y)
        t.moveto(self.p2.x, self.p2.y)
    
# 2. Exercise 2
    def __eq__(self, other):
        if not isinstance(other, Line): return False
        return (self.p1 == other.p1 and self.p2 == other.p2) or \
               (self.p1 == other.p2 and self.p2 == other.p1)

# 3. Exercise 3
    def midpoint(self):
        mid_x = (self.p1.x + self.p2.x) / 2
        mid_y = (self.p1.y + self.p2.y) / 2
        return Point(mid_x, mid_y)

class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(corner={self.corner}, width={self.width}, height={self.height})"

    def get_corners(self):
        p1 = self.corner
        p2 = Point(self.corner.x + self.width, self.corner.y)
        p3 = Point(self.corner.x + self.width, self.corner.y + self.height)
        p4 = Point(self.corner.x, self.corner.y + self.height)
        return [p1, p2, p3, p4]

    def make_lines(self):
        corners = self.get_corners()
        return [
            Line(corners[0], corners[1]), 
            Line(corners[1], corners[2]), 
            Line(corners[2], corners[3]), 
            Line(corners[3], corners[0])
        ]

    def draw(self, t: MyTurtle):
        corners = self.get_corners()
        for i in range(4):
            t.jumpto(corners[i].x, corners[i].y)
            t.moveto(corners[(i + 1) % 4].x, corners[(i + 1) % 4].y)

# 4. Exercise 4
    def midpoint(self):
        center_x = self.corner.x + (self.width / 2)
        center_y = self.corner.y + (self.height / 2)
        return Point(center_x, center_y)

# 5. Exercise 5
    def make_cross(self):
        lines = self.make_lines()
        m_top = lines[0].midpoint()
        m_right = lines[1].midpoint()
        m_bottom = lines[2].midpoint()
        m_left = lines[3].midpoint()
        cross_v = Line(m_top, m_bottom)
        cross_h = Line(m_left, m_right)
        
        return [cross_v, cross_h]

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f"Circle(center={self.center}, radius={self.radius})"

    def draw(self, t: MyTurtle):
        
        start_x = self.center.x
        start_y = self.center.y - self.radius
        
        t.jumpto(start_x, start_y)
        t.t.setheading(0) 
        t.t.circle(self.radius)