# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root):
            if not root or root == p or root == q:
                return root
            right=find(root.right)
            left=find(root.left)

            if right and left:
                return root
            
            return right or left
        return find(root)
    