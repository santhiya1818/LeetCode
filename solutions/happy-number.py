class Solution(object):
    def isHappy(self, n):
        seen = set()
        s = str(n)
        sum1 = 0
        while(n != 1):
            s = str(n)
            sum1 = 0
            for i in s:
                n1 = int(i)
                sum1 += pow(n1,2)
            n = sum1
            if n in seen:
                return False
            seen.add(n)
        return True