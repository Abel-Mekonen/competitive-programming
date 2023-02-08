class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    
        graph = defaultdict(list)
        queue = deque()
        queue.append(source)
        visited = set()
        answer = 0
        
        for idx, route in enumerate(routes):
            for bus in route:
                graph[bus].append(idx)
        
        while queue:
            for _ in range(len(queue)):
                station = queue.popleft()
                if station == target:
                    return answer

                for route in graph[station]:
                    if route not in visited:
                        for b in routes[route]:
                            queue.append(b)
                        visited.add(route)
            answer += 1
            
        return -1
            
