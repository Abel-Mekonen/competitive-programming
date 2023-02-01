class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(nums)
        if 0 in s:
            return len(s) - 1
        else:
            return len(s)
