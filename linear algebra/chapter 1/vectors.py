from manimlib import *




def MathTex(*a,**kw):
    return Tex(*a,**kw)


def Create(*a,**kw):
    return ShowCreation(*a,**kw)








class VectorExplanation(Scene):
    """
    This is taken from NCERT Class 11, Chapter 1, Vectors.
    The scene explains the concept of vectors in a step-by-step manner."""
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



class Part1(Scene):
    def construct(self):
        title = Text("Matrices", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        
 
        matrix_tex = r"""
        M = \begin{bmatrix}
        e_{11} & e_{12} & \cdots & e_{1n} \\
        e_{21} & e_{22} & \cdots & e_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        e_{m1} & e_{m2} & \cdots & e_{mn}
        \end{bmatrix}
        """

        matrix = Tex(matrix_tex)
        matrix.scale(1.2)  # Optional: scale up for better visibility
        matrix.move_to(ORIGIN)

        self.play(Write(matrix))
        self.wait(2)

        # m_label = Tex(r"m").scale(0.8)
        # n_label = Tex(r"n").scale(0.8)

 # Create the shape label: m x n
        shape_label = Tex(r"m \times n")
        shape_label.scale(0.8)

        # Position it to the bottom right of the matrix
        shape_label.next_to(matrix.get_corner(DOWN + RIGHT), DOWN + RIGHT, buff=0.1)

        # Animate the shape label
        self.play(FadeIn(shape_label))
        self.wait(2)








        # # Positioning
        # m_label.next_to(matrix.get_bottom(), LEFT, buff=0.3).shift(0.3 * DOWN + 1.5 * RIGHT)
        # n_label.next_to(matrix.get_bottom(), RIGHT, buff=0.3).shift(0.3 * DOWN + 1.5 * LEFT)

        # # Display matrix
        # self.play(Write(matrix))
        # self.wait(0.5)

        # # Animate m, then n
        # self.play(FadeIn(m_label))
        # self.wait(0.3)
        # self.play(FadeIn(n_label))
        # self.wait(2)



