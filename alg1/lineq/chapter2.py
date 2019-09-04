from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        title = TextMobject("Introduction to Linear Equations")
        title.scale(1.5)
        title.to_edge(UP)
        rect = ScreenRectangle(height=6)
        rect.next_to(title, DOWN)

        self.play(Write(title), Write(rect))
        self.wait()

        self.play(Uncreate(title), Uncreate(rect))
        self.wait()

        axes = Axes(
            x_min=-5,
            x_max=5,
            y_min=-3,
            y_max=3,
            number_line_config={
                "include_tip": False,
            }
        )

        f1 = FunctionGraph(lambda x: x)
        f2 = FunctionGraph(lambda x: 3*x, color=RED)

        self.play(Write(axes), Write(f1), Write(f2))
        self.wait()


class SlopeCalc(Scene):
    def construct(self):
        eq = TexMobject("y=0.5x+1")