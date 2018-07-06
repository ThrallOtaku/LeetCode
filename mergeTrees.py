class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)+str(self.left)+str(self.right)

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        # 左叶子深度遍历
        t1.left = self.mergeTrees(t1.left, t2.left)
        # 右叶子深度遍历
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


# 给一个list转换成二叉树
def createBinaryTree(nodesList, t):
    for node in nodesList:
        if node is None:
            t = None
        else:
            t = TreeNode(node)
            del (nodesList[0])
            t.left = createBinaryTree(nodesList, t.left)
            t.right = createBinaryTree(nodesList, t.right)
    return t


# 前序遍历,根左右
# 中序遍历,左根右
# 后序遍历,左右根
def preorder(t, list):
    if t is None:
        return;
    else:
        print(t.val)
        list.append(t.val)
        print(list)
        preorder(t.left, list)
        preorder(t.right, list)


def inOrder(self,TreeNode):
    if TreeNode == None:
        return
    # 先打印左结点，再打印根结点，后打印右结点
    self.inOrder(TreeNode.left)
    print(TreeNode.data)
    self.inOrder(TreeNode.right)

def postOrder(self,TreeNode):
    if TreeNode == None:
        return
    # 先打印左结点，再打印右结点，后打印根结点
    self.postOrder(TreeNode.left)
    self.postOrder(TreeNode.right)
    print(TreeNode.data)

# 合并二叉树
# 输入:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# 输出:
# 合并后的树:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7


if __name__ == '__main__':
    t = None
    t1 = createBinaryTree([1, 3, 2, 5], t)
    print(t1)
    list = []
    # 前序遍历二叉树
    preorder(t1, list)
