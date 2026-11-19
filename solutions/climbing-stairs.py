class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        one_st = 1
        two_st = 2
        curr = 0
        for i in range(3,n+1):
            curr = one_st + two_st
            one_st = two_st
            two_st = curr
        return curr
        