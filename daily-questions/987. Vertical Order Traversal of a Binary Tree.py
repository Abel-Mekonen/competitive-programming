class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        li = []
        
        def dfs(node , order_v ,order_h ):
            li.append((order_v, order_h , node.val))
            if node.left:
                dfs(node.left , order_v - 1 , order_h + 1)
            if node.right:
                dfs(node.right , order_v + 1 , order_h + 1)
                
        dfs(root , 0 , 0)
        li.sort()
        ans = []
        level = li[0][0]
        temp = []
        
        for i in li:
            if i[0] == level:
                temp.append(i[2])
            else:
                ans.append(temp)
                level = i[0]
                temp = [i[2]]
                
        ans.append(temp)
        return ans
