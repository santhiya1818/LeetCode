class Solution(object):
    def alternateDigitSum(self, n):
        res = 0
        s = str(n)
        for i in range(len(s)):
            if (i%2 == 0):
                res += int(s[i])
            else:
                res -= int(s[i])
        return res
        