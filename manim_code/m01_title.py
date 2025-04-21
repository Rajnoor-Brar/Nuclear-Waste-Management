from manim import *
import numpy as np


class Title(Scene):
    def construct(self):
        # Custom colors
        CUSTOM_SVG_COLOR = rgb_to_color([0.0, 0.4, 0.9])     # Cyan-like
        CUSTOM_GLOW_COLOR = rgb_to_color([0.0, 0.4, 0.8])    # Bright cyan-blue

        # Load SVG warning sign and control size/position
        svg = SVGMobject("images/radioactive.svg")
        svg.set_color(CUSTOM_SVG_COLOR)
        svg.set_fill(CUSTOM_SVG_COLOR, opacity=0.9)
        svg.set_stroke(CUSTOM_SVG_COLOR, width=3)
        svg.scale(0.5)
        svg.move_to([0, -2.7, 0])  # Custom position (x, y, z)

        # Group for glow + svg
        glow_group = VGroup()

        # Glow layer
        glow = svg.copy()
        glow.set_color(CUSTOM_GLOW_COLOR)
        glow.set_fill(CUSTOM_GLOW_COLOR, opacity=0.3)
        glow.set_stroke(CUSTOM_GLOW_COLOR, width=5, opacity=0.6)
        glow.scale(1.02)
        glow_group.add(glow)

        # Add layered glow effect
        for i in range(3):
            layer = svg.copy()
            layer.set_color(CUSTOM_GLOW_COLOR)
            layer.set_stroke(CUSTOM_GLOW_COLOR, width=4 + 3 * i, opacity=0.1)
            layer.set_fill(opacity=0)
            layer.scale(1.02 + 0.01 * i)
            glow_group.add(layer)

        # Add the main SVG on top
        glow_group.add(svg)

        # Time tracker to simulate scene time
        time_tracker = ValueTracker(0)

        # Update function for glow
        def update_glow(mob):
            t = time_tracker.get_value()
            opacity = 0.2 + 0.2 * np.sin(2 * PI * t)
            for g in glow_group[:-1]:  # Apply to all glow layers
                g.set_fill(CUSTOM_GLOW_COLOR, opacity=opacity)
                g.set_stroke(CUSTOM_GLOW_COLOR, opacity=opacity)

        glow_group.add_updater(update_glow)

        self.add(glow_group)

        # Animate the time tracker only for first 5 seconds
        self.play(
            time_tracker.animate.increment_value(3),
            run_time=3, rate_func=linear
        )

        glow_group.remove_updater(update_glow)

        # Keep glowing after 5 seconds
        glow_group.add_updater(update_glow)

        # Add glowing text after 5 seconds with custom font
        title_text = Text("Nuclear Waste Management", font_size=56, font="Edu AU VIC WA NT Pre")
        title_text.set_color(WHITE)
        title_text.move_to([0, 0, 0])
        title_text.set_opacity(0)

        def update_text(mob, alpha):
            t = alpha * 5  # same domain as time_tracker
            opacity = min(1.0, t * 0.2) * (0.8 + 0.2 * np.sin(4 * PI * t))
            mob.set_opacity(opacity)

        self.play(
            UpdateFromAlphaFunc(title_text, update_text),time_tracker.animate.increment_value(3),
            run_time=5, rate_func=linear
        )

        self.add(title_text)
        glow_group.remove_updater(update_glow)


if __name__ == "__main__":
    from manim import config
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 30
    config.output_file = "01_D5_Title.mp4"
    config.preview = True

    scene = Title()
    scene.render()
