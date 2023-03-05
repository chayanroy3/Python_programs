# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root ==None:
            return True
        else:
            return self.ismirror(root.left,root.right)
    def ismirror(self,left,right):
        if left == None and right == None:
            return True
        if left == None or right== None:
            return False
        if left.val == right.val:
            out=self.ismirror(left.left,right.right)
            inn=self.ismirror(left.right,right.left)
            return out and inn
        else:
            return False
