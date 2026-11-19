class Solution(object):
    def countBits(self, n):
        l = []
        for i in range(0,n+1):
            s = bin(i)[2:]
            d = s.count("1")
            l.append(d)
        return l
        