class Solution(object):
    def truncateSentence(self, s, k):
        t = s.split(' ')
        s = []
        for i in range(k):
            s.append(t[i])
        return " ".join(s)
        