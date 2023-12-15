from src.lsystem import LSystem, ProductionRule

"""
An implementation of the Dragon curve Visualization in our system
https://en.wikipedia.org/wiki/L-system#Example_6:_dragon_curve
"""

# Dragon curve LSystem
dragon_curve = LSystem(
    start="F",
    rules=
    {
        "F": ProductionRule("F+G", None, None),
        "G": ProductionRule("F-G", None, None)
    },
    iterations=10,
    visualizations=
    {
        "F": lambda t: t.forward(10),
        "G": lambda t: t.forward(10),
        "+": lambda t: t.left(90),
        "-": lambda t: t.right(90)
    },
    render_start_pos=(-200, 0),
    render_heading=270,
    debug=True
)

dragon_curve.visualize()