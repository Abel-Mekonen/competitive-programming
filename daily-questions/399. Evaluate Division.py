class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        NQ = len(queries)
        answer = [-1.0]*NQ
        
        for idx, equation in enumerate(equations):
            graph[equation[0]].append((equation[1], values[idx]))
            graph[equation[1]].append((equation[0], 1/values[idx]))
            
        for i in range(NQ):
            if queries[i][0] in graph and queries[i][1] in graph:
                visited = set()
                queue = deque([(queries[i][0], 1)])
                while queue:
                    node, value = queue.popleft()
                    if node == queries[i][-1]:
                        answer[i] = value
                        break
                    for child in graph[node]:

                        if child not in visited:
                            queue.append((child[0], child[1]*value))
                            visited.add(child)
        return answer
