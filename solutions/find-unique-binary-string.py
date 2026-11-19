class Solution(object):
    def findDifferentBinaryString(self, nums):
        n = nums[0];
        d = len(n)
        p = pow(2,d)
        for i in range(p):
            de = bin(i)[2:].zfill(d)
            if de not in nums:
                res = de
        return res
        