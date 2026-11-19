class Solution(object):
    def sumOfUnique(self, nums):
        s = 0
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                s+=nums[i]
        return s
        