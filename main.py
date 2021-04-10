import email
import glob
import multiprocessing
import os
import string
import sys

from trie import Trie, END
from tqdm import tqdm


def normalize(word):
    return word.lower().strip(string.whitespace + string.punctuation)


def index_path(path):
    result = []

    with open(path, encoding='cp1251') as f:
        content = f.read()
        parsed = email.message_from_string(content)

        for (header, value) in parsed.items():
            for word in value.split():
                normalized = normalize(word)
                if normalized:
                    result.append((normalize(word), path))

        for word in parsed.get_payload().split():
            normalized = normalize(word)
            if normalized:
                result.append((normalized, path))

    return result


def index_emails(path_to_directory):
    trie = Trie()

    with multiprocessing.Pool() as p:
        paths = glob.glob(os.path.join(path_to_directory, '**/*.'), recursive=True)

        for pairs in tqdm(p.imap(index_path, paths), total=len(paths)):
            for (word, path) in pairs:
                trie.add(word, path)

    return trie


def test(word, trie):
    return trie.get(normalize(word))


def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else 'skilling-j'

    trie = index_emails(input_path)

    def walk(node):
        for ch in node:
            if ch == END:
                for path in node[ch]:
                    yield path
                continue
            yield from walk(node[ch])

    trie_paths = list(walk(trie.trie))
    print(f'Total in dir: {len(glob.glob(input_path + "/**/*.", recursive=True))} paths')
    print(f'Total in trie: {len(trie_paths)} paths')
    print(f'Unique in trie: {len(set(trie_paths))} paths')

    if input_path == 'skilling-j':
        print()

        # Test for no word in corpus
        alexey = test('alexey', trie)
        print(len(alexey) == 0)

        # Test for email header value with trailing punctuation
        investments = test('investments', trie)
        print(f'{input_path}/deleted_items/3.' in investments)

        # Test for regular word
        bosphorus = test('bosphorus', trie)
        print(f'{input_path}/all_documents/1298.' in bosphorus)


if __name__ == '__main__':
    main()
