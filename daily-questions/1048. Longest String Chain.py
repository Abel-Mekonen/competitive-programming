class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        freq = defaultdict(int)
        s = set(words)
        
        for word in words:
            freq[word] = 1
        
        words.sort(key = lambda x: len(x))
        for word in words:
            for i in range(len(word)):
                pred = word[:i] + word[i + 1:]
                if pred in s:
                    freq[word] = max(freq[word], freq[pred] + 1)
        
        return max(freq.values())
