class Trie:
    def __init__(self):
        self.node = {}
        self.end = '*'
        self.cache = {}
    
    def add(self, word):
        node = self.node
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[self.end] = True
    
    def word_break(self, word, idx, node=None, depth=0):
        depth += 1
        if (idx, depth) not in self.cache:
            node = node or self.node
            ch = word[idx]
            if idx >= len(word)-1:
                self.cache[(idx, depth)] = ch in node and self.end in node[ch]
            elif ch not in node:
                self.cache[(idx, depth)] = False
            elif self.end in node[ch]:
                self.cache[(idx, depth)] = (
                    self.word_break(word, idx+1, node[ch], depth)
                    or self.word_break(word, idx+1, self.node, 0)
                )
            else:
                self.cache[(idx, depth)] = self.word_break(word, idx+1, node[ch], depth)
        return self.cache[(idx, depth)]
        

class Solution:
    a
    def wordBreak(self, s: str, word_dict) -> bool:
        trie = Trie()
        [trie.add(word) for word in word_dict]
        return trie.word_break(s, 0)


### Ingenious and fast solution from submitted
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        X = {}
        def wordBreak_(x):
            if x not in X:
                X[x] = False
                for word in wordDict:
                    if x.startswith(word):
                        n = len(word)
                        if len(x) == n or wordBreak_(x[n:]):
                            X[x] = True
                            break
            
            return X[x]
        
        return wordBreak_(s)
