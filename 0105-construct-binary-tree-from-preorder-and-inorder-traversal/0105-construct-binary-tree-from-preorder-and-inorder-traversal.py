# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        
        root = TreeNode()
    
        if len(inorder) == 0 or len(preorder) == 0:
            return None

        root.val = preorder.pop(0)
        idx = inorder.index(root.val)

        #중위순회 
        inorder_left = inorder[:idx]
        inorder_right = inorder[idx+1:]
        #전위순회 
        preorder_left = preorder[:len(inorder_left)]
        preorder_right = preorder[len(inorder_left):]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root
            