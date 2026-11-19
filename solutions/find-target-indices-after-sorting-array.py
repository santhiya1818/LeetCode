class Solution(object):
    def targetIndices(self, nums, target):
        l = nums.sort()
        l1 = []
        for i in range(len(nums)):
            if nums[i] == target:
                l1.append(i)
        return l1
        