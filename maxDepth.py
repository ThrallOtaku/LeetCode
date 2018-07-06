# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        leftDepth = self.maxDepth(root.left) + 1
        rightDepth = self.maxDepth(root.right) + 1
        return leftDepth if leftDepth>rightDepth else rightDepth



# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3
if __name__ == '__main__':
    pass
