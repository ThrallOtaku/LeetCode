class Solution:
    def reverseString(s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


# 反转字符串
# 输入：s = "hello"
# 返回："olleh"
if __name__ == '__main__':
    s='hello'
    print(Solution.reverseString(s))
