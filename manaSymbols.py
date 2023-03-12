from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
import resources


class ManaSymbols(QWidget):
    def __init__(self):
        super(ManaSymbols, self).__init__()
        self.costLayout = QHBoxLayout()

        W = QPixmap(':/resources/W.png')
        U = QPixmap(':/resources/U.png') # NOTE: while the vars are named after the first letter of the respective colour, blue uses "u" to differentiate from black.
        B = QPixmap(':/resources/B.png')
        R = QPixmap(':/resources/R.png')
        G = QPixmap(':/resources/G.png')

        # TODO: general strat will be to parse the mana cost and add the resource file w/ string concating.

        self.cost = QLabel()
        self.cost.setPixmap(U)
        self.costLayout.addWidget(self.cost)

        self.setLayout(self.costLayout)