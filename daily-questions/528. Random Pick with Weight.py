class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        total = sum(w)
        for i in range(len(self.w)):
            self.w[i] = math.floor((self.w[i] / total) * 100)    
        for i in range(1,len(self.w)):
            self.w[i] += self.w[i - 1]
               
    def search(self, target):
        left, right = 0, len(self.w) - 1
        
        while left < right:
            mid = (left + right) // 2
            if self.w[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        return right
    
    def pickIndex(self) -> int:
        target = random.randint(0, self.w[-1])
        return self.search(target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
