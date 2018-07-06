class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        """
        python 交换两个变量的值不需要重剑变量
        like    a,b=b,a
        """
        root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root
