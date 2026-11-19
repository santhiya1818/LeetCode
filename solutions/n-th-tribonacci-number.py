class Solution(object):
    def tribonacci(self, n):
        if n == 1:
            return 1
        elif(n == 2):
            return 1
        elif(n == 3):
            return 2
        t1 = 0
        t2 = 1
        t3 = 1
        curr = 0
        for i in range(n-2):
            curr = t1+t2+t3
            t1 = t2
            t2 = t3
            t3 = curr
        return curr
        