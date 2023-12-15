from src.stochastic_lsystem import StochasticLSystem

"""
An implementation of the Fractal plant in our Stochastic L-system
http://algorithmicbotany.org/papers/abop/abop.pdf - Page 28 (Section 1.7)
"""

# List to store stack
stack = []


# Functions to push/pop stack for fractal plant
def push_stack(t):
    stack.append((t.pos(), t.heading()))


def pop_stack(t):
    pos, heading = stack.pop()
    t.setpos(pos)
    t.setheading(heading)


# Fractal Plant Stochastic LSystem with stochastic rules
fractal_plant = StochasticLSystem(
    start="F",
    rules=
    {
        "F":
        [
            ("F[+F]F[-F]F", 0.33),  # Probability 1/3
            ("F[+F]F", 0.33),       # Probability 1/3
            ("F[-F]F", 0.34)        # Probability 1/3
        ]
    },
    iterations=5,
    visualizations={
        "F": lambda t: t.forward(5),
        "+": lambda t: t.left(25),
        "-": lambda t: t.right(25),
        "[": push_stack,
        "]": pop_stack
    },
    render_start_pos=(0, -400),
    render_heading=90,
    debug=True
)

# Visualize the Stochastic Fractal Plant
fractal_plant.visualize()
