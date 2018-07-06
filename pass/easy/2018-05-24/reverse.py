class Solution:
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            rNum = int(str(x)[::-1])
        else:
            rNum = int("-" + str(-x)[::-1])
        # 判断返回参数是否超出整数范围
        if rNum > (pow(2, 31) - 1) or rNum < pow(-2, 31):
            return 0
        else:
            return rNum



if __name__ == '__main__':
    num1 = -123
    num2 = 988766
    num3 = 120
    str1 = "women manmanman "

    num444 = 9646324351
    num555 = pow(2, 31) - 1
    num666 = pow(-2, 31)
    print("num555", num555)
    print(num444 > num555)
    print(num444 < num666)
    print(num444 > num555 | num444 < num666)
    print("or  ", (num444 > num555 or num444 < num666))
    print(Solution.reverse(1534236469))
