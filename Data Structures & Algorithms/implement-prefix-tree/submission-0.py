class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True