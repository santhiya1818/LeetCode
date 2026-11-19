class Solution(object):
    def majorityElement(self, nums):
        can = None
        count = 0
        for i in nums:
            if (count == 0):
                can = i
            if(can == i):
                count = count + 1
            else:
                count = count - 1
        return can