from manim import *
import numpy as np
import random

class Title(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        time = ValueTracker(0)
        time.add_updater(lambda m, dt: m.increment_value(dt))
        self.add(time)

        layout = [5, 4, 5]  # Number of atoms per row
        spacing_x = 2.5
        spacing_y = 2.5
        center_y = 0

        stable_indices = {0, 2, 6, 7, 9, 11}  # arbitrary stable atoms
        atoms = VGroup()

        index = 0
        for row, count in enumerate(layout):
            y = center_y + (1 - row) * spacing_y  # Top to bottom
            offset_x = -((count - 1) / 2) * spacing_x  # Center the row

            for col in range(count):
                x = offset_x + col * spacing_x
                pos = np.array([x, y, 0])
                is_stable = index in stable_indices
                atom = self.make_atom(pos, is_stable, time)
                atoms.add(atom)
                index += 1

        self.add(atoms)
        self.wait(6)

    def make_atom(self, pos, is_stable, time):
        A_pulse = 0.05
        f_pulse = 2
        shake_amp = 0.05
        flicker_rate = 20

        # Nucleus
        nucleus = Dot(point=pos, radius=0.14, color=BLACK)

        # Circular orbit
        orbit_radius = 1
        orbit = Circle(radius=orbit_radius, color=GRAY, stroke_opacity=0.7)
        orbit.move_to(pos)

        # Electron
        electron = Dot(radius=0.05, color=BLUE)

        # Electron updater: circular motion
        def get_electron_pos(t):
            angle = 2 * PI * t
            x = orbit_radius * np.cos(angle)
            y = orbit_radius * np.sin(angle)
            return pos + np.array([x, y, 0])

        def electron_updater(mob, dt):
            t = time.get_value()
            mob.move_to(get_electron_pos(t * 2.2))

        electron.add_updater(electron_updater)

        # Nucleus animation
        base_radius = nucleus.radius
        base_pos = np.array(pos)

        if is_stable:
            def stable_pulse(mob, dt):
                t = time.get_value()
                scale = 1 + A_pulse * np.sin(2 * PI * f_pulse * t)
                mob.scale_to_fit_width(2 * base_radius * scale)
            nucleus.color = PURPLE
            nucleus.add_updater(stable_pulse)
        else:
            frame_count = [0]
            def unstable_vibrate(mob, dt):
                dx = random.uniform(-shake_amp, shake_amp)
                dy = random.uniform(-shake_amp, shake_amp)
                mob.move_to(base_pos + [dx, dy, 0])
                frame_count[0] += 1
                if frame_count[0] % max(1, int(60/flicker_rate)) == 0:
                    mob.set_opacity(random.uniform(0.3, 1.0))
            nucleus.color = ORANGE
            nucleus.add_updater(unstable_vibrate)

        return VGroup(nucleus, orbit, electron)
