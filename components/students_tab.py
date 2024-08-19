from typing import Literal, TypedDict, Tuple, List, cast

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.properties import (
    ListProperty,
    NumericProperty,
    StringProperty,
    ObjectProperty,
    AliasProperty)

from ..util import load_layout
from ..behaviors import BackgroundColorBehavior, BorderBehavior
from .common import MGridLayout, MBoxLayout

load_layout(__file__)

class RowDict(TypedDict):
    id: int
    first_name: str
    last_name: str
    klass: str

def _return_true(*_args, **_kwargs) -> Literal[True]:
    return True

def _get_students(self) -> List[RowDict]:
    # placeholder data
    return [
        RowDict(
            id=(i * 10 + j),
            first_name=f"{chr(ord('A') + i)}{chr(ord('A') + j)}",
            last_name=f"{chr(ord('A') + 5 + i)}{chr(ord('A') + 5 + j)}",
            klass=f"{10 + j // 7} {chr(ord('A') + (j % 5))}")
        for i in reversed(range(1, 2))
        for j in reversed(range(1, 10))]

class StudentsTab(Screen):
    students = AliasProperty(_get_students, _return_true)
    table_grid = ObjectProperty()

    def __init__(self, *args, **kwargs) -> None:
        super(StudentsTab, self).__init__(*args, **kwargs)

        def make_table_grid(self, *_args):
            self.table_grid.clear_widgets()
            for s in self.students:
                row = StudentsTableRow()
                for (key, val) in s.items():
                    setattr(row, key, val)
                self.table_grid.add_widget(row)

        self.bind(students=make_table_grid)
        make_table_grid(self)

class StudentsTableRow(MBoxLayout):
    id = NumericProperty()
    first_name = StringProperty()
    last_name = StringProperty()
    klass = StringProperty()

class StudentsRecycleGrid(
    BackgroundColorBehavior,
    BorderBehavior,
    RecycleGridLayout
):
    pass
