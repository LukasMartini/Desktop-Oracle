import socket

from bs4 import BeautifulSoup
import requests

import scrython
import time
import cacher

class Parser:
    def __init__(self):
        self.card = "" # Ensure that this is public to other classes.
        self.cache = cacher.Cacher()

    def search(self, name): # TODO: avoid searching with scrython directly, try to check the cache first.
        try:
            time.sleep(0.2) # Used to avoid an IP ban.
            self.card = scrython.cards.Search(q=name) # Runs a search query based on whatever the user puts in.
            for each in range(len(self.card.data())): # Adds the name of each item into the cache
                self.cache.add(self.card.data()[each].get('name'))
        except Exception as e:
            self.card = self.cache.search(name)