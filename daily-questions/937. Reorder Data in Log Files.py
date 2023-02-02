class Solution:
    def sort_key(self,x):
        temp = x.split()
        return temp[1:], temp[0]
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            temp = log.split()
            if temp[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
                
        letter_logs.sort(key= self.sort_key)
        letter_logs.extend(digit_logs)
        
        return letter_logs
        
