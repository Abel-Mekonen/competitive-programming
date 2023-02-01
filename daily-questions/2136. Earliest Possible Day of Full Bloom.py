class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        merged = [(growTime[i], plantTime[i]) for i in range(len(growTime))]
        merged.sort(key = lambda x: (-x[0], x[1]))
        
        best = 0
        summ = 0
        for i in range(len(merged)):
            best = max(best, summ + merged[i][0] + merged[i][1])
            summ += merged[i][1]
        
        return best
