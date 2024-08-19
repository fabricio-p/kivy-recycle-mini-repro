from kivy.lang import Builder
from kivy.properties import ColorProperty, VariableListProperty, NumericProperty

from .. import colors

Builder.load_string(
"""
<BorderBehavior>:
  canvas.after:
    Color:
      rgba: self.border_color
    Line:
      width: self.border_width
      rounded_rectangle: [*self.pos, *self.size, *self.border_radius]
"""
)

class BorderBehavior:
    border_color = ColorProperty(colors.transparent)
    border_width = NumericProperty(1)
    border_radius = VariableListProperty(0)
