class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for letter in s:
            # 实际上是推演出这个规律哦
            num = num * 26 + ord(letter) -ord("A")+1
        return num


if __name__ == '__main__':
    print(Solution().titleToNumber("AB"));
    #ord
    # ord 只能单个字母
    #65
    print(ord("A"))
