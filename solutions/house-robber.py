class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        return max(dp)            