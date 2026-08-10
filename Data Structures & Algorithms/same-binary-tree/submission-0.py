# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ls=[]
        rs=[]
        def dfs1(root):
            if not root :
                ls.append(None)
                return 
            ls.append(root.val)
            dfs1(root.left)
            dfs1(root.right)
        def dfs2(node):
            if not node:
                rs.append(None)
                return 
            rs.append(node.val)
            dfs2(node.left)
            dfs2(node.right)
        dfs1(p)
        dfs2(q)
        return ls==rs
            
        