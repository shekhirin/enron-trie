import email
import glob
import os
import string

from trie import Trie


def normalize(word):
    return word.lower().strip(string.whitespace + string.punctuation)


def index_emails(path_to_directory):
    trie = Trie()

    for path in glob.glob(os.path.join(path_to_directory, '**/*.'), recursive=True):
        with open(path, encoding='cp1251') as f:
            content = f.read()
            parsed = email.message_from_string(content)

            for (header, value) in parsed.items():
                for word in value.split():
                    normalized = normalize(word)
                    if normalized:
                        trie.add(normalize(word), path)

            for word in parsed.get_payload().split():
                normalized = normalize(word)
                if normalized:
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

    # Test for no word in corpus
    biscuit = test('biscuit', trie)
    print(len(biscuit) == 0)

    # Test for email header value with trailing ...
    investments = test('investments', trie)
    print('skilling-j/deleted_items/3.' in investments)

    # Test for regular word
    print(test('bosphorus', trie))


if __name__ == '__main__':
    main()
