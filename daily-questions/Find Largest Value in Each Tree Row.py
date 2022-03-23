# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = collections.deque()
        layer_id = 1
        que.append((root,1))
        loc_max = root.val
        ans=[]
        while que:
            curr = que.popleft()
            if curr[0].left:
                que.append((curr[0].left,curr[1] + 1))
            if curr[0].right:
                que.append((curr[0].right,curr[1] + 1))   
            if curr[1] == layer_id:
                loc_max = curr[0].val if curr[0].val > loc_max else loc_max
            else:
                ans.append(loc_max)
                loc_max = curr[0].val
                layer_id = curr[1]
            if not que:
                
                ans.append(loc_max if loc_max > curr[0].val else curr[0].val)
        return ans
                
                  
        