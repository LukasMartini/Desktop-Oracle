from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
import resources


class ManaSymbols(QWidget):
    def __init__(self, manaCost):
        super(ManaSymbols, self).__init__()
        self.costLayout = QHBoxLayout()

        # TODO: Possible bug catching and general improvements:
        #       - There is likely to be an issue with mana symbols that I forgot to include/how they format infinity in the json.
        #       - Fix the spacing on the layout with styling, shouldn't be difficult
        # FIXED - Phyrexian symbols do not work as of this moment (they're replaced by the non-phyrexian counterpart)

        currentPositionInString = 0
        for each in manaCost:
            newLabel = QLabel()
            if currentPositionInString + 1 < len(manaCost) and manaCost[currentPositionInString+1] == '/':
                newLabel.setPixmap(QPixmap(':/resources/' + each + 'P.png'))
                self.costLayout.addWidget(newLabel)
            elif each != '{' and each != '}':
                newLabel.setPixmap(QPixmap(':/resources/' + each + '.png'))
                self.costLayout.addWidget(newLabel)
            currentPositionInString+=1

        self.setLayout(self.costLayout)