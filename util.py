from pathlib import Path

from kivy.lang import Builder

def load_layout(str_file_path: str) -> None:
    file_path = Path(str_file_path).resolve()
    name = file_path.stem
    dir = file_path.parent
    kv_path = dir / f"{name}.kv"
    Builder.load_file(str(kv_path))

def with_alpha(color, alpha):
    return [*color[:3], alpha]
