from manimlib import * 



def MathTex(*a,**kw):
    return Tex(*a,**kw)


def Create(*a,**kw):
    return ShowCreation(*a,**kw)




class SpanOfSingleVector(Scene):
    def construct(self):
        axes = Axes()
        self.add(axes)

        v = np.array([2, 1, 0])
        origin = np.array([0, 0, 0])
        arrow = Arrow(start=origin, end=v, buff=0, color=BLUE)
        label = Tex(r"\vec{v}").next_to(arrow.get_end(), UP)

        self.play(GrowArrow(arrow), Write(label))
        self.wait(1)

        scaling_factors = [2, 0.5, -0.5, -1.5, 1.5]

        for scale in scaling_factors:
            scaled_vec = scale * v
            arrow_scaled = Arrow(start=origin, end=scaled_vec, buff=0, color=RED)
            label_scaled = Tex(f"{scale}\\vec{{v}}").next_to(arrow_scaled.get_end(), UP)
            self.play(GrowArrow(arrow_scaled), Write(label_scaled))
            self.wait(0.5)

        line = Line(start=5*v/np.linalg.norm(v), end=-5*v/np.linalg.norm(v), color=YELLOW)
        text = Tex(r"\text{Span}(\vec{v}) \text{ is a line}").to_edge(UP)
        self.play(ShowCreation(line), Write(text))
        self.wait(2)










