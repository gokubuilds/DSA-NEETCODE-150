# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lowest_common_ancestor = root

        node = root
        while True:
            print(node.val)
            if node.val == p.val or node.val == q.val:
                return node
            elif (node.val > p.val and node.val < q.val) or (node.val < p.val and node.val > q.val):
                return node
            elif node.val > p.val and node.val > q.val:
                node = node.left
                continue
            elif node.val < p.val and node.val < q.val:
                node = node.right
                continue