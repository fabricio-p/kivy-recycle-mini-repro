from kivy.lang import Builder
from kivy.properties import ColorProperty, VariableListProperty

from .. import colors

Builder.load_string(
"""
<BackgroundColorBehavior>:
  canvas.before:
    Color:
      rgba: self.background_color
    RoundedRectangle:
      pos: self.pos
      size: self.size
      radius: self.border_radius
"""
)

class BackgroundColorBehavior:
    background_color = ColorProperty(colors.transparent)
    border_radius = VariableListProperty(0)
