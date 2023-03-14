from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel

from manaSymbols import ManaSymbols

class CardInfo(QWidget):
    def __init__(self, name, manaCost, typeLine, oracleText, power, toughness, loyalty):
        super(CardInfo, self).__init__()

        cardLayout = QHBoxLayout()

        reformat = oracleText.split('\n')
        formattedText = []
        for each in reformat:
            if len(each) <= 50:
                formattedText.append(each)
            else:
                wordCount = 0
                totalCount = 0
                while totalCount < len(each):
                    string = []
                    while wordCount <= 60 and totalCount < len(each):
                        string.append(each[totalCount:each.find(' ', totalCount+1)])
                        totalCount += abs(totalCount - each.find(' ', totalCount+1))
                        wordCount += abs(wordCount - each.find(' ', wordCount+1))
                    string[0] = string[0].lstrip()
                    formattedText.append(''.join(string))
                    wordCount = 0

        self.cardName = QLabel(name)
        self.cardText = QLabel('\n'.join(formattedText))
        self.cmc = ManaSymbols(manaCost)

        cardLayout.addWidget(self.cardName)
        cardLayout.addWidget(self.cardText)
        cardLayout.addWidget(self.cmc)

        self.setLayout(cardLayout)