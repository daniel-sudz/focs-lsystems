

import turtle as turtle
from typing import Callable, Dict, Optional

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
            visualizations: Optional[Dict[str, Callable[[turtle.Turtle], None]]] = None,
            debug: bool = True
    ):
        # copy over the init parameters
        self.start = start
        self.rules = rules
        self.iterations = iterations
        self.visualizations = visualizations
        self.debug = debug

        # define defaults actions
        self.no_visualize: Callable[[turtle.Turtle], None] = lambda x: None

        # intialize the visualization environment if needed
        if self.visualizations:
            turtle.setup()
            self.vis_turtle = turtle.Turtle()
            self.vis_screen = turtle.Screen()

            self.vis_turtle.color(0.0, 0.0, 0.0)
            self.vis_turtle.pencolor(0.0, 0.0, 0.0)

    def visualize(self, cur_string: str = None, iteration: int = 0):
        cur_string = cur_string or self.start
        
        # apply visualizations
        if self.visualizations:
            for char in cur_string:
                action = self.visualizations.get(char, self.no_visualize)
                action(self.vis_turtle)

        if iteration < self.iterations:
            # apply the rewrite rules
            new_string: str = ""
            for char in cur_string:
                new_string += self.rules.get(char, char)

            # print debug information on transformations
            if self.debug:
                if iteration == 0:
                    print("-" * 100)
                print(f"||Iteration: {iteration} || Value || {new_string} ||")
                if iteration == self.iterations:
                    print("-" * 100)
            
            # go to the next iteration
            self.visualize(new_string, iteration + 1)
        else:
            # make the python turtle GUI come up
            if self.visualizations:
                self.vis_screen.exitonclick()