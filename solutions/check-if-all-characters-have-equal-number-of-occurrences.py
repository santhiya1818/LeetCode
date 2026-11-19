class Solution(object):
    def areOccurrencesEqual(self, s):
        l = []
        for i in range(len(s)):
            l.append(s.count(s[i]))
        st = sorted(set(l))
        if len(st) == 1:
            return True
        else:
            return False
        