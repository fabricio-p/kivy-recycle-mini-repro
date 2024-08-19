from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import (
    ColorProperty,
    NumericProperty,
    ListProperty,
    BooleanProperty)
from kivy.uix.behaviors import ButtonBehavior

from .. import colors
from ..behaviors import *

Builder.load_string(
"""
<MGridLayout>:
  size_hint: None, None
  size: self.minimum_size
  background_color: app.color.all.transparent
  border_color: app.color.all.transparent
  border_width: 1
  border_radius: 0

<MLabel>:
  size_hint: None, None
  size: self.texture_size
  color: app.color.fg.normal.prim

<BoxButton>:
  background_color: app.color.all.transparent
  size_hint: None, None
  size: self.minimum_size

<GridButton>:
  -size_hint: 1, None
  rows: 1
  orientation: "lr-tb"
"""
)

class MLabel(Label):
    pass

class MGridLayout(BackgroundColorBehavior, BorderBehavior, GridLayout):
    pass

class GridButton(ButtonBehavior, MGridLayout):
    pass

class MBoxLayout(BorderBehavior, BoxLayout):
    pass

class BoxButton(
    BackgroundColorBehavior,
    BorderBehavior,
    ButtonBehavior,
    BoxLayout
):
    pass

class IfBox(BackgroundColorBehavior, BorderBehavior, BoxLayout):
    cond = BooleanProperty(True)

    _ws = ListProperty([None, None])

    def on_kv_post(self, *_args) -> None:
        def on_cond(self, *_args) -> None:
            w = self._ws[0] if self.cond else self._ws[1]
            super(IfBox, self).clear_widgets()
            super(IfBox, self).add_widget(w)
        assert self._ws[0] is not None and self._ws[1] is not None
        self.bind(cond=on_cond)
        on_cond(self)

    def add_widget(self, widget: Widget) -> None:
        if self._ws[0] is None:
            self._ws[0] = widget
        elif self._ws[1] is None:
            self._ws[1] = widget
        else:
            raise ValueError("`IfBox` accepts only 2 widgets and no more")
