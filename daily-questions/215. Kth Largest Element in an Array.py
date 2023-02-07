class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        li=heapq.nlargest(k,nums)
        return li[-1]
