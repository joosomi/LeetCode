# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # if not root:
        #     return 0
        
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        # # + 1 => root를 depth에 포함시킴



        depth = 0
        if root:
            nodes = [root]
        else:
            nodes = []

        while nodes:
            depth +=1
            queue = []
            for i in nodes:
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
            nodes = queue

        return depth