class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        words = ["Hello", "Alaska", "Dad", "Peace"]
        res = []
        for row in [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]:
            for word in words:
                w = word.lower()
                # 表示是否w的每个字符都在row中
                if set(w) <= row:
                    res.append(word)
        print(res)



