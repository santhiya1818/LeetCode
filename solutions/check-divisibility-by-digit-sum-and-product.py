class Solution(object):
    def checkDivisibility(self, n):
        s = str(n)
        su = 0
        pr = 1
        for i in s:
            su = su+ int(i)
            pr = pr * int(i)
        if n % (su+pr) == 0:
            return True
        else:
            return False
        