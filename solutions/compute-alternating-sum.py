class Solution(object):
    def alternatingSum(self, nums):
        return sum(nums[::2]) - sum(nums[1::2])
