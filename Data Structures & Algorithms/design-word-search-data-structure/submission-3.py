class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True        

    def search(self, word: str) -> bool:
        def dfs_search(start: int, root: TrieNode):
            curr = root
            for i in range(start, len(word)):
                if word[i] == ".":
                    for child in curr.children.values():
                        if dfs_search(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.is_end
                
        return dfs_search(0, self.root)
