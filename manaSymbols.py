from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap
import resources


class ManaSymbols(QWidget):
    def __init__(self, manaCost):
        super(ManaSymbols, self).__init__()
        self.costLayout = QHBoxLayout()
        self.costLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        # TODO: Possible bug catching and general improvements:
        #       - There is likely to be an issue with mana symbols that I forgot to include/how they format infinity in the json.
        # FIXED - Fix the spacing on the layout with styling, shouldn't be difficult
        # FIXED - Phyrexian symbols do not work as of this moment (they're replaced by the non-phyrexian counterpart)
        for each in manaCost.split('{')[1::]: # Loops through mana cost string split by {, starting from the second item as the first item is '', caused by { being the first character of any cost string.
            newLabel = QLabel()
            if '/' in each: # Handles Phyrexian mana
                newLabel.setPixmap(QPixmap(':/resources/' + each[0] + 'P.png'))
                self.costLayout.addWidget(newLabel)
            else:
                newLabel.setPixmap(QPixmap(':/resources/' + each[:len(each)-1:] + '.png')) # each[:len(each)-1:] is just indexing until the second last character in the string (1 before the closing })
                self.costLayout.addWidget(newLabel)

        self.setLayout(self.costLayout)