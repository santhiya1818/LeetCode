class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        n = abs(num)
        s = []
        while (n != 0):
            n1 = n % 7
            s.append(str(n1))
            n = n //7
        if (num < 0):
            st = "".join(s)
            return "-"+st[::-1]
        else:
            return "".join(s)[::-1]
        