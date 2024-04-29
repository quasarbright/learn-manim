from manim import *

class BetaReduction(Scene):
    def construct(self):
        start = MathTex(r'(\lambda {{x}} . {{(x\ x)}}) {{y}}')
        with_subst = MathTex(r'{{(x\ x)}} [{{y}} / {{x}}]')
        final = MathTex(r'{{(y\ y)}}')
        self.play(Write(start))
        self.play(TransformMatchingTex(start, with_subst))
        self.play(Transform(with_subst, final))