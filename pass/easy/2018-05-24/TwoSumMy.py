class Solution(object):
    def twoSum(nums, target):
        for i in nums:
            for j in nums:
                if i + j == target:
                    return [nums.index(i), nums.index(j)]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution.twoSum(nums, target))
