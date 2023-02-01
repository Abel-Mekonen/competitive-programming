class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        answer = [[0] * len(mat[0]) for _ in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                top = mat[i - 1][j] if i else 0
                left = mat[i][j - 1] if j else 0
                top_left = mat[i - 1][j - 1] if i and j else 0
                current = mat[i][j]
                mat[i][j] = top + left + current - top_left
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                l_idx, r_idx = max(j - k, 0), min(j + k, len(mat[0]) - 1)
                t_idx, b_idx = max(i - k, 0), min(i + k, len(mat) - 1)
                
                left = mat[b_idx][l_idx - 1] if l_idx else 0
                top = mat[t_idx - 1][r_idx] if t_idx else 0
                top_left = mat[t_idx - 1][l_idx - 1] if l_idx and t_idx else 0
                net = mat[b_idx][r_idx] - left - top + top_left
                answer[i][j] = net
        
        return answer
