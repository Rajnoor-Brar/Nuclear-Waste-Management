from manim import *

class Title(Scene):
    def construct(self):
        zoom_time = 2
        hold_time = 1.5

        # Load images/SVGs for each scale (must be pre-prepared)
        hand = ImageMobject("images/hand.jpg").scale(1.5)
        skin = ImageMobject("images/skin_surface.jpg").scale(3)
        cells = ImageMobject("images/cell.svg").scale(4)
        molecules = ImageMobject("images/molecules.svg").scale(5)
        atoms = ImageMobject("images/atoms.svg").scale(6)

        # Start from hand
        self.play(FadeIn(hand))
        self.wait(hold_time)

        # Zoom to skin
        self.play(Transform(hand, skin), run_time=zoom_time)
        self.wait(hold_time)

        # Zoom to cells
        self.play(Transform(hand, cells), run_time=zoom_time)
        self.wait(hold_time)

        # Zoom to molecules
        self.play(Transform(hand, molecules), run_time=zoom_time)
        self.wait(hold_time)

        # Zoom to atoms
        self.play(Transform(hand, atoms), run_time=zoom_time)
        self.wait(hold_time)

        self.play(FadeOut(hand))
