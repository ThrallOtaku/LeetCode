class Solution:
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x)[::-1] == str(x):
            return True
        else:
            return False


if __name__ == '__main__':
    # 判断回文数
    num1 = 121
    num2 = 321
    print(Solution.isPalindrome(num2))
