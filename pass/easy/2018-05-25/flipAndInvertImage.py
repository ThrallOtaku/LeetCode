class Solution:
    def flipAndInvertImage(A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rList = []
        for elist in A:
            elist.reverse()
            for index, element in enumerate(elist):
                elist[index] = element ^ 1
            # append 是作为list元素，+=是作为拆分的单个元素
            rList.append(elist)
        return rList


# 输入: [[1,1,0],[1,0,1],[0,0,0]]
# 输出: [[1,0,0],[0,1,0],[1,1,1]]
# 解释: 首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
#      然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]

# 输入: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# 输出: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 解释: 首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
#      然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

if __name__ == '__main__':
    # basic
    list1 = [1, 2, 3, 4]
    list1.reverse()
    print(list1)

    # run
    A = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
print(Solution.flipAndInvertImage(A))
