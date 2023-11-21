from src.lsystem import LSystem

"""
    An implementation of the Koch Curve Visualization in our system
    https://en.wikipedia.org/wiki/L-system#Example_4:_Koch_curve
"""
koch_curve = LSystem(
    "F",
    {
        "F": "F+F−F−F+F",
    },
    1,
    {
        "F": lambda t: t.forward(100),
        "+": lambda t: t.left(90),
        "-": lambda t: t.right(90)
    }
    
)

koch_curve.visualize()
