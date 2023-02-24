from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QLineEdit, QScrollArea, QLabel

from cardInfo import CardInfo
from parser import Parser

import time

class mw(QMainWindow):
    def __init__(self):
        super(mw, self).__init__()
        mainWindow = QWidget()
        mainLayout = QVBoxLayout()
        self.url = ""
        self.referenceTime = time.time()
        self.parser = Parser()

        # Setup for searchbar widget
        self.searchBar = QLineEdit()
        self.searchBar.setPlaceholderText("Search with card names and text...")
        self.searchBar.textChanged.connect(self.updateSearch)

        # Setup for scroll area and related widgets
        self.cardViewer = QScrollArea()
        self.cardViewer.setWidgetResizable(True)

        self.scroller = QWidget()
        self.scrollLayout = QVBoxLayout()
        self.scroller.setLayout(self.scrollLayout)
        self.cardViewer.setWidget(self.scroller)

        # Add both main widgets to the main layout
        mainLayout.addWidget(self.searchBar)
        mainLayout.addWidget(self.cardViewer)

        # Show GUI
        mainWindow.setLayout(mainLayout)
        self.setCentralWidget(mainWindow)
        self.show()

    def clearScrollLayout(self):
        for item in range(self.scrollLayout.count()):
            card = self.scrollLayout.itemAt(item)
            try:
                card.widget().close()
            except AttributeError:
                pass
            self.scrollLayout.removeItem(card)

    def updateSearch(self, search):
        self.url = search # NOTE: this means that there is a simple in operation to check if the search should come back.
        self.clearScrollLayout()
        checkStart = time.time() # This, along with self.referenceTime, allow for a way to avoid overloading the API while also not causing stutter like time.sleep()
        if checkStart - self.referenceTime > 3:
            results = self.parser.search(self.url)
            for each in results:
                self.scrollLayout.addWidget(CardInfo(each[0], each[1], each[2], each[3], each[4], each[5], each[6], each[7], each[8]))




main = QApplication([])
window = mw()

# TEST CODE: used to ensure that card grabbing works properly.
#parserTest = Parser()
#testCard = parserTest.search("Craterhoof Behemoth")
# cardsToDisplay = []
# for each in testCard:
#     cardsToDisplay.append(CardInfo(each[0], each[1], each[2], each[3], each[4], each[5], each[6], each[7], each[8]))
#
# for each in cardsToDisplay:
#     window.scrollLayout.addWidget(each)
# print(testCard)
#try:
#   card = scrython.cards.Search(q="b")
#   parserTest.cache.clear()
#except Error as e:
#   print("scryfall may be down for maintenance. DO NOT CLEAR CACHE.")
#parserTest.cache.printTable()

main.exec()
window.parser.cache.close()