class VectorAddition(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes()
        self.add(axes)

        # Define the vectors
        vector_1 = np.array([3, 0, 0])
        vector_2 = np.array([-3, 1, 0])
        origin = np.array([0, 0, 0])

        # Create arrows for the vectors
        vector_1_arrow = Arrow(start=origin, end=vector_1, buff=0, color=BLUE)
        vector_2_arrow = Arrow(start=origin, end=vector_2, buff=0, color=GREEN)

        # Create labels for the vectors
        vector_1_label = MathTex(r'\vec{v}_1').next_to(vector_1_arrow.get_end(), DOWN)
        vector_2_label = MathTex(r'\vec{v}_2').next_to(vector_2_arrow.get_end(), RIGHT)

        # Display vectors and their labels
        self.play(GrowArrow(vector_1_arrow), Write(vector_1_label))
        self.play(GrowArrow(vector_2_arrow), Write(vector_2_label))

        # Display the vectors as column matrices
        vector_1_matrix = Matrix([[3], [0]]).scale(0.5)
        vector_1_matrix.next_to(vector_1_label, DOWN)

        vector_2_matrix = Matrix([[-3], [1]]).scale(0.5)
        vector_2_matrix.next_to(vector_2_label, RIGHT)

        self.play(Write(vector_1_matrix))
        self.play(Write(vector_2_matrix))

        # Translate the second vector to start at the end of the first vector
        vector_2_arrow_new = Arrow(start=vector_1, end=vector_1 + vector_2, buff=0, color=GREEN)
        vector_2_label_new = MathTex(r'\vec{v}_2').next_to(vector_2_arrow_new.get_end(), RIGHT)

        self.play(Transform(vector_2_arrow, vector_2_arrow_new), Transform(vector_2_label, vector_2_label_new))

        # Compute the sum vector
        sum_vector = vector_1 + vector_2

        # Create an arrow for the sum vector
        sum_vector_arrow = Arrow(start=origin, end=sum_vector, buff=0, color=ORANGE)

        # Create a label for the sum vector
        sum_vector_label = MathTex(r'\vec{v}_1 + \vec{v}_2').next_to(sum_vector_arrow.get_end(), UP)

        # Display the sum vector and its label
        self.play(GrowArrow(sum_vector_arrow), Write(sum_vector_label))

        # Create the triangle representing the vector addition
        triangle = Polygon(origin, vector_1, sum_vector, color=YELLOW, fill_opacity=0.5)

        # Display the triangle
        self.play(ShowCreation(triangle))

        # Display the matrices
        sum_vector_matrix = Matrix([[0], [1]]).scale(0.5)
        sum_vector_matrix.next_to(sum_vector_label, RIGHT)
        self.play(Write(sum_vector_matrix))


        
class Vectorki(Scene):
    def construct(self):
        # Define basis vectors
        basis_vector_1 = np.array([1, 1, 0])
        # basis_vector_2 = np.array([0, 1, 0])
        origin = np.array([0, 0, 0])

        # Create arrows for basis vectors
        basis_vector_1_arrow = Arrow(start=origin, end=basis_vector_1, buff=0, color=BLUE)
        # basis_vector_2_arrow = Arrow(start=origin, end=basis_vector_2, buff=0, color=GREEN)

        # Add labels for basis vectors
        basis_vector_1_label = Tex(r'\hat{i}').next_to(basis_vector_1_arrow.get_end(), UP)
        # basis_vector_2_label = Tex(r'\hat{j}').next_to(basis_vector_2_arrow.get_end(), RIGHT)

        # Add basis vectors and labels to the scene
        self.play(GrowArrow(basis_vector_1_arrow), Write(basis_vector_1_label))
        # self.play(GrowArrow(basis_vector_2_arrow), Write(basis_vector_2_label))
        self.wait(1)

        # Create a grid
        grid = NumberPlane()

        # Add grid to the scene
        self.play(ShowCreation(grid))
        self.wait(1)








class LinearCombinationOfiAndj(Scene):
  

    def construct(self):
            
        axes = Axes()
        self.add(axes)

        grid = NumberPlane()
        self.add(grid)

        i_hat = np.array([1, 0, 0])
        j_hat = np.array([0, 1, 0])
        origin = np.array([0, 0, 0])

        # mat = np.c_([i_hat,j_hat,origin])
        
        
        i_vector = Arrow(start=origin, end=i_hat, buff=0, color=BLUE)
        j_vector = Arrow(start=origin, end=j_hat, buff=0, color=GREEN)
        i_label = Tex(r'\hat{i}').next_to(i_vector.get_end(), UP)
        j_label = Tex(r'\hat{j}').next_to(j_vector.get_end(), RIGHT)
        # i_label = Tex(r'\vec{v}_1').next_to(i_vector.get_end(), UP)
        # j_label = Tex(r'\vec{v}_2').next_to(j_vector.get_end(), RIGHT)

        self.play(ShowCreation(axes))
        self.play(GrowArrow(i_vector), Write(i_label))
        self.play(GrowArrow(j_vector), Write(j_label))
        self.wait(1)

        
        random_vector = np.array([-1,-3, 0])
        point_dot = Dot(point=random_vector, color=RED)

        
        random_vector_obj = Arrow(start=origin, end=random_vector, buff=0, color=RED)
        random_vector_label = Tex(r'\vec{v}').next_to(random_vector_obj.get_end(), UP)

        
        # self.play(GrowArrow(random_vector_obj), Write(random_vector_label))
        self.play(GrowFromCenter(point_dot))

        self.wait(1)

        
        a, b = random_vector[0], random_vector[1]

        
        combination_vector_i = a * i_hat
        combination_vector_j = b * j_hat

        
        combination_vector_i_obj = Arrow(start=origin, end=combination_vector_i, buff=0, color=BLUE)
        combination_vector_j_obj = Arrow(start=origin, end=combination_vector_j, buff=0, color=GREEN)
        # combination_vector_i_label = Tex(f'{a}\\vec{{v_1}}').next_to(combination_vector_i_obj.get_end(), UP)
        # combination_vector_j_label = Tex(f'{b}\\vec{{v_2}}').next_to(combination_vector_j_obj.get_end(), RIGHT)
        combination_vector_i_label = Tex(f'{a}\\vec{{i}}').next_to(combination_vector_i_obj.get_end(), UP)
        combination_vector_j_label = Tex(f'{b}\\vec{{j}}').next_to(combination_vector_j_obj.get_end(), RIGHT)

        
        self.play(GrowArrow(combination_vector_i_obj), Write(combination_vector_i_label))
        self.play(GrowArrow(combination_vector_j_obj), Write(combination_vector_j_label))
        self.wait(1)

        
        sum_vector = combination_vector_i + combination_vector_j

        
        sum_vector_obj = Arrow(start=origin, end=sum_vector, buff=0, color=RED)
        sum_vector_label = Tex(r'\vec{v}').next_to(sum_vector_obj.get_end(), UP)

        
        self.play(GrowArrow(sum_vector_obj), Write(sum_vector_label))
        self.wait(1)

        
           
        triangle = Polygon(origin, combination_vector_i, sum_vector, color=YELLOW, fill_opacity=0.5)

        
        self.play(ShowCreation(triangle))
        self.wait(1)



class TriangularLaw(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes()
        self.add(axes)

        # Define the vectors
        vector_1 = np.array([3, 0, 0])
        v1 = np.array(vector_1[:2]).reshape(-1,2).T
        vector_2 = np.array([-3, 1, 0])
        v2 = np.array(vector_2[:2]).reshape(-1,2).T
        origin = np.array([0, 0, 0])

        # Create arrows for the vectors
        vector_1_arrow = Arrow(start=origin, end=vector_1, buff=0, color=BLUE)
        vector_2_arrow = Arrow(start=origin, end=vector_2, buff=0, color=GREEN)

        # Create labels for the vectors
        vector_1_label = MathTex(r'\vec{v}_1').next_to(vector_1_arrow.get_end(), UP)
        vector_2_label = MathTex(r'\vec{v}_2').next_to(vector_2_arrow.get_end(), RIGHT)

        # Display vectors and their labels
        self.play(GrowArrow(vector_1_arrow), Write(vector_1_label))
        self.play(GrowArrow(vector_2_arrow), Write(vector_2_label))
        self.wait(1)

        # Display the vectors as column matrices
        # vector_1_matrix = Matrix([[3], [0]]).scale(0.5)
        vector_1_matrix = Matrix(v1).scale(0.5)
        vector_1_matrix.next_to(vector_1_label, DOWN)

        vector_2_matrix = Matrix(v2).scale(0.5)
        vector_2_matrix.next_to(vector_2_label, RIGHT)

        self.play(Write(vector_1_matrix))
        self.play(Write(vector_2_matrix))


        # Compute the sum vector
        sum_vector = vector_1 + vector_2

        # Create an arrow for the sum vector
        sum_vector_arrow = Arrow(start=origin, end=sum_vector, buff=0, color=ORANGE)

        # Create a label for the sum vector
        sum_vector_label = MathTex(r'\vec{v}_1 + \vec{v}_2').next_to(sum_vector_arrow.get_end(), UP)

        # Display the sum vector and its label
        self.play(GrowArrow(sum_vector_arrow), Write(sum_vector_label))
        self.wait(1)

        # Create the triangle representing the vector addition
        triangle = Polygon(origin, vector_1, sum_vector, color=YELLOW, fill_opacity=0.5)

        # Display the triangle
        self.play(ShowCreation(triangle))
        self.wait(1)

        # Display the matrices
        sum_vector_matrix = Matrix(v2+v1).scale(0.5)
        sum_vector_matrix.next_to(sum_vector_label, RIGHT)
        self.play(Write(sum_vector_matrix))
        self.wait(2)
