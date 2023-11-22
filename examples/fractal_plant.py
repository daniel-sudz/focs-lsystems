from src.lsystem import LSystem

"""
An implementation of the Fractal plant in our system
https://en.wikipedia.org/wiki/L-system#Example_7:_fractal_plant
"""


# list to store stack
stack = []


# Functions to push/pop stack for fractal plant
def push_stack(t):
    stack.append((t.pos(), t.heading()))


def pop_stack(t):
    pos, heading = stack.pop()
    t.setpos(pos)
    t.setheading(heading)


# Fractal Plant LSystem
fractal_plant = LSystem(
    start="X",
    rules=
    {
        "X": "F+[[X]-X]-F[-FX]+X",
        "F": "FF"
    },
    iterations=6,
    visualizations=
    {
        "F": lambda t: t.forward(5),
        "+": lambda t: t.left(25),
        "-": lambda t: t.right(25),
        "[": push_stack,
        "]": pop_stack
    },
    render_start_pos=(-250, -400),
    render_heading=70,
    debug=True
)

# Visualize the Fractal Plant
fractal_plant.visualize()
