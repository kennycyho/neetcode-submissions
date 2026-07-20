class Node:
    def __init__(self, val: str = ""):
        self.leaves = [None] * 26 # len 26 array, a-z
        self.val = val
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root: Node = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            charIdx = self.getCharIdx(char)
            nextNode = cur.leaves[charIdx]
            if not nextNode:
                nextNode = Node(char)
                cur.leaves[charIdx] = nextNode
            cur = nextNode
        cur.isWord = True

    def search(self, word: str) -> bool:
        # travel down trie until word is completed (check complete flag) or char not exists
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            charIdx = self.getCharIdx(char)
            nextNode = cur.leaves[charIdx]
            if not nextNode:
                return False
            cur = nextNode
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        # travel down trie until prefix is completed or char not exists
        cur = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            charIdx = self.getCharIdx(char)
            nextNode = cur.leaves[charIdx]
            if not nextNode:
                return False
            cur = nextNode
        return True
        
    def getCharIdx(self, char: str) -> int:
        return ord(char) - ord("a")