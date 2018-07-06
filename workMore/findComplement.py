class Solution:
    def findComplement(num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        #从第一位开始一位一位按位异或获得补数
        while num >= i:
            # ^表示按位进行亦或运算
            num ^= i
            # 各二进位全部左移若干位,高位丢弃,低位补0
            i <<= 1
        return num


# 输入: 5
# 输出: 2
# 解释: 5的二进制表示为101（没有前导零位），其补数为010。所以你需要输出2。
# 输入: 1
# 输出: 0
# 解释: 1的二进制表示为1（没有前导零位），其补数为0。所以你需要输出0。

if __name__ == '__main__':
    print(Solution.findComplement(5))
