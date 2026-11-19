class Solution(object):
    def firstUniqChar(self, s):
        c = {}
        for i in s:
            c[i] = c.get(i,0)+1
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1