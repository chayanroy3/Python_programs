# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #call recursively for left, root and right
        result=[]
        def f(node):
            if node == None:
                return
            if node.left != None:
                f(node.left)
            result.append(node.val)
            if node.right!= None:
                f(node.right)
            #result.append(node.val)
        f(root)
        return result
