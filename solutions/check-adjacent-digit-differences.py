class Solution(object):
    def isAdjacentDiffAtMostTwo(self, s):
        for i in range(len(s)-1):
            n1 = abs(int(s[i]) - int(s[i+1]))
            if n1 > 2:
                return False
        return True