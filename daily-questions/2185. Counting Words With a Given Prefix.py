class Solution:
    def insert(self, word, root):
        curr = root
        for char in word:
            if char not in curr:
                curr[char] = {}
                curr[char]['#'] = 0
            curr = curr[char]
            curr['#'] += 1
     
    
    def search(self, word, root):
        curr = root 
        for char in word:
            if char not in curr:
                return 0
            curr = curr[char]
        return curr['#']
    
    
    def prefixCount(self, words: List[str], pref: str) -> int:
        root = {}
        root['#'] = 0
        for word in words:
            self.insert(word, root) 
        return self.search(pref, root)
