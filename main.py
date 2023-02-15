from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QLineEdit, QScrollArea, QLabel

from cardInfo import CardInfo
from parser import Parser

class mw(QMainWindow):
    def __init__(self):
        super(mw, self).__init__()
        mainWindow = QWidget()
        mainLayout = QVBoxLayout()
        self.url = ""

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

        self.scrollLayout.addWidget(CardInfo())

        # Add both main widgets to the main layout
        mainLayout.addWidget(self.searchBar)
        mainLayout.addWidget(self.cardViewer)

        # Show GUI
        mainWindow.setLayout(mainLayout)
        self.setCentralWidget(mainWindow)
        self.show()

    def updateSearch(self, search):
        self.url = search # NOTE: this means that there is a simple in operation to check if the search should come back.
        parserTest.search(self.url)




main = QApplication([])
window = mw()

# TEST CODE: used to ensure that card grabbing works properly.
parserTest = Parser()
parserTest.search("Crater")
parserTest.cache.printTable()
#parserTest.cache.clear()

main.exec()
parserTest.cache.close()