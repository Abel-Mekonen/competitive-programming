class Solution:
    def racecar(self, target: int) -> int:
        queue = deque()
        queue.append([0,0,1])
        visited = set()
        while queue:  
            pos, steps, speed = queue.popleft()
            state =(pos, speed)
            
            if pos == target:
                return steps
            
            if state not in visited:
                visited.add(state)
                nxt_pos, nxt_steps, nxt_speed = pos + speed, steps + 1, speed * 2
                queue.append([nxt_pos, nxt_steps, nxt_speed])
                if (pos + speed < target and speed < 0) or (pos + speed > target and speed > 0):
                    new_speed = -1 if speed > 0 else 1
                    queue.append([pos, steps + 1, new_speed])
