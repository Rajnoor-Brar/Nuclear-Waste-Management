from manim import *
import random

# === Editable Parameters ===
core_duration = 3          # Duration for reactor core scene
towers_duration = 3.5      # Duration for steam animation
glow_pulse_rate = 0.4      # Base glow flicker interval
fade_time = 0.5            # Fade-in/fade-out transition

# === Scene ===
class NuclearSequence(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # === 1. Glowing Reactor Core ===
        reactor = SVGMobject("images/Reactor_Core_BOR.svg")
        reactor.set(width=4)
        reactor.move_to(ORIGIN)

        glow = Circle(radius=2, color=YELLOW, fill_opacity=0.3).move_to(reactor)
        glow.set_stroke(width=0)

        self.play(FadeIn(reactor), FadeIn(glow), run_time=fade_time)

        # Flickering glow using randomized pulse timing
                # Flickering glow using randomized pulse timing and transparency
        glow_time = 0
        while glow_time < core_duration - fade_time:
            flicker_scale = random.uniform(1.15, 1.35)
            flicker_opacity = random.uniform(0.4, 0.9)
            flicker_rate = random.uniform(glow_pulse_rate * 0.5, glow_pulse_rate * 1.5)

            self.play(
                AnimationGroup(
                    Indicate(glow, scale_factor=flicker_scale, color=YELLOW, rate_func=there_and_back),
                    glow.animate.set(fill_opacity=flicker_opacity),
                    lag_ratio=0
                ),
                run_time=flicker_rate
            )

            glow_time += flicker_rate


        self.wait(0.1)
        self.play(FadeOut(reactor), FadeOut(glow), run_time=fade_time)

        # === 2. Cooling Towers ===
        towers = SVGMobject("images/power_plant.svg")
        towers.set(width=6)
        towers.move_to(DOWN)

        self.play(FadeIn(towers), run_time=fade_time)

        # Create steam bubbles (dots) in batches
        bubble_groups = []
        total_bubbles = 15
        bubbles_per_group = 5
        for _ in range(0, total_bubbles, bubbles_per_group):
            group = VGroup(*[
                Dot(radius=0.1, color=WHITE).shift(DOWN * 0.5 + RIGHT * random.uniform(-1.5, 1.5))
                for _ in range(bubbles_per_group)
            ])
            bubble_groups.append(group)

        # Animate bubbles in bunches to random heights
        for group in bubble_groups:
            for dot in group:
                self.add(dot)
            self.play(
                AnimationGroup(*[
                    dot.animate.shift(UP * random.uniform(1.5, 3)).fade(1)
                    for dot in group
                ], lag_ratio=0.1),
                run_time=towers_duration
            )
            for dot in group:
                self.remove(dot)

        self.wait(0.3)
        self.play(FadeOut(towers), run_time=fade_time)
