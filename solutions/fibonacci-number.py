class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n
        f0 = 0
        f1 = 1
        curr = 0
        for i in range(n-1):
            curr = f0 + f1
            f0 = f1
            f1 = curr
        return curr
        