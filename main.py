import glob
import os

from trie import Trie

# trie = Trie()
#
# trie.add('chunk', 'chunk.xml')
# trie.add('chunky', 'chunky.xml')
# trie.add('chunky', 'chunky1.xml')
#
# print(trie.trie)
# print(trie.get('chunk'))
# print(trie.get('chunky'))


def index_emails(path_to_directory):
    trie = Trie()

    for path in glob.glob(os.path.join(path_to_directory, '**/*.'), recursive=True):
        with open(path, encoding='cp1251') as f:
            for line in f.readlines():
                for word in line.split():
                    normalized = word.lower()
                    trie.add(normalized, path)

    return trie


def test(word, trie):
    return trie.get(word)


trie = index_emails('skilling-j')
print(test('banned', trie))
