# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        depth = inorder.index(preorder[0])
        left = self.buildTree(preorder[1:depth+1],inorder[:depth])
        right = self.buildTree(preorder[depth+1:],inorder[depth+1:])
        root.left = left
        root.right = right
        return root