class Solution:
    def judgeCircle(moves):
        """
        :type moves: str
        :rtype: bool
        """
        if moves.count("U")==moves.count("D") and moves.count("R")==moves.count("L"):
            return True
        else:
            return False


# R（右），L（左），U（上）和 D（下）
# #输入: "UD"
# 输出: true
# 输入: "LL"
# 输出: false
if __name__ == '__main__':
    print(Solution.judgeCircle("UD"))