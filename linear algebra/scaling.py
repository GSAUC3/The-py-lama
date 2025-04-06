from manimlib import * 



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
            lambda: MathTex(f'{continuous_scale_factor.get_value():.2f}\\cdot\\vec{{v}}').next_to(
                continuously_scaled_vector.get_end(), UP
            )
        )

        # Create the vector matrix
        vector_matrix = always_redraw(
            lambda: Matrix(
                [[f'{continuous_scale_factor.get_value() :.2f} * { vector[0]:.2f}'],
                 [f'{continuous_scale_factor.get_value() :.2f} * { vector[1]:.2f}']],
               
            ).shift(3* DOWN + 2*RIGHT)
        )
        equal_to = Tex('=').next_to(vector_matrix)
        vector_mat_result = always_redraw(
            lambda: Matrix(
                [[f'{continuous_scale_factor.get_value() * vector[0]:.2f}'],
                 [f'{continuous_scale_factor.get_value() * vector[1]:.2f}']],
               
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
        for scale in [1, 2, -1, -3, -2, -0.5, 0.5, 1]:
            self.play(
                continuous_scale_factor.animate.set_value(scale),
                run_time=5,
                rate_func=linear
            )
            self.wait(1)