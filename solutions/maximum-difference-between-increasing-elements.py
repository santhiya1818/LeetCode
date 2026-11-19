class Solution(object):
    def maximumDifference(self, nums):
        l = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if i < j and nums[j] - nums[i] != 0:
                    l.append(nums[j]-nums[i])
            l.append(-1)
        return max(l)
        