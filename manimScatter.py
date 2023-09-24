import pandas as pd
import os
from manim import *

class Scatter(Scene):
    def construct(self):
        # Download data and put in DataFrame
        data_url = "https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/regression/linear_normal.csv"

        df = pd.read_csv(data_url)

        # Add the Axes
        ax = Axes(x_range=[0, 100, 5], y_range=[-20, 200, 10])
        self.add(ax)

        # Add the dots
        for x, y in df.values:
            dot = Dot(ax.c2p(x, y), color=BLUE)
            self.add(dot)

class ScatterAnimated(Scene):

    def construct(self):
        # Download data and put in DataFrame
        self.camera.background_color = WHITE

        scatterText = Text("Scatter Plot From Pulled .csv Data!", color = BLACK).to_edge(UP)
        data_url = "https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/regression/linear_normal.csv"
        dataText = Text("https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/regression/linear_normal.csv", color = BLACK).next_to(scatterText, DOWN, buff = 0.2).scale(0.25)

        df = pd.read_csv(data_url)

        # Animate the creation of Axes
        ax = Axes(x_range=[0, 100, 5], y_range=[-20, 200, 10]).set_color(BLACK)

        self.play(Write(scatterText))
        self.play(Write(ax))

        self.wait()  # wait for 1 second

        # Animate the creation of dots
        dots = [Dot(ax.c2p(x, y), color=BLUE) for x, y in df.values]
        self.play(LaggedStart(*[Write(dot) for dot in dots], lag_ratio=.05))

        self.wait()  # wait for 1 second
        self.play(Write(dataText))
        self.wait(2)

        trendLine = ax.plot(lambda x: 1.9*x + 1, x_range = [0,95], color = RED)
        trendLineText = Text("Add A Trendline Even!", color = RED).to_edge(DOWN)
        self.play(Write(trendLineText))
        self.play(Create(trendLine), run_time = 3)
        self.wait()