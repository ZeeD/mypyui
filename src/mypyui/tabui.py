from contextlib import contextmanager
from typing import Iterator
from typing import List

from movs.model import Row
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow

from .chartview import ChartView
from .viewmodel import SortFilterViewModel

TABUI_UI_PATH = f'{__file__}/../../../resources/tabui.ui'


@contextmanager
def main_window(data: List[Row]) -> Iterator[QMainWindow]:
    app = QApplication([__file__])

    window = QUiLoader().load(TABUI_UI_PATH)

    view_model = SortFilterViewModel(window, data)
    window.tableView.setModel(view_model)
    window.lineEdit.textChanged.connect(view_model.filter_changed)

    window.tab_2.layout().addWidget(ChartView(window, data))

    try:
        yield window
    finally:
        app.exec_()