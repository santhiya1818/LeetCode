class Solution(object):
    def arrayRankTransform(self, arr):
        res = []
        s = sorted(set(arr))
        d = {}
        for i in range(len(s)):
            d[s[i]] = i+1
        for i in arr:
            res.append(d[i])
        return res