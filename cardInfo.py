from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel

from manaSymbols import ManaSymbols

class CardInfo(QWidget):
    def __init__(self):
        super(CardInfo, self).__init__()

        cardLayout = QHBoxLayout()

        self.cardName = QLabel("Jace, the Mind Sculptor")
        self.cardText = QLabel("A real Piece Of Shit (tm)")
        self.cmc = ManaSymbols()

        cardLayout.addWidget(self.cardName)
        cardLayout.addWidget(self.cardText)
        cardLayout.addWidget(self.cmc)

        self.setLayout(cardLayout)