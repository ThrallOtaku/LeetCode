class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binarynum = bin(n).replace('0b', '')
        # print(bin(n))
        # print(binarynum)
        # enumerate 先index 后item,可以enumerate 数字
        for index, item in enumerate(binarynum):
            # print("index:",index)
            # print("item:",item)
            # print("index-1:",index-1)
            # print(binarynum[index - 1])
            if index==len(binarynum)-1:
                break
            if item == binarynum[index + 1]:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().hasAlternatingBits(10));
