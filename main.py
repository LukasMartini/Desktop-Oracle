from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QLineEdit, QScrollArea, QLabel, QPushButton
from PyQt6.QtCore import QTimer

from cardInfo import CardInfo
from parser import Parser


#TODO: MAIN OVERHEAD TODO TO DO BECAUSE IT'S IMPORTANT: please put pre and post conditions on everything.
class mw(QMainWindow):
    def __init__(self):
        super(mw, self).__init__()
        mainWindow = QWidget()
        mainLayout = QVBoxLayout()
        self.url = ""
        self.parser = Parser()

        # Setup for timer so I don't get banhammered lul
        self.preventOverload = QTimer()
        self.preventOverload.setSingleShot(True)
        self.preventOverload.timeout.connect(self.updateSearch)

        # Setup for searchbar widget
        self.defaultText = "Search with card names and text..."
        self.searchBar = QLineEdit()
        self.searchBar.setPlaceholderText(self.defaultText)
        self.searchBar.textChanged.connect(self.preventUpdateSearchOverload)

        # Setup for scroll area and related widgets
        self.cardViewer = QScrollArea()
        self.cardViewer.setWidgetResizable(True)

        self.scroller = QWidget()
        self.scrollLayout = QVBoxLayout()
        self.scroller.setLayout(self.scrollLayout)
        self.cardViewer.setWidget(self.scroller)

        # Setup for a clear search and table button.
        self.clearButton = QPushButton()
        self.clearButton.setText("Clear Tables")
        self.clearButton.clicked.connect(self.clearTables)

        # Add both main widgets to the main layout
        mainLayout.addWidget(self.searchBar)
        mainLayout.addWidget(self.cardViewer)
        mainLayout.addWidget(self.clearButton)

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
                self.scrollLayout.removeItem(card)
                return True
        return False

    def preventUpdateSearchOverload(self):
        self.preventOverload.start(1000)

    def updateSearch(self): # THIS SHOULD NEVER BE CALLED DIRECTLY
        self.url = self.searchBar.text() # NOTE: this means that there is a simple in operation to check if the search should come back.
        results = self.parser.search(self.url)
        results = sorted(results, key=lambda result: result[0].find(self.url)) # Uses a lambda that sorts by the earliest appearance of the search term.

        #TODO: This is a very dirty solution to get around some of the widgets mysteriously being NoneType. Try to find out root cause to not have to do this.
        while self.clearScrollLayout():
            pass

        for each in results:
            self.scrollLayout.addWidget(CardInfo(each[0], each[1], each[2], each[3], each[4], each[5], each[6]))

    def clearTables(self):
        self.searchBar.setText(self.defaultText)
        self.preventUpdateSearchOverload()
        self.searchBar.clear()
        self.parser.cache.clear()





main = QApplication([])
window = mw()

main.exec()
window.parser.cache.close()