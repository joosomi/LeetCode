# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 후위 순회 : 왼 -> 오 -> root 
        # 모두 가장 깊은 리프 -> 그 지점 LCA 후보로 저장
        # 마지막으로 저장된 그 노드가 LCA

        def dfs(node):
            if not node:
                return (0, None)
            
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)

            
            if left_depth == right_depth:
                return (left_depth+1, node)
            elif left_depth > right_depth:
                return (left_depth+1, left_node)
            else:
                return (right_depth+1, right_node)

        return dfs(root)[1]
