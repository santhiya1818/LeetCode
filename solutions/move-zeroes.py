class Solution(object):
    def moveZeroes(self, nums):
        l = []
        l2 = []
        for i in range(len(nums)):
            if nums[i] != 0:
                l.append(nums[i])
        cnt = nums.count(0)
        for i in range(cnt):
            l.append(0)
        nums[:] = l
        