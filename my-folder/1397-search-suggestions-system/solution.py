class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            if len(curr.words) < 3:
                curr.words.append(word)

    def search(self, prefix):
        curr = self.root
        res = []

        for char in prefix:
            if char not in curr.children:
                curr = None
                break
            curr = curr.children[char]
            res.append(curr.words if curr else [])
        while len(res) < len(prefix):
            res.append([])

        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # products.sort()
        # res = []
        # prefix = ""

        # for char in searchWord:
        #     prefix += char
        #     match = []

        #     for word in products:
        #         # if word.startswith(prefix):
        #         if word[:len(prefix)] == prefix:
        #             match.append(word)

        #         if len(match) == 3:
        #             break

        #     res.append(match)

        # return res
        products.sort()
        trie = Trie()

        for prod in products:
            trie.insert(prod)

        return trie.search(searchWord)
