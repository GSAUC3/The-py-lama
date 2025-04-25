from manimlib import *
import numpy as np 


class LinearTransformation(Scene):
    def construct(self):
        # Coordinate system
        axes = Axes()
        self.add(axes)

        # Add a background grid
        grid = NumberPlane()
        self.add(grid)

        # Define the transformation matrix A
        # A = np.array([
        #     [1, -1],
        #     [1, 1]
        # ])
        A = np.array([
            [2, 1],
            [-1, 1]
        ])

        v = np.array([[1/2],
                      [1/2]])

        # Display matrix
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
        v_vec = Vector(v.squeeze())

        self.play(GrowArrow(i_hat), Write(i_label))
        self.play(GrowArrow(j_hat), Write(j_label))
        self.wait(1)
        self.play(GrowArrow(v_vec))

        # Group basis vectors
        basis_group = VGroup(i_hat, j_hat, i_label, j_label,v_vec)

        # Apply the transformation matrix
        self.play(
            ApplyMatrix(A, grid),
            ApplyMatrix(A, basis_group),
            run_time=3
        )

        self.wait(2)


class LinearTransformation2(Scene):
    def construct(self):
        # Coordinate system
        axes = Axes()
        self.add(axes)

        # Grid
        grid = NumberPlane()
        self.add(grid)

        # Matrix A
        A = np.array([
            [1, -1],
            [1, 1]
        ])

        # Show matrix
        matrix_tex = Matrix(A)
        matrix_label = TexText("Matrix A =").next_to(matrix_tex, LEFT)
        matrix_group = VGroup(matrix_label, matrix_tex)
        matrix_group.to_corner(UL)
        self.play(Write(matrix_group))
        # self.wait(1)

        # Standard basis vectors
        i_hat = Vector([1, 0], color=BLUE)
        j_hat = Vector([0, 1], color=GREEN)
        i_label = Text("î", font_size=24).next_to(i_hat.get_end(), DOWN)
        j_label = Text("ĵ", font_size=24).next_to(j_hat.get_end(), LEFT)

        self.play(GrowArrow(i_hat), Write(i_label))
        self.play(GrowArrow(j_hat), Write(j_label))
        self.wait(3)

        basis_group = VGroup(i_hat, j_hat, i_label, j_label)

        # Apply transformation to grid and basis vectors
        self.play(
            ApplyMatrix(A, grid),
            ApplyMatrix(A, basis_group),
            run_time=3
        )

        self.wait(1)

        a_i_label = Text("A·î", font_size=24).move_to(i_label.get_center())
        a_j_label = Text("A·ĵ", font_size=24).move_to(j_label.get_center())

        # Animate label transformation
        self.play(
            Transform(i_label, a_i_label),
            Transform(j_label, a_j_label)
        )
        # Define new vector v = 2 * A·î + 1 * A·ĵ
        
        V_dash = np.array([1/2, 1/2])

        v = A @ V_dash
        vec_v = Vector(v, color=PURPLE)
        v_label = Text(f"v = {V_dash[0]}·Aî + {V_dash[1]}·Aĵ", font_size=28).next_to(vec_v.get_end(), RIGHT)

        # Show linear combination visually
        step1 = Vector(A[:, 0]*V_dash[0], color=YELLOW)  # 2 * A·î
        step2 = Vector(A[:, 1]*V_dash[1], color=ORANGE).shift(step1.get_end())  # 1 * A·ĵ, starting where step1 ends

        # remove the axes
        self.wait(1)
        # self.play(FadeOut(axes))

        # self.wait(2)

        # label1 = Text(f"{V_dash[0]}·Aî", font_size=24).next_to(step1.get_end(), LEFT)
        self.play(GrowArrow(step1))
        # self.play(Write(label1))

        # label2 = Text(f"{V_dash[1]}·Aĵ", font_size=24).next_to(step2.get_end(), DOWN)
        self.play(GrowArrow(step2))
        # self.play(Write(label2))


        # Final vector is result of both
        self.play(GrowArrow(vec_v), Write(v_label.shift(UP*0.25)))
