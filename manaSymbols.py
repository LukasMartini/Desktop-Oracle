from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
import resources


class ManaSymbols(QWidget):
    def __init__(self):
        super(ManaSymbols, self).__init__()
        self.costLayout = QHBoxLayout()

        self.u = QPixmap(':/resources/u.png') # NOTE: while the vars are named after the first letter of the respective colour, blue uses "u" to differentiate from black.

        self.cost = QLabel()
        self.cost.setPixmap(self.u)
        self.costLayout.addWidget(self.cost)

        self.setLayout(self.costLayout)