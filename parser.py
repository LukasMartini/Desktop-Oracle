import socket

from bs4 import BeautifulSoup
import requests

import scrython
import cacher

class Parser:
    def __init__(self):
        self.card = "" # Ensure that this is public to other classes.
        self.cache = cacher.Cacher()

    def search(self, name):
        try:
            self.card = scrython.cards.Search(q=name) # Runs a search query based on whatever the user puts in.
            self.returnCard = []
            for each in range(len(self.card.data())): # Adds the name of each item into the cache
                self.returnCard.append((self.card.data()[each].get('name'),
                                        self.card.data()[each].get('image_uris').get('small'),
                                        self.card.data()[each].get('image_uris').get('normal'),
                                        self.card.data()[each].get('mana_cost'),
                                        self.card.data()[each].get('type_line'),
                                        self.card.data()[each].get('oracle_text'),
                                        self.card.data()[each].get('power'),
                                        self.card.data()[each].get('toughness'),
                                        self.card.data()[each].get('loyalty')))
                self.cache.add([self.card.data()[each].get('name'),
                                self.card.data()[each].get('image_uris').get('small'),
                                self.card.data()[each].get('image_uris').get('normal'),
                                self.card.data()[each].get('mana_cost'),
                                self.card.data()[each].get('type_line'),
                                self.card.data()[each].get('oracle_text'),
                                self.card.data()[each].get('power'),
                                self.card.data()[each].get('toughness'),
                                self.card.data()[each].get('loyalty')])
                #print(self.card.data()[each]) # DEBUG CODE, DELETE LATER
            self.card = self.returnCard
        except Exception as e:
            self.card = self.cache.search(name)

        return self.card