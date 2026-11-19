class Solution(object):
    def reverseStr(self, s, k):
        d = ""
        n = 2*k
        for i in range(0,len(s),n):
            t = s[0+i:k+i]
            st = t[::-1]
            d += st + s[k+i:i+n]
        return d