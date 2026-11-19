class Solution(object):
    def separateDigits(self, nums):
        l = []
        for i in nums:
            s = str(i)
            for j in s:
                d = int(j)
                l.append(d)
        return l
        