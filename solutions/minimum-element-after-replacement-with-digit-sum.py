class Solution(object):
    def minElement(self, nums):
        l = []
        for i in nums:
            s = str(i)
            d = 0
            for j in s:
                d+=int(j)
            l.append(d)
        return min(l)
        