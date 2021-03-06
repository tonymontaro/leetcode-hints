import string
import random

class Codec:
    def __init__(self):
        self.urls = {}
        self.known_urls = {}
        self.characters = list(string.ascii_letters) + list('1234567890')

    def encode(self, long_url):
        if long_url in self.known_urls:
            return self.known_urls[long_url]
        short_url = None
        while not short_url:
            url = self.get_short_str()
            if url not in self.urls:
                short_url = url
                self.urls[short_url] = long_url
                self.known_urls[long_url] = short_url
        return short_url
        

    def decode(self, short_url):
        if short_url in self.urls:
            return self.urls[short_url]

    def get_short_str(self):
        rs = [random.choice(self.characters) for _ in range(6)]
        return ''.join(rs)
