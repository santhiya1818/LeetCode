class Solution(object):
    def checkGoodInteger(self, n):
        ds = 0
        ss = 0
        str1 = str(n)
        for i in str1:
            n1 = int(i)
            ds += n1
            n2 = n1*n1
            ss += n2
        if (ss - ds >= 50):
            return True
        else:
            return False