class Solution(object):
    def runningSum(self, nums):
        l = []
        sum1 = 0
        for i in nums:
            sum1 = sum1 + i
            l.append(sum1)
        return l
        