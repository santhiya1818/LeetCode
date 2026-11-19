class Solution(object):
    def reversePrefix(self, s, k):
        s1 = s[:k]
        s2 = s[k:]
        rev = s1[::-1]
        res = rev+s2
        return res
        