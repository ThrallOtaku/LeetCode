class Solution:
    def uniqueMorseRepresentations(words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseCodes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        enChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        dic = dict()
        for index, code in enumerate(morseCodes):
            # 莫斯密码和英文字母做成字典,以英文字母为key
            dic[enChar[index]] = code
        # words转换成morese
        list = []
        for word in words:
            wordMorse = ''
            for i in word:
                wordMorse += dic[i]
            list.append(wordMorse)
        # 返回list去重后的长度
        return len(set(list))


#唯一摩尔斯密码词
# 输入: words = ["gin", "zen", "gig", "msg"]
# 输出: 2
# 解释:
# 各单词翻译如下:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
#
# 共有 2 种不同翻译, "--...-." 和 "--...--.".
# 26字母莫斯密码表
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",
# ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
# "...","-","..-","...-",".--","-..-","-.--","--.."]


if __name__ == '__main__':
    words = ["gin", "zen", "gig", "msg"]
    print(Solution.uniqueMorseRepresentations(words))
