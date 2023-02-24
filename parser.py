import socket

from bs4 import BeautifulSoup
import requests

import scrython
import cacher

class Parser:
    def __init__(self):
        self.card = "" # Ensure that this is public to other classes.
        self.cache = cacher.Cacher()
        self.returnCard = []

    def search(self, name):
        if name == "": # This is in place to avoid just pulling the entire cache when backspacing your way to victory.
            return []
        try:
            pageNum = 1
            self.returnCard = []
            while pageNum == 1 or self.card.has_more(): # pageNum ensures it runs once, self.card.has_more ensures it stops once it runs out of pages.
                self.card = scrython.cards.Search(q=name, page=pageNum) # Runs a search query based on whatever the user puts in.
                for each in range(len(self.card.data())): # Adds the name of each item into the cache
                    # The total_cards check is to allow for more narrow searches to find cards less strictly when it doesn't affect time much.
                    # the compareStart check is to cut down on huge checks.
                    #TODO: add a page system to cut down on slow query times.
                    if self.card.scryfallJson.get('total_cards') < 200 or self.compareStart(name, self.card.data()[each].get('name')):
                        info = [self.card.data()[each].get('name'),
                                self.card.data()[each].get('mana_cost'),
                                self.card.data()[each].get('type_line'),
                                self.card.data()[each].get('oracle_text'),
                                self.card.data()[each].get('power'),
                                self.card.data()[each].get('toughness'),
                                self.card.data()[each].get('loyalty')]
                        self.returnCard.append(info)
                        self.cache.add(info)
                pageNum += 1
        except Exception as e:
            print(e)
            self.returnCard = self.cache.search(name)

        return self.returnCard

    def compareStart(self, searchTerm, searchResult):
        return searchTerm == searchResult[0:len(searchTerm)]