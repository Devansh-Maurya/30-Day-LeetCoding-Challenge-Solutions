# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder or not len(preorder):
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        
        i = 1
        while i < len(preorder) and (preorder[i] < root.val):
            i += 1

        left = preorder[1:i]
        right = preorder[i:]
                
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        
        return root
