class Solution(object):
    def addToArrayForm(self, num, k):
        s = ""
        l = []
        for i in num:
            r = str(i)
            s +=r
        de = int(s)
        sum = de+k
        d = str(sum)
        for i in d:
            h = int(i)
            l.append(h)
        return l

        