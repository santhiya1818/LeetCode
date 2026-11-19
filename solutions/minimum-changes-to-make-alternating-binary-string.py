class Solution(object):
    def minOperations(self, s):
        res = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    res += 1
            else:
                if s[i] != '1':
                    res += 1
        return min(res, len(s) - res)