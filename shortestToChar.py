class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        dic = {}
        res = []
        for index, s in enumerate(S):
            if s == C:
                # 放入字典
                dic[index] = s
        for i in range(len(S)):
            tmp = []
            for key in dic.keys():
                # 计算所有根C的距离
                tmp.append(abs(key - i))
            # 取最小的那个
            res.append(min(tmp))
        return res
