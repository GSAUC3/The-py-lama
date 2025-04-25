from manimlib import * 



def MathTex(*a,**kw):
    return Tex(*a,**kw)


def Create(*a,**kw):
    return ShowCreation(*a,**kw)


class Scaling(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes()
        self.add(axes)

        # Define the vector
        vector = np.array([2, 1, 0])
        origin = np.array([0, 0, 0])

        # Create the vector arrow and its label
        vector_arrow = Arrow(start=origin, end=vector, buff=0, color=BLUE)
        vector_label = MathTex(r'\vec{v}').next_to(vector_arrow.get_end(), UP)

        # Initial scale factor
        continuous_scale_factor = ValueTracker(1)

        # Create the continuously scaled vector arrow
        continuously_scaled_vector = always_redraw(
            lambda: Arrow(
                start=origin,
                end=continuous_scale_factor.get_value() * vector,
                buff=0,
                color=BLUE
            )
        )

        # Create the continuously updating label
        continuous_label = always_redraw(
            lambda: MathTex(f'{continuous_scale_factor.get_value():.1f}\\cdot\\vec{{v}}').next_to(
                continuously_scaled_vector.get_end(), UP
            )
        )

        # Create the vector matrix
        vector_matrix = always_redraw(
            lambda: Matrix(
                [[f'{continuous_scale_factor.get_value() :.1f} * { vector[0]:.1f}'],
                 [f'{continuous_scale_factor.get_value() :.1f} * { vector[1]:.1f}']],
               
            ).shift(3* DOWN + 2*RIGHT)
        )
        equal_to = Tex('=').next_to(vector_matrix)
        vector_mat_result = always_redraw(
            lambda: Matrix(
                [[f'{continuous_scale_factor.get_value() * vector[0]:.1f}'],
                 [f'{continuous_scale_factor.get_value() * vector[1]:.1f}']],
               
            ).next_to(equal_to)
        )

        # Add the initial vector and its label
        self.add(vector_arrow, vector_label)

        basis_vector_1_label = Tex(r'\vec{v} =').next_to(vector_matrix.get_left(), LEFT)
        # Animate the creation of the continuously scaled vector and its label
        self.play(ShowCreation(basis_vector_1_label),
            FadeOut(vector_arrow),
            FadeOut(vector_label),
            Create(continuously_scaled_vector),
            Write(continuous_label),
            Write(vector_matrix),
            Write(equal_to) ,
            Write(vector_mat_result)
        )

        # Scale the vector through different values
        for scale in [2,0,  -1.5]:
            self.play(
                continuous_scale_factor.animate.set_value(scale),
                run_time=5,
                rate_func=linear
            )
            self.wait(1)