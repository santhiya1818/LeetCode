class Solution(object):
    def evenOddBit(self, n):
        e = 0
        o = 0
        b = bin(n)[2:][::-1]
        for i in range(len(b)):
            if (i % 2) == 0 and b[i] == "1":
                e+=1
            elif (i % 2) != 0 and b[i] == "1":
                o+=1
        return [e,o]
