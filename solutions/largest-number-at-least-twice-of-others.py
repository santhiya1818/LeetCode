class Solution(object):
    def dominantIndex(self, nums):
        m = max(nums)
        flag = m
        for i in range(len(nums)):
            if nums[i] * 2 > m and nums[i] != m:
                flag = -1
        if flag != -1:
            return nums.index(m)
        else:
            return -1
        