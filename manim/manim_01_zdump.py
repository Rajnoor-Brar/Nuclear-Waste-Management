        # Background image
        background = ImageMobject("images/godzilla.jpg")
        background.scale_to_fit_height(config.frame_height)
        background.scale_to_fit_width(config.frame_width)

        # Dark overlay to make background very dark
        overlay = Rectangle(
            width=config.frame_width, height=config.frame_height,
            fill_color=BLACK, fill_opacity=0.4
        )

        self.add(background, overlay)