class Solution(object):
    def missingNumber(self, nums):
        num = sorted(nums)
        for i in range(len(nums)):
            if i != num[i]:
                return i
        return i+1       