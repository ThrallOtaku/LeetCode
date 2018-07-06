class Solution:
    def numJewelsInStones(J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        n = 0
        for i in J:
            #S.count(i),S字符串中有多少个i
            n += S.count(i)
        return n


# 宝石石头问题
# 输入: J = "aA", S = "aAAbbbb"
# 输出: 3
# 输入: J = "z", S = "ZZ"
# 输出: 0

if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    #这样可以直接遍历String的字符,666
    for i in S:
        print(i)

    print(Solution.numJewelsInStones(J, S))
