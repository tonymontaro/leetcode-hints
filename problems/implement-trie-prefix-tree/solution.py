class Trie:
    def __init__(self):
        self.root = {}
        self.end = "*"

    def insert(self, word: str) -> None:
        """O(w) time and space"""
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end] = True

    def search(self, word: str) -> bool:
        """O(w) time"""
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end in node

    def startsWith(self, prefix: str) -> bool:
        """O(p) time"""
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
