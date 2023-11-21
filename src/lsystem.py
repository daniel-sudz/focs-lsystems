

from turtle import Turtle
from typing import Callable, Dict

class LSystem:

    """
        Creates an Lsystem defined by (start, rules, iterations, visualization)

        @param start: the starting string for the 0th iteration
        @param rules: the production rules for rewriting a string
        @param iterations: the number of iterations to compute
        @param visuations: a list of callbacks to perform a visualization
        on each charecter change
    """
    def __init__(
            self,
            start: str,
            rules: Dict[str, str],
            iterations: int,
            visualization: Dict[str, Callable[[Turtle], None]]
    ):
        self.start = start
        self.rules = rules
        self.iterations = iterations
        self.visualization = visualization

    def visualize():
        pass