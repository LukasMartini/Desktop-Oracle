import socket

from bs4 import BeautifulSoup
import requests

import scrython
import scrython.foundation
import cacher

class Parser:
    def __init__(self):
        self.card = "" # Ensure that this is public to other classes.
        self.cache = cacher.Cacher()
        self.returnCard = []

    def search(self, name, pageNum):
        if name == "": # This is in place to avoid just pulling the entire cache when backspacing your way to victory.
            return []
        try:
            self.returnCard = []
            self.card = scrython.cards.Search(q=name, page=pageNum, order="name", dir="asc") # Runs a search query based on whatever the user puts in.
            for each in range(len(self.card.data())): # Adds the name of each item into the cache
                info = [self.card.data()[each].get('name'),
                        self.card.data()[each].get('mana_cost'),
                        self.card.data()[each].get('type_line'),
                        self.card.data()[each].get('oracle_text'),
                        self.card.data()[each].get('power'),
                        self.card.data()[each].get('toughness'),
                        self.card.data()[each].get('loyalty')]
                self.returnCard.append(info)
                self.cache.add(info)
        except scrython.ScryfallError as e: # Brute force error checking, ensures that the page is turned blank if you go beyond the number of pages available.
            return pageNum-1
        except Exception as p:
            print(p)
            self.returnCard = self.cache.search(name)
        return self.returnCard