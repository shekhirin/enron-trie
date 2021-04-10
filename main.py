import glob
import os

from trie import Trie


def index_emails(path_to_directory):
    trie = Trie()

    for path in glob.glob(os.path.join(path_to_directory, '**/*.'), recursive=True):
        with open(path, encoding='cp1251') as f:
            content = f.read()
            content = content[content.index('\n\n'):]
            for word in content.split():
                normalized = word.lower().strip()
                trie.add(normalized, path)

    return trie


def test(word, trie):
    return trie.get(word.lower().strip())

def main():
    # trie = Trie()
    #
    # trie.add('chunk', 'chunk.xml')
    # trie.add('chunky', 'chunky.xml')
    # trie.add('chunky', 'chunky1.xml')
    #
    # print(trie.trie)
    # print(trie.get('chunk'))
    # print(trie.get('chunky'))

    trie = index_emails('skilling-j')
    print(test('biscuit', trie))  # Test for no word in corpus
    print(test('mime', trie))  # Test for email header value
    print(test('bosphorus', trie))  # Test for regular word


if __name__ == '__main__':
    main()