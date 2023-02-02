class Solution:
    def isValid(self, s, left, right):
        l,r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif left or right:
                l += left
                r -= right
                left = right = 0
            else:
                return False
        return True
    
    def validPalindrome(self, s: str) -> bool:
        return self.isValid(s, 1, 0) or self.isValid(s, 0, 1)
        
