import io
import turtle as turtle
import warnings
from typing import Callable, Dict, Optional
import imageio
import os
from PIL import Image
import numpy as np

ghostscript_path = os.path.join(os.path.dirname(__file__), 'ghostscript_bin', 'gs')
Image.GS_PROG = ghostscript_path

class ProductionRule:
    """
    Describe a production rule of an Lsystem (can be context-sensitive or not)

    @param from: the symbol to rewrite
    @param context_left: the context on the left (None if not-sensitive)
    @param context_right: the context on the right (None if not-sensitive)
    """
    def __init__(self, rewrite_from: str, context_left: Optional[str], context_right: Optional[str]):
        self.rewrite_from = rewrite_from
        self.context_left = context_left
        self.context_right = context_right

class LSystem:
    """
    Creates a Lsystem with the desired parameters

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
            rules: Dict[str, ProductionRule],
            iterations: int,
            visualizations: Optional[Dict[str, Callable[[turtle.Turtle], None]]] = None,
            render_start_pos: tuple[int, int] = (0, 0),
            render_heading: int = 0,
            debug: bool = True
    ):
        # cpy over the init parameters
        self.start = start
        self.rules = rules
        self.iterations = iterations
        self.visualizations = visualizations
        self.debug = debug
        self.render_start_pos = render_start_pos
        self.render_heading = render_heading

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

            # set turtle starting position and heading
            self.vis_turtle.penup()
            self.vis_turtle.setpos(render_start_pos)
            self.vis_turtle.setheading(render_heading)

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

            for idx, char in enumerate(cur_string):
                production_rule = self.rules.get(char, ProductionRule(char, None, None))

                # handle left_context
                if production_rule.context_left:
                    if (len(production_rule.context_left) > idx) or (cur_string[0:idx] != production_rule.context_left):
                        continue

                # handle right_context
                if production_rule.context_right:
                    if (len(production_rule.context_right) > (len(cur_string) - idx - 1)) or (cur_string[idx+1:len(cur_string)] != production_rule.context_right):
                        continue
                               
                new_string += self.rules.get(char, ProductionRule(char, None, None)).rewrite_from

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
