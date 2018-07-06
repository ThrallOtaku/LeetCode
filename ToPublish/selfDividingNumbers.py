class Solution:
    def selfDividingNumbers(left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        nums = []
        if 1 <= left <= right <= 10000:
            # range含左不含右
            for i in range(left, right + 1):
                valinum = 0
                for character in str(i):
                    if int(character) == 0 or i % int(character) != 0:
                        valinum += 1
                        break
                if valinum == 0:
                    nums.append(i)
        return nums

#自除数
# 输入：
# 上边界left = 1, 下边界right = 22
# 输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
if __name__ == '__main__':
    for i in str(100):
        print(i)
    print(Solution.selfDividingNumbers(1, 22))
