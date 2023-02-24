from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel

from manaSymbols import ManaSymbols

class CardInfo(QWidget):
    def __init__(self, name, manaCost, typeLine, oracleText, power, toughness, loyalty):
        super(CardInfo, self).__init__()

        cardLayout = QHBoxLayout()

        self.cardName = QLabel(name)
        self.cardText = QLabel(oracleText)
        self.cmc = ManaSymbols()

        cardLayout.addWidget(self.cardName)
        cardLayout.addWidget(self.cardText)
        cardLayout.addWidget(self.cmc)

        self.setLayout(cardLayout)