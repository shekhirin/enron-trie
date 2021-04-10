class Trie:
    def __init__(self):
        self.trie = {}
        self.PATH = 'PATH'

    def add(self, word, path):
        node = self.trie

        for ch in word:
            if ch not in node:
                node[ch] = {}

            node = node[ch]

        if self.PATH not in node:
            node[self.PATH] = set()

        node[self.PATH].add(path)

    def get(self, word):
        node = self.trie

        for ch in word:
            if ch not in node:
                return []

            node = node[ch]

        if self.PATH not in node:
            return []

        return node[self.PATH]

