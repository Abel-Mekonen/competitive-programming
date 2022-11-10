class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits.insert(0,0)
        carry = 1
        
        for i in range(len(digits) - 1, -1, -1):
            
            current_sum = digits[i] + carry
            digits[i] = current_sum % 10
            if current_sum < 10:
                break
                
        if digits[0]:
            return digits
        
        return digits[1:]
