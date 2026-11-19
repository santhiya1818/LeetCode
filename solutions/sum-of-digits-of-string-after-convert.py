class Solution(object):
    def getLucky(self, s, k):
        s1 = ""
        d = 0
        for i in s:
            n = (ord(i) - 97) + 1
            s1 += str(n)
        for j in range(k):
            d = 0
            for x in s1:
                d += int(x)
            s1 =""
            s1 = str(d)
        return d
        