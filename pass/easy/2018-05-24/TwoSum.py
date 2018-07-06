class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buff_dic = dict()
        for index, value in enumerate(nums):
            print(index, value)
            sub = target - value
            if sub in buff_dic:
                return [buff_dic[sub], index]
            else:
                buff_dic[value] = index


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution.twoSum(nums, target))
