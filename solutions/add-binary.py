class Solution(object):
    def addBinary(self, a, b):
        a1 = int(a,2)
        b1 = int(b,2)
        a2 = int(a1)
        b2 = int(b1)
        c = a2+b2
        c1 = bin(c)[2:]
        return c1    