# manim -pql manim.py SquareToSineWave

from manim_cli import *
import numpy as np

class SquareToSineWave(Scene):
    def construct(self):
        # Step 1: Create a Square
        square = Square(side_length=4, color=BLUE)
        self.play(Create(square))
        self.wait(1)

        # Step 2: Transform Square to Circle
        circle = Circle(radius=2, color=GREEN)
        self.play(Transform(square, circle))
        self.wait(1)

        # Step 3: Morph Circle to Sine Wave
        def circle_to_sine_wave(point):
            """
            This function maps a point from the circle to a sine wave.
            Assumes the circle is centered at origin.
            """
            x, y, z = point
            # Convert polar angle (θ) from the circle to map it linearly to x
            r = np.sqrt(x**2 + y**2)
            if r == 0:
                return np.array([0, 0, 0])
            theta = np.arctan2(y, x)
            # Normalize θ from [-π, π] to [0, 1]
            t = (theta + PI) / (2 * PI)
            # Map to sine wave
            sine_x = interpolate(-3, 3, t)   # from -3 to 3 units
            sine_y = 1.5 * np.sin(2 * PI * t)
            return np.array([sine_x, sine_y, 0])

        sine_wave = always_redraw(lambda: square.copy().apply_function(circle_to_sine_wave))

        self.play(Transform(square, sine_wave), run_time=3)
        self.wait(2)
