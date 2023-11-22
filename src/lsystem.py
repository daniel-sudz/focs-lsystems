import turtle as turtle
from typing import Callable, Dict, Optional


class LSystem:

    """
        Creates a Lsystem with desired parameters below:

        @param start: the starting string for the 0th iteration
        @param rules: the production rules for rewriting a string
        @param iterations: the number of iterations to compute
        @param visualizations: a list of callbacks to perform a visualization
        on each character change
        @param render_start_pos: a tuple for the start coordinates (int, int)
        for rendering the visualization
        @param debug: boolean to choose whether to print debug info or not
    """
    def __init__(
            self,
            start: str,
            rules: Dict[str, str],
            iterations: int,
            visualizations: Optional[Dict[str, Callable[[turtle.Turtle], None]]] = None,
            render_start_pos: tuple[int, int] = (0, 0),
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

        # initialize the visualization environment if needed
        if self.visualizations:
            # create the turtle
            turtle.setup()
            self.vis_turtle = turtle.Turtle()
            self.vis_screen = turtle.Screen()

            # modify speed and delay as desired
            self.vis_turtle.speed(0)  # 0 (fastest) - 10 (slowest)
            self.vis_screen.delay(0)

            # set turtle starting position
            self.vis_turtle.penup()
            self.vis_turtle.setpos(render_start_pos)

            # set turtle properties
            self.vis_turtle.pendown()
            self.vis_turtle.color(0.0, 0.0, 0.0)
            self.vis_turtle.pencolor(0.0, 0.0, 0.0)

    def visualize(self, cur_string: str = None, iteration: int = 0):
        cur_string = cur_string or self.start

        # print debug information on transformations
        if self.debug:
            if iteration == 0:
                print("-" * 100)
            print(f"||Iteration: {iteration} || Value || {cur_string} ||")
            if iteration == self.iterations:
                print("-" * 100)

        if iteration < self.iterations:
            # apply the rewrite rules
            new_string: str = ""
            for char in cur_string:
                new_string += self.rules.get(char, char)

            # go to the next iteration
            self.visualize(new_string, iteration + 1)
        else:
            if self.visualizations:
                # apply visualizations
                for char in cur_string:
                    action = self.visualizations.get(char, self.no_visualize)
                    action(self.vis_turtle)

                # make the GUI come up
                self.vis_screen.exitonclick()
