from src.lsystem import LSystem

"""
    An implementation of the Koch curve Visualization in our system
    https://en.wikipedia.org/wiki/L-system#Example_4:_Koch_curve
"""

# Koch curve LSystem
koch_curve = LSystem(
    start="F",
    rules=
    {
        "F": "F+F-F-F+F",
    },
    iterations=3,
    visualizations=
    {
        "F": lambda t: t.forward(30),
        "+": lambda t: t.left(90),
        "-": lambda t: t.right(90)
    },
    render_start_pos=(-400, 0),
    debug=True
)

koch_curve.visualize()
