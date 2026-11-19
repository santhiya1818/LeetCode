class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count  = 0
        l = []
        for i in range(len(nums)):
            if(nums[i] == 1):
                count+=1
            else:
                l.append(count)
                count = 0
            l.append(count)
        return max(l)

        