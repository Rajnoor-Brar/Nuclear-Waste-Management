from manim import *

class Title(Scene):
    def construct(self):
        self.camera.background_color = WHITE  # White background

        # Load SVGs and set color for visibility
        hand = SVGMobject("images/hand.svg").scale(2)
        hand.z_index = 4
        cell = SVGMobject("images/cell.svg").scale(2)
        cell.z_index = 3
        molecules = SVGMobject("images/molecules.svg").scale(2)
        molecules.z_index = 2
        atoms = SVGMobject("images/atoms.svg").scale(2)
        atoms.z_index = 1

        # Function to handle transition between stages
        def transition(current, next_obj):
            
            next_obj.scale(0.1).move_to(ORIGIN)
            self.add(next_obj.set_opacity(0))

            self.play(
                current.animate.scale(20).set_opacity(0),
                next_obj.animate.scale(20).set_opacity(1),
                run_time=1
            )

            self.remove(current)

        transition(hand, cell)
        self.wait(0.5)
        transition(cell, molecules)
        self.wait(0.5)
        transition(molecules, atoms)
        self.wait(0.5)
