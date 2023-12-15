from src.lsystem import LSystem

"""
An implementation of the Sierpinski Triangle in our system
https://en.wikipedia.org/wiki/L-system#Example_5:_Sierpinski_triangle
"""

# Distance to move/write forward
distance = 10


# Function to move forward for Sierpinski Triangle
def move_forward(t):
    t.penup()
    t.forward(distance)
    t.pendown()


# Sierpinski Triangle LSystem
sierpinski_triangle = LSystem(
    start="F-F-F",
    rules=
    {
        "F": "F-G+F+G-F",
        "G": "GG"
    },
    iterations=5,
    visualizations=
    {
        "F": lambda t: t.forward(distance),
        "G": move_forward,
        "+": lambda t: t.left(120),
        "-": lambda t: t.right(120)
    },
    render_start_pos=(-300, -250),
    render_heading=90,
    debug=True
)

sierpinski_triangle.visualize()
