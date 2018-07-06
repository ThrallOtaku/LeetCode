class Solution:
    def hammingDistance(x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # 相当于按位异或
        n = x ^ y
        # 返回一个int的整数表示
        n = bin(n)
        return n.count('1')


# 汉明距离
# 输入: x = 1, y = 4
# 输出: 2
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑  ↑

if __name__ == '__main__':
    x = 1
    y = 4
    print(Solution.hammingDistance(x, y))
