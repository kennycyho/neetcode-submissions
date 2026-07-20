class TrieNode:
    def __init__(self, val: str = "") -> None:
        self.val = val
        self.leaves = [None] * 26
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            i = ord(ch) - ord('a')
            if cur.leaves[i]:
                cur = cur.leaves[i]
            else:
                newNode = TrieNode(ch)
                cur.leaves[i] = newNode
                cur = newNode
        cur.isWord = True

    def search(self, word: str) -> bool:
        def recurse(cur, wordIdx):
            if not cur:
                return False
            if wordIdx == len(word):
                return cur.isWord
            
            ch = word[wordIdx]
            if ch == ".":
                for leaf in cur.leaves:
                    if recurse(leaf, wordIdx + 1):
                        return True
                return False
            else:
                return recurse(cur.leaves[ord(ch) - ord('a')],  wordIdx + 1)

        return recurse(self.root, 0)