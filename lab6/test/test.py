import unittest
from src.main import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.words = [
            "website",
            "trigger",
            "miwa",
            "mysql",
            "react",
            "flask",
            "spring"
        ]
        for word in self.words:
            self.trie.insert(word)

    def test_search_existing_words(self):
        for word in self.words:
            self.assertTrue(self.trie.search(word))

    def test_search_non_existing_word(self):
        self.assertFalse(self.trie.search("nodejs"))
        self.assertFalse(self.trie.search("angular"))
        self.assertFalse(self.trie.search("slack"))

    def test_starts_with_existing_prefix(self):
        self.assertTrue(self.trie.starts_with("we"))
        self.assertTrue(self.trie.starts_with("mi"))
        self.assertTrue(self.trie.starts_with("mysq"))

    def test_starts_with_non_existing_prefix(self):
        self.assertFalse(self.trie.starts_with("me"))
        self.assertFalse(self.trie.starts_with("qwe"))
        self.assertFalse(self.trie.starts_with("vfr"))


if __name__ == '__main__':
    unittest.main()
