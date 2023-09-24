from manim import *
import random as rd
import math
from manim_rubikscube import *


class Data(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        hello = Text("Hello World!", color = BLACK)
        hook = Text("Today, I'm Going To Show You How Your Data Could Look", font_size = 30, color = BLACK).shift(DOWN*2)
        
        self.play(Write(hello))
        self.wait()
        self.play(Write(hook), run_time = 2)
        self.wait()
        self.play(FadeOut(hello))
        self.play(hook.animate.shift(UP*5))
        ul = Underline(hook).set_color(BLACK)
        self.play(Create(ul))
        self.wait()

        colorList = (RED, BLUE, PURPLE, GREEN, ORANGE)
        graphsIntro = Text("Firstly, Graphs Need ", color = BLACK, font_size = 30).shift(LEFT*4)
        graphsIntro2 = Text("COLOR", font_size = 40).next_to(graphsIntro, RIGHT).set_color(color=[RED, BLUE, GREEN, ORANGE, PURPLE])
        
        self.play(Write(graphsIntro))
        self.wait(0.5)
        self.play(Write(graphsIntro2))
        self.wait(2)

        axes1 = Axes(x_range=[0,10,1], y_range=[0,10,1], tips = True).set_color(BLACK)
        xlabel1 = axes1.get_x_axis_label("x").set_color(BLACK)
        ylabel1 = axes1.get_y_axis_label("y").set_color(BLACK)
        graph1 = axes1.plot(lambda x: 2*math.log(x+1), x_range=[0.001, 10]).set_color(BLUE)
        self.play(Create(axes1), run_time = 2)
        self.play(Create(xlabel1),Create(ylabel1))
        self.wait()
        self.play(Create(graph1), run_time = 2)
        self.wait()
        
        self.play(FadeOut(graphsIntro, shift = RIGHT),FadeOut(graphsIntro2, shift = RIGHT))
        self.wait()
        self.play(FadeOut(axes1), FadeOut(xlabel1), FadeOut(ylabel1), FadeOut(graph1))
        self.wait(2)
        hook2 = Text("3D Models Make Your Presentation Better!", font_size = 30, color = BLACK).shift(UP*3)
        self.play(ReplacementTransform(hook, hook2))
        self.wait(2)

        cube = RubiksCube().scale(0.5)
        cube.move_to(ORIGIN)
         # Setup where the camera looks
        self.move_camera(phi=50*DEGREES, theta=160*DEGREES)
        self.renderer.camera.frame_center = cube.get_center()

         # At this point, you have created a RubiksCube object.
         # All that's left is to add it to the scene.

         # A RubiksCube acts as any other Mobject. It can be added with
         # self.add() or any Manim creation animation
        self.play(
            FadeIn(cube)
        )

         # Rotate the camera around the RubiksCube for 8 seconds
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(4)

        self.play(FadeOut(cube), FadeOut(hook2), FadeOut(ul), run_time = 3)
        self.wait()

