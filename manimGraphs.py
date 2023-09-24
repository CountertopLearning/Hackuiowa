from manim import *

class GraphShowcase(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes1 = Axes(
            x_range = [0,10,1],
            y_range = [0,30, 6],
            axis_config={"include_tip": False}
        ).set_color(BLACK)

        t = ValueTracker(0)
        g = ValueTracker(1)
        def func(x):
            return (x-5)**2
        graph1 = axes1.plot(func, color = RED)

        labels = axes1.get_axis_labels(x_label="x", y_label=f"f(x)=x^{2}").set_color(BLACK)
        dot1 = Dot(point=[axes1.c2p(t.get_value(), func(t.get_value()))]).set_color(BLACK)
        dot1.add_updater(lambda x: x.move_to(axes1.c2p(t.get_value(), func(t.get_value()))))
        dot2 = Dot(point=[axes1.c2p(g.get_value(), func(g.get_value()))]).set_color(BLACK)
        dot2.add_updater(lambda x: x.move_to(axes1.c2p(g.get_value(), func(g.get_value()))))
        secantLine1 = Line(
            start=[dot1.get_center()],
            end=[dot2.get_center()] 
            ).set_color(BLUE)
        secantLine1.add_updater(lambda z: z.become(Line(dot1.get_center(), dot2.get_center()).set_color(BLUE)))

        self.play(Create(axes1))
        self.play(Create(graph1), Create(dot1), Create(dot2), run_time = 2)
        self.wait()
        self.play(Create(secantLine1))
        self.wait()
        self.play(FadeIn(labels))
        slopeExplanation = Text("Animations Can Help Understand Inclines And Declines In Data", color = BLACK).scale(0.5).to_edge(UP+RIGHT)
        self.play(Write(slopeExplanation))
        self.play(t.animate.set_value(5), g.animate.set_value(1))
        self.wait()

        self.play(t.animate.set_value(8), g.animate.set_value(4))
        self.wait()

        self.play(t.animate.set_value(1), g.animate.set_value(2.5))
        self.wait()

        self.play(t.animate.set_value(1), g.animate.set_value(10))
        self.wait()

        self.play(t.animate.set_value(3.2), g.animate.set_value(3))
        self.wait(2)
        self.play(FadeOut(slopeExplanation, shift = UP))
        self.play(FadeOut(axes1), FadeOut(graph1), FadeOut(dot1), FadeOut(dot2), FadeOut(labels), FadeOut(secantLine1))
        self.wait()

        chart = BarChart(
            values=[-5, 40, -10, 20, -3],
            bar_names=["one", "two", "three", "four", "five"],
            y_range=[-20, 50, 10],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 36},
        ).set_color(BLACK)

        c_bar_lbls = chart.get_bar_labels(font_size=48).set_color(BLACK)

        self.play(Create(chart), Create(c_bar_lbls), run_time = 2)
        self.play(Write(Text("Bar Graphs Can Be Created From Live Data", color = BLACK, font_size = 35).to_edge(UP)))
        self.wait(3)

        #self.play(FadeOut(chart, shift = DOWN), FadeOut(c_bar_lbls, shift = DOWN))

        