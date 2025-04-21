from manim import *
import numpy as np
import random

class Title(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        t = ValueTracker(0)
        t.add_updater(lambda m, dt: m.increment_value(dt))
        self.add(t)

        # 1) Parent nucleus: 12 protons + 13 neutrons randomly scattered
        spread_radius = 0.3  # control how spread out the nucleus is
        nucleus_parent = self.make_random_nucleus(num_protons=12, num_neutrons=13, spread=spread_radius)

        # 2) Electrons: 8 orbiting in a circle
        electron_radius = 1.8
        electrons = VGroup(*[
            Dot(radius=0.06, color=BLUE).move_to(
                ORIGIN + np.array([np.cos(theta) * electron_radius, np.sin(theta) * electron_radius, 0])
            )
            for theta in np.linspace(0, TAU, 8, endpoint=False)
        ])
        electrons.add_updater(lambda mob, dt: mob.rotate_about_origin(PI * dt*1.3))  # spin orbit

        # 3) Nucleus pulsation to show instability
        def pulse_nucleus(mob, dt):
            ω = 1.5  # Hz
            A = 0.04
            scale = 1 + A * np.sin(2 * PI * ω * t.get_value())
            mob.scale_to_fit_width(nucleus_parent.width * scale)
        nucleus_parent.add_updater(pulse_nucleus)

        # 4) Add to scene
        self.add(nucleus_parent, electrons)
        self.wait(3)

        # 5) Emit α-particle (2 protons + 2 neutrons)
        alpha = self.make_random_nucleus(num_protons=2, num_neutrons=2, spread=spread_radius * 0.55).move_to(ORIGIN)
        nucleus_daughter = self.make_random_nucleus(num_protons=10, num_neutrons=11, spread=spread_radius * 0.9)
        self.add(alpha)
        self.play(
            alpha.animate.shift(RIGHT * 4 + UP * 2).scale(1.5).fade(0),
            Transform(nucleus_parent, nucleus_daughter),
            run_time=2
        )
        self.wait(2)

    def make_random_nucleus(self, num_protons, num_neutrons, spread=0.8):
        particles = []

        for _ in range(num_protons):
            x, y = self.random_in_disk(spread)
            particles.append(Dot(point=[x,y,0], radius=0.12) \
    .set_fill(RED, opacity=1) \
    .set_stroke(BLACK, width=2))

        for _ in range(num_neutrons):
            x, y = self.random_in_disk(spread)
            particles.append(Dot(point=[x,y,0], radius=0.12) \
    .set_fill(BLUE, opacity=1) \
    .set_stroke(BLACK, width=2))

        return VGroup(*particles)

    def random_in_disk(self, radius):
        r = radius * np.sqrt(random.random())  # uniform distribution over area
        theta = random.uniform(0, 2 * np.pi)
        return r * np.cos(theta), r * np.sin(theta)
