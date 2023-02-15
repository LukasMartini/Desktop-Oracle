from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QVBoxLayout, QGridLayout
from PyQt6.QtWidgets import QLineEdit, QPushButton, QScrollArea, QLabel

from cardInfo import CardInfo

class mw(QMainWindow):
    def __init__(self):
        super(mw, self).__init__()
        mainWindow = QWidget()
        mainLayout = QVBoxLayout()

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
        pass # Will eventually pass text to the class that handles searching



main = QApplication([])
window = mw()

main.exec()