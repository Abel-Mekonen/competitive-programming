class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        answer  = []
        N = len(adjacentPairs) + 1
        nbrs = defaultdict(list)
        start, prev = None, None
        for n1, n2 in adjacentPairs:
            nbrs[n1].append(n2)
            nbrs[n2].append(n1)
        
        for nbr in nbrs:
            if len(nbrs[nbr]) == 1:
                start = nbr
                break
        
        for _ in range(N):
            answer.append(start)
            for nbr in nbrs[start]:
                if nbr != prev:
                    prev = start
                    start = nbr
                    break
        
        return answer
                    
        
        
        
            
