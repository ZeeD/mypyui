from sys import argv
from typing import List
from typing import Optional

from movs import read_txt
from movs.model import Row

from .tabui import main_window


def loader(path: str) -> List[Row]:
    _, data = read_txt(path)
    return list(data)


def main() -> None:
    accumulator: Optional[str]
    try:
        _, accumulator = argv
    except ValueError:
        accumulator = None

    with main_window(loader, accumulator) as window:
        window.show()
