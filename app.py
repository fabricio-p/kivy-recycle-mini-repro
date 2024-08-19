from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import (
    ObjectProperty,
    ColorProperty,
    VariableListProperty,
    ListProperty,
    NumericProperty,
    StringProperty,
    DictProperty,
    BooleanProperty)
from kivy.utils import QueryDict, rgba
from kivy.event import EventDispatcher

from .behaviors import *
from .components import *
from .util import with_alpha
from . import colors, paths

class ServiceApp(App):
    color = QueryDict(
        all = colors,
        bg = QueryDict(
            normal = QueryDict(
                prim = colors.white,
                sec = colors.white_silver,
                tert = colors.slate_gray
            ),
            active = QueryDict(
                prim = colors.sea,
            ),
            construct = QueryDict(
                prim = colors.green,
            ),
            destroy = QueryDict(
                prim = colors.red,
                sec = with_alpha(colors.red, 0.0),
            ),
            edit = QueryDict(
                prim = colors.orange,
                sec = with_alpha(colors.orange, 0.0),
            ),
            link = QueryDict(
                prim = colors.platinum,
            ),
        ),
        fg = QueryDict(
            normal = QueryDict(
                prim = colors.black,
                sec = colors.charcoal,
                tert = colors.midnight_blue,
            ),
            link = QueryDict(
                prim = colors.oxford_blue,
            ),
        ),
    )

    paths = paths

    def build(self) -> Widget:
        return AppView()

class AppView(MGridLayout):
    tab_manager = ObjectProperty()

    def on_kv_post(self, *_args, **_kwargs) -> None:
        students_tab = StudentsTab()
        self.tab_manager.add_widget(students_tab)

    def _set_tab(self, _, name: str) -> None:
        self.tab_manager.current = name
