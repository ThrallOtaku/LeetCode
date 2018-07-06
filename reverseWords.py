class Solution:
    def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        slist = s.split(" ")
        rstring = ""
        for ilist in slist:
            rstring += ilist[::-1] + " "
        return rstring.strip()


# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#
# 示例 1:
# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc"
if __name__ == '__main__':
    words = "Let's take LeetCode contest"
    print(Solution.reverseWords(words))
    pass
