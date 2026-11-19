class Solution(object):
    def isIsomorphic(self, s, t):
        p = {}
        dup = set()
        w = s
        v = t
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            wr = w[i]
            pa = v[i]
            if pa in p:
                if p[pa] != wr:
                    return False
            else:
                if wr in dup:
                    return False
                p[pa] = wr
                dup.add(wr)
        return True
        