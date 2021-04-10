from trie import Trie

trie = Trie()

trie.add('chunk', 'chunk.xml')
trie.add('chunky', 'chunky.xml')
trie.add('chunky', 'chunky1.xml')

print(trie.trie)
print(trie.get('chunk'))
print(trie.get('chunky'))