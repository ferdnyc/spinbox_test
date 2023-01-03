# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from typing import Optional

from PySide6.QtWidgets import QApplication, QDialog, QSpinBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from ui_Dialog import Ui_Dialog

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.spinBox1.valueChanged.connect(lambda v: self.onValueChanged(v, widget=self.ui.spinBox1))
        self.ui.spinBox2.valueChanged.connect(lambda v: self.onValueChanged(v, widget=self.ui.spinBox2))

    def onValueChanged(self, value, /, widget:Optional[QSpinBox]=None):
        do_all = self.ui.checkUpdateAll.isChecked()
        do_block = self.ui.checkBlock.isChecked()

        if not widget:
            return
        if widget is self.ui.spinBox1:
            other_widget = self.ui.spinBox2
        else:
            other_widget = self.ui.spinBox1

        if do_block:
            other_widget.blockSignals(True)
            if do_all:
                widget.blockSignals(True)


        if value > 0:
            other_widget.setMaximum(100 - value)
        if do_all:
            other_v = other_widget.value()
            widget.setMaximum(100 - other_v)

        sb1 = self.ui.spinBox1
        sb2 = self.ui.spinBox2

        self.ui.labelOutput.setText(f"Box Totals: {sb1.value()}/{sb1.maximum()} + {sb2.value()}/{sb2.maximum()}")

        if do_block:
            other_widget.blockSignals(False)
            if do_all:
                widget.blockSignals(False)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Dialog()
    widget.show()
    sys.exit(app.exec())
