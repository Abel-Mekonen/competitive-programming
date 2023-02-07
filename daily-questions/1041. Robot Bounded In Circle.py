class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        x, y = 0, 0
        idx = 0
        for d in instructions:
            if d == 'G':
                x_n, y_n = directions[idx]
                x += x_n
                y += y_n
            elif d == 'R':
                idx = (idx + 1) % 4
            else:
                idx = (idx - 1 + 4) % 4
        
        if (x == 0 and y == 0 ) or idx:
            return True
        
        return False
