# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        low = 1
        h = n
        while (low <= h):
            mid = (low +h) // 2
            res = guess(mid)
            if res == -1:
                h = mid -1
            elif res == 1:
                low = mid +1
            elif res == 0:
                return mid

        