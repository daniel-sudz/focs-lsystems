from src.lsystem import LSystem

"""
    An implementation of the Cantor Set Visualization in our system
    https://en.wikipedia.org/wiki/L-system#Example_4:_Koch_curve
"""
cantor_set = LSystem(
    "F",
    {
        "F": "F+F-F-F+F",
    },
    3,
    {
        "F": lambda t: t.forward(30),
        "+": lambda t: t.left(90),
        "-": lambda t: t.right(90)
    },
    (-500, 0),
    True
)

cantor_set.visualize()
