# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return height(root)[1]
        
        
def height(root):
    if not root:
        return 0, 0
    
    l = height(root.left)
    r = height(root.right)
    
    lh = l[0]
    rh = r[0]
    
    ld = l[1]
    rd = r[1]
    
    h = max(lh, rh) + 1
    
    diam = max(ld, rd, lh + rh)
    return (h, diam)
