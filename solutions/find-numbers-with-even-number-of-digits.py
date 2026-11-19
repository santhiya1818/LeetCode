class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            s = str(i)
            l = len(s)
            if (l % 2 == 0):
                count+=1
        return count
        