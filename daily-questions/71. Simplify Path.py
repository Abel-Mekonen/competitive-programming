class Solution:
    def removeDots(self, stack):
        c = 0
        s = 0
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == '.':
                c += 1
            elif stack[i] == '/':
                s += 1
                break
            else:
                break
        
        if c == 2 and s == 1:
            slashes  = 0
            while stack and slashes < 2:
                if stack[-1] == '/':
                    slashes += 1
                stack.pop()
            stack.append('/')
                
        elif c == 1 and s == 1:
            stack.pop()
        
    def simplifyPath(self, path: str) -> str:
        stack = ['/']
        for i in range(len(path)):
            if path[i] == '/' :
                self.removeDots(stack)
                
            if not stack:
                stack.append(path[i])
            else:
                if path[i] == '/':
                    if  stack[-1] != '/':
                        stack.append('/')
                else:
                    stack.append(path[i])
                    
        self.removeDots(stack)
        answer = ''.join(stack)
        return answer if (answer[-1] != '/') or (len(answer) <= 1) else answer[:len(answer) - 1]
            
                    
                    
