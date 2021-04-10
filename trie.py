END = None


class Trie:
    def __init__(self):
        self.trie = {}

    def add(self, word, path):
        node = self.trie

        for ch in word:
            if ch not in node:
                node[ch] = {}

            node = node[ch]

        if END not in node:
            node[END] = set()

        node[END].add(path)

    def get(self, word):
        node = self.trie

        for ch in word:
            if ch not in node:
                return []

            node = node[ch]

        if END not in node:
            return []

        return node[END]
