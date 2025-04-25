from manimlib import *




class LT(Scene):
    def render_text(self, input_text, max_width=FRAME_WIDTH - 1):
        text = Text(input_text)

        # Scale down text if it's too wide
        if text.get_width() > max_width:
            scale_factor = max_width / text.get_width()
            text.scale(scale_factor)

        # Center the text
        text.move_to(ORIGIN)
        self.play(Write(text))
        self.wait(2)

    def construct(self):
        your_text = """
        Linear Transformations
        """
        self.render_text(your_text)



class SpanDefinition(Scene):
    def construct(self):
        span_tex = Tex(
            R"\text{span}(\vec{v}_1, \vec{v}_2, \dots, \vec{v}_k) = "
            R"\{ a_1 \vec{v}_1 + a_2 \vec{v}_2 + \dots + a_k \vec{v}_k \mid "
            R"a_1, a_2, \dots, a_k \in \mathbb{R} \}"
        )

        # Auto-scale if too wide
        max_width = FRAME_WIDTH - 1
        if span_tex.get_width() > max_width:
            span_tex.scale(max_width / span_tex.get_width())

        # Center and show
        span_tex.move_to(ORIGIN)
        self.play(Write(span_tex))
        self.wait(2)


from manimlib import *

class VectorSpaceDefinition(Scene):
    def construct(self):
        title = Tex(R"\textbf{Definition: Vector Space}")
        title.scale(1.2).to_edge(UP)

        definition_lines = VGroup(
            Tex(R"A vector space consists of:"),
            Tex(R"1. A set V (elements of V are called vectors)"),
            Tex(R"2. A field F (elements of F are called scalars)"),
            Tex(R"3. Two operations:"),
            Tex(R"\quad \bullet Vector addition: v + w \in V for v, w \in V"),
            Tex(R"\quad \bullet Scalar multiplication: cv \in V for c \in F, v \in V"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        definition_lines.next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(*[Write(line) for line in definition_lines])
        self.wait(2)



class LatexTitle(Scene):
    def render_tex(self, input_tex, max_width=FRAME_WIDTH - 1):
        tex = Tex(input_tex)

        # Scale down if the width exceeds max_width
        if tex.get_width() > max_width:
            scale_factor = max_width / tex.get_width()
            tex.scale(scale_factor)

        # Center the tex on screen
        tex.move_to(ORIGIN)
        self.play(Write(tex))
        self.wait(2)

    def construct(self):
        your_latex = r"""
        \textbf{Linear Transformations}
        """
        self.render_tex(your_latex)
