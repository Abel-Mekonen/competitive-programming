class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first, second, third = -inf, -inf, -inf
        for num in nums:
            if num > first:
                third = second
                second = first 
                first = num
            elif num < first and num > second:
                third = second
                second = num
            elif num < second and num > third:
                third = num
        
        return third if third != -inf else first
