video="02_Radiation_Basics_03_D4.mp4"

from manim_code.m02_radBas_03 import *

if __name__ == "__main__":
    from manim import config
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 30
    config.output_file = video
    config.preview = True

    scene = Title()
    scene.render()