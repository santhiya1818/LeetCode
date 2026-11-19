class Solution(object):
    def wordPattern(self, pattern, s):
        p = {}
        dup = set()
        word = s.split()
        if len(word) != len(pattern):
            return False
        for i in range(len(pattern)):
            wr = word[i]
            pa = pattern[i]
            if pa in p:
                if p[pa] != wr:
                    return False
            else:
                if wr in dup:
                    return False
                p[pa] = wr
                dup.add(wr)
        return True
                
        