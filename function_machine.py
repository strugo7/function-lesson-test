from manim import *

NAVY   = "#0B1220"
CANVAS = "#1A2540"
BLUE   = "#3B9EFF"
AMBER  = "#FFC94D"
TEXTC  = "#E2E8F0"
MUTED  = "#94A3B8"

HEB = "Noto Sans Hebrew"

config.background_color = NAVY


class FunctionMachine(Scene):
    def construct(self):
        self.camera.background_color = NAVY

        # ---------- המכונה ----------
        box = RoundedRectangle(
            corner_radius=0.25, width=2.6, height=1.3,
            color=BLUE, fill_color=CANVAS, fill_opacity=1, stroke_width=3,
        )
        label = Text("x²", font=HEB, font_size=40, color=BLUE, weight=BOLD)
        label.move_to(box)
        machine = VGroup(box, label)

        self.play(FadeIn(machine, scale=0.85), run_time=0.6)
        self.wait(0.2)

        def run_pair(x_val, y_val):
            x_txt = Text(str(x_val), font=HEB, font_size=44, color=TEXTC)
            x_txt.move_to(LEFT * 4.2)
            self.play(FadeIn(x_txt, shift=RIGHT * 0.3), run_time=0.32)
            self.play(x_txt.animate.move_to(box.get_left() + LEFT * 0.25), run_time=0.45)
            self.play(FadeOut(x_txt, scale=0.3), Flash(box.get_center(), color=BLUE, flash_radius=1.0), run_time=0.3)

            y_txt = Text(str(y_val), font=HEB, font_size=44, color=AMBER)
            y_txt.move_to(box.get_right() + RIGHT * 0.25)
            self.play(FadeIn(y_txt, scale=1.3), run_time=0.25)
            self.play(y_txt.animate.move_to(RIGHT * 4.2), run_time=0.45)
            self.play(FadeOut(y_txt), run_time=0.25)

        run_pair(2, 4)
        run_pair(3, 9)
        run_pair(-2, 4)

        rule = Text("כל קלט מקבל בדיוק פלט אחד", font=HEB, font_size=30, color=TEXTC)
        rule.next_to(machine, DOWN, buff=0.8)
        self.play(FadeIn(rule, shift=UP * 0.2), run_time=0.55)
        self.wait(0.8)
        self.play(FadeOut(rule), FadeOut(machine), run_time=0.55)

        # ---------- בונים את הגרף מהנקודות ----------
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-1, 9.5, 2],
            x_length=6, y_length=4.2,
            axis_config={"color": MUTED, "stroke_width": 2},
        )
        self.play(Create(axes), run_time=0.55)

        xs = [-2.8, -2.4, -2, -1.6, -1.2, -0.8, -0.4, 0, 0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8]
        dots = VGroup()
        curve_pts = []
        for xv in xs:
            yv = xv * xv
            p = axes.coords_to_point(xv, yv)
            curve_pts.append(p)
            dots.add(Dot(p, radius=0.045, color=AMBER))

        self.play(LaggedStart(*[FadeIn(d, scale=0.3) for d in dots], lag_ratio=0.06), run_time=1.5)

        parabola = VMobject(color=BLUE, stroke_width=4)
        parabola.set_points_smoothly(curve_pts)
        self.play(Create(parabola), run_time=0.9)
        self.wait(0.5)

        tag = Text("MathNext", font=HEB, font_size=26, color=MUTED)
        tag.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(tag), run_time=0.45)
        self.wait(0.7)
        self.play(FadeOut(VGroup(axes, dots, parabola, tag)), run_time=0.5)
