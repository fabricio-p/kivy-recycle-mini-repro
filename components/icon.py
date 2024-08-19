from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.properties import StringProperty

from .. import paths

Builder.load_string(
"""
<Icon>:
  size_hint: None, None
  size: self.texture_size
"""
)

class Icon(Image):
    name = StringProperty()
    ext = StringProperty("png")

    def on_kv_post(self, *_args, **kwargs) -> None:
        self.source = str(
            paths.assets /
            f"{self.name}_{self.size[0]}x{self.size[1]}.{self.ext}")
