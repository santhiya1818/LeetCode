class Solution(object):
    def isPowerOfThree(self, n):
        for i in range(25):
            if n == pow(3,i):
                return True
        return False
        