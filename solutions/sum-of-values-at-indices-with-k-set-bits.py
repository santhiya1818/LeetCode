class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        sum1 = 0
        for i in range(len(nums)):
            s = bin(i)[2:]
            if s.count("1") == k:
                sum1 += nums[i]
        return sum1
        