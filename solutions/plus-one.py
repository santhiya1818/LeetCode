class Solution(object):
    def plusOne(self, digits):
        a = ""
        for i  in digits:
            d = str(i)
            a+=d
        di = int(a)
        di = di+1
        l = []
        s = str(di)
        for i in s:
            j = int(i)
            l.append(j)
        return l
