from manimlib import *
import numpy as np






def MathTex(*a,**kw):
    return Tex(*a,**kw)


def Create(*a,**kw):
    return ShowCreation(*a,**kw)



class SpanOfSingleVector(Scene):
    def construct(self):
        axes = Axes()
        self.add(axes)

        
        vector = np.array([2, 1, 0])
        origin = np.array([0, 0, 0])
        
        
        vector_obj = Arrow(start=origin, end=vector, buff=0, color=BLUE)
        vector_label = Tex(r'\vec{v}').next_to(vector_obj.get_end(), UP)

        
        self.play(GrowArrow(vector_obj), Write(vector_label))
        self.wait(1)

        
        scaling_factors = [2, 0.5, -0.5, 1.5, -1.5]

        
        scaled_vectors = []

        for scale_factor in scaling_factors:
            
            scaled_vector = scale_factor * vector

            
            scaled_vector_obj = Arrow(start=origin, end=scaled_vector, buff=0, color=RED if scale_factor > 0 else GREEN)
            scaled_vector_label = Tex(f'{scale_factor}\\vec{{v}}').next_to(scaled_vector_obj.get_end(), UP if scale_factor > 0 else DOWN)

            
            self.play(GrowArrow(scaled_vector_obj), Write(scaled_vector_label))
            self.wait(2)

            
            scaled_vectors.append((scaled_vector_obj, scaled_vector_label))

        
        parallel_line = Line(start=5 * vector / np.linalg.norm(vector), end=-5 * vector / np.linalg.norm(vector), color=YELLOW)
        parallel_text = Tex(r'\text{All scaled vectors are parallel to } \vec{v}').to_edge(UP)

        self.play(ShowCreation(parallel_line), Write(parallel_text))
        self.wait(2)


class SpanOfTwoVectors(Scene):
    def construct(self):
        # Create coordinate axes
        # axes = Axes(x_range=[-6, 6, 1], y_range=[-4, 4, 1], axis_config={"include_numbers": True})
        axes = Axes()
        self.add(axes)

        # Define two linearly independent vectors in R^2
        v1 = np.array([1, 0, 0])
        v2 = np.array([0, 1, 0])
        origin = np.array([0, 0, 0])

        # Draw the base vectors
        arrow_v1 = Arrow(start=origin, end=v1, buff=0, color=BLUE)
        arrow_v2 = Arrow(start=origin, end=v2, buff=0, color=GREEN)
        label_v1 = Tex(r"\vec{v}_1").next_to(arrow_v1.get_end(), UP)
        label_v2 = Tex(r"\vec{v}_2").next_to(arrow_v2.get_end(), UP)

        self.play(GrowArrow(arrow_v1), Write(label_v1))
        self.play(GrowArrow(arrow_v2), Write(label_v2))
        self.wait(1)

        # Show combinations (a*v1 + b*v2)
        coefficients = range(-3, 4)
        vector_field = VGroup()

        for a in coefficients:
            for b in coefficients:
                combo = a * v1 + b * v2
                if np.allclose(combo, origin):  # skip origin arrow
                    continue
                arrow = Arrow(start=origin, end=combo, buff=0, color=RED, stroke_width=2)
                vector_field.add(arrow)

        # Animate all arrows appearing to fill the plane
        self.play(LaggedStartMap(GrowArrow, vector_field, lag_ratio=0.05))
        self.wait(1)

        span_text = Tex(r"\text{Span}(\vec{v}_1, \vec{v}_2) = \mathbb{R}^2").to_edge(UP)
        self.play(Write(span_text))
        self.wait(2)



class BasisVector(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes()
        self.add(axes)

        # Define the transformation matrix A
        A = np.array([
            [2, 1],
            [1, 2]
        ])

        # Show matrix A on screen
        matrix_tex = Matrix(A)
        matrix_label = TexText("Matrix A =").next_to(matrix_tex, LEFT)
        matrix_group = VGroup(matrix_label, matrix_tex)
        matrix_group.to_corner(UL)
        self.play(Write(matrix_group))

        # Draw standard basis vectors
        i_hat = Vector([1, 0], color=BLUE)
        j_hat = Vector([0, 1], color=GREEN)

        i_label = Text("î", font_size=24).next_to(i_hat.get_end(), DOWN)
        j_label = Text("ĵ", font_size=24).next_to(j_hat.get_end(), LEFT)

        self.play(GrowArrow(i_hat), Write(i_label))
        self.play(GrowArrow(j_hat), Write(j_label))
        self.wait(1)

        # Draw the transformed vectors (columns of matrix A)
        col1 = Vector(A[:, 0], color=YELLOW)
        col2 = Vector(A[:, 1], color=ORANGE)

        col1_label = Text("A·î", font_size=24).next_to(col1.get_end(), RIGHT)
        col2_label = Text("A·ĵ", font_size=24).next_to(col2.get_end(), UP)

        self.play(Transform(i_hat, col1), Transform(i_label, col1_label))
        self.play(Transform(j_hat, col2), Transform(j_label, col2_label))

        self.wait(2)


