class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites, best, left = 0, inf , 0
        
        for right in range(len(blocks)):
            if blocks[right] == 'W':
                whites += 1
                
            while right - left + 1 == k:
                best = min(best, whites)
                if blocks[left] == 'W':
                    whites -= 1
                left += 1 
                
        return best
                    
                
