import turtle
import random
from typing import List, Tuple, Dict, Optional, Callable


def choose_random_rule(rules: List[Tuple[str, float]]) -> str:
    total_prob = sum(prob for _, prob in rules)
    rand_num = random.uniform(0, total_prob)
    cumulative_prob = 0

    for rule, prob in rules:
        cumulative_prob += prob
        if rand_num <= cumulative_prob:
            return rule

    # This should not happen, but in case of rounding errors
    return rules[-1][0]


class StochasticLSystem:
    """
    Creates a Stochastic Lsystem with the desired parameters

    @param start: the starting string for the 0th iteration
    @param rules: the production rules for rewriting a string
    @param iterations: the number of iterations to compute
    @param visualizations: a list of callbacks to perform a visualization
    on each character change
    @param render_start_pos: a tuple for the start coordinates (int, int)
    for rendering the visualization
    @param render_heading: sets the orientation angle of the turtle
    @param debug: boolean to choose whether to print debug info or not
    """
    def __init__(
            self,
            start: str,
            rules: Dict[str, List[Tuple[str, float]]],
            iterations: int,
            visualizations: Optional[Dict[str, Callable[[turtle.Turtle], None]]] = None,
            render_start_pos: Tuple[int, int] = (0, 0),
            render_heading: int = 0,
            debug: bool = True
    ):
        self.start = start
        self.rules = rules
        self.iterations = iterations
        self.visualizations = visualizations
        self.debug = debug
        self.vis_turtle = turtle.Turtle()
        self.vis_screen = turtle.Screen()

        self._initialize_turtle(render_start_pos, render_heading)

    def _initialize_turtle(self, start_pos, heading):
        self.vis_turtle.speed(0)
        self.vis_screen.delay(0)
        self.vis_turtle.penup()
        self.vis_turtle.setpos(start_pos)
        self.vis_turtle.setheading(heading)
        self.vis_turtle.pendown()
        self.vis_turtle.color(0.0, 0.0, 0.0)
        self.vis_turtle.pencolor(0.0, 0.0, 0.0)

    def visualize(self, cur_string: str = None, iteration: int = 0):
        cur_string = cur_string or self.start

        if self.debug:
            if iteration == 0:
                print("-" * 100)
            print(f"||Iteration: {iteration} || Value || {cur_string} ||")
            if iteration == self.iterations:
                print("-" * 100)

        if iteration < self.iterations:
            new_string = self.apply_stochastic_rules(cur_string)
            self.visualize(new_string, iteration + 1)
        else:
            if self.visualizations:
                for char in cur_string:
                    action = self.visualizations.get(char, self.visualize)
                    action(self.vis_turtle)

                self.vis_screen.exitonclick()

    def apply_stochastic_rules(self, cur_string: str) -> str:
        new_string = ""
        for char in cur_string:
            rule = self.rules.get(char, [(char, 1.0)])
            new_string += choose_random_rule(rule)

        return new_string
