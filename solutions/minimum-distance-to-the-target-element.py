class Solution(object):
    def getMinDistance(self, nums, target, start):
        return min(abs(i - start) for i in range(len(nums)) if nums[i] == target)       