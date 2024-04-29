from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class BetaReduction(Scene):
    def construct(self):
        start = MathTex(r'(\lambda {{x}} . {{(x\ x)}}) {{y}}')
        with_subst = MathTex(r'{{(x\ x)}} [{{y}} / {{x}}]')
        final = MathTex(r'{{(y\ y)}}')
        self.play(Write(start))
        self.play(TransformMatchingTex(start, with_subst))
        self.play(Transform(with_subst, final))

class MatchingEquationParts(Scene):
    def construct(self):
        # variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)

        eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
        eq2 = MathTex("{{i}}^2", "+", "{{j}}^2", "=", "{{k}}^2")
        eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")

        self.add(eq1)
        self.wait(0.5)
        # self.play(TransformMatchingTex(Group(eq1, variables), eq2))
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(0.5)
