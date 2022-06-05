from point import Point, Velocity
"""
This class is in charge of all moving objects on screen.

Attributes:
    _text (string): The text to display
    _font_size (int): The font size to use.
    _color (Color): The color of the text.
    _position (Point): The screen coordinates.
    _velocity (Point): The speed and direction.
    _x (integer): The horizontal distance from the origin.
    _y (integer): The vertical distance from the origin.
"""

class Moving_Object:

    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()

    def draw(self):
        pass