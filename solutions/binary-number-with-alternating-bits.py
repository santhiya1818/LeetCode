class Solution(object):
    def hasAlternatingBits(self, n):
        s = bin(n)[2:]
        l = []
        curr = s[0]
        for i in range(1,len(s)):
            if curr == s[i]:
                l.append(0)
            else:
                l.append(1)
            curr = s[i]
        if (len(l) == l.count(1)):
            return True
        else:
            return False