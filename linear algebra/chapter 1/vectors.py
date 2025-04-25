from manimlib import *




def MathTex(*a,**kw):
    return Tex(*a,**kw)


def Create(*a,**kw):
    return ShowCreation(*a,**kw)








class VectorExplanation(Scene):
    def construct(self):
        # Step 1: A line with no direction
        title1 = Text("Imagine a Line, this has no direction.", font="Arial", font_size=28).to_edge(UP)
        self.play(Write(title1))

        line = Line(LEFT*5, RIGHT*5, color=WHITE)
        self.play(ShowCreation(line))
        self.wait(4)

        # Step 2: Add direction
        title2 = Text("We can define a direction by giving an arrow.", font="Arial", font_size=28).to_edge(UP)
        self.play(Transform(title1, title2))

        arrow = Arrow(LEFT*5, RIGHT*5, buff=0, color=YELLOW)
        self.play(Transform(line, arrow))
        self.wait(4)

        # Step 3: Restrict to two points A and B
        title3 = Text("Now let's restrict this line to two points, A and B.", font="Arial", font_size=28).to_edge(UP)
        self.play(Transform(title1, title3))

        point_a = Dot(LEFT*3, color=BLUE)
        point_b = Dot(RIGHT*3, color=RED)
        label_a = Text("A", font_size=24).next_to(point_a, DOWN)
        label_b = Text("B", font_size=24).next_to(point_b, DOWN)
        ab_arrow = Arrow(LEFT*3, RIGHT*3, buff=0, color=GREEN)

        self.play(FadeOut(line), FadeIn(point_a), FadeIn(point_b), FadeIn(label_a), FadeIn(label_b))
        self.play(ShowCreation(ab_arrow))
        self.wait(4)

        # Step 4: Declare it as a vector
        title4 = Text("Ladies and gentlemen, this is nothing but a vector.", font="Arial", font_size=28).to_edge(UP)
        self.play(Transform(title1, title4))
        self.wait(4)

        title5 = Text("A vector has both magnitude and direction.", font="Arial", font_size=28).to_edge(UP)
        self.play(Transform(title1, title5))

        vector_label = Text("Vector", font_size=32, color=GREEN).next_to(ab_arrow, UP)
        self.play(Write(vector_label))
        self.wait(4)
