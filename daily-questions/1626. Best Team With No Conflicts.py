class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        indices = [i for i in range(len(ages))]
        indices.sort(key = lambda x : (ages[x], scores[x]))
        dp = [0] * len(ages)
        
        for i in range(len(ages)):
            prev, curr_score = 0, scores[indices[i]]
            
            for j in range(i):
                if dp[j] > prev and scores[indices[j]] <= curr_score:
                    prev = dp[j]
            dp[i] = prev + curr_score
        
        return max(dp)
