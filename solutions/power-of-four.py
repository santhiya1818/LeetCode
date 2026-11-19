class Solution(object):
    def isPowerOfFour(self, n):
        for i in range(16):
            if(n == pow(4,i)):
                return True
        return False
        