class Solution:
    def maximumSwap(self, num: int) -> int:
        temp = [int(digit) for digit in str(num)]
        nxt_greatest = deque()
        
        for i in range(len(temp) - 1, -1, -1):
            if not nxt_greatest or temp[i] > temp[nxt_greatest[0]]:
                nxt_greatest.appendleft(i)
            else:
                nxt_greatest.appendleft(nxt_greatest[0])
        
        for i in range(len(temp) - 1):
            if temp[i] < temp[nxt_greatest[i]]:
                temp[i], temp[nxt_greatest[i]] = temp[nxt_greatest[i]], temp[i]
                break
                
        return int(''.join(map(str, temp)))
                
        
        
            
        
        