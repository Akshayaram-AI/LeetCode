# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans =0 
        def height(root):
            nonlocal ans
            if not root:
                return 0
            right = height(root.right)
            left = height(root.left)

            ans = max(ans,left+right)
            return 1+max(left,right)

        height(root)
        return ans