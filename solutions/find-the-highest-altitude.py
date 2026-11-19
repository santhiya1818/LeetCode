class Solution(object):
    def largestAltitude(self, gain):
        cur = 0
        max1  = 0
        for i in range(len(gain)):
            cur += gain[i]
            max1 = max(cur,max1)
        return max1
        