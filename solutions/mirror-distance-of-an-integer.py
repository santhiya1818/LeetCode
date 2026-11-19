class Solution(object):
    def mirrorDistance(self, n):
        s = str(n)
        c = int(s[::-1])
        return abs(c - n)
        