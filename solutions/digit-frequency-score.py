class Solution(object):
    def digitFrequencyScore(self, n):
        c = 0
        s = str(n)
        s1 = set(s)
        s1 = list(s1)
        for i in range(len(s1)):
            c += int(s1[i]) * s.count(s1[i])
        return c
        