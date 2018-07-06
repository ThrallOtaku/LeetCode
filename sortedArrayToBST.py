# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) // 2  # “//”表示整数除法；“/”浮点数除法；
        # 根节点是
        root = TreeNode(nums[mid])
        # 左边剩下的list
        left = nums[:mid]
        # 右边剩下的list
        right = nums[mid + 1:]
        # 递归左边的list
        root.left = self.sortedArrayToBST(left)
        # 递归右边的list
        root.right = self.sortedArrayToBST(right)
        return root


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    print(Solution().sortedArrayToBST(nums))
