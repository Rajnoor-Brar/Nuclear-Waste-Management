from manim import *
import numpy as np

class SquareToSineWave(Scene):
    def construct(self):
        square = Square(side_length=4, color=BLUE)
        self.play(Create(square))
        self.wait(1)

        circle = Circle(radius=2, color=GREEN)
        self.play(Transform(square, circle))
        self.wait(1)

        def to_sine(point):
            x, y, z = point
            r = np.sqrt(x**2 + y**2)
            if r == 0:
                return np.array([0, 0, 0])
            theta = np.arctan2(y, x)
            t = (theta + PI) / (2 * PI)
            return np.array([interpolate(-3, 3, t), 1.5 * np.sin(2 * PI * t), 0])

        sine_wave = always_redraw(lambda: circle.copy().apply_function(to_sine))
        self.play(Transform(circle, sine_wave), run_time=3)
        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.pixel_height = 720
    config.pixel_width = 1280
    config.frame_rate = 30
    config.output_file = "square_to_sine.mp4"
    config.preview = True

    scene = SquareToSineWave()
    scene.render()
