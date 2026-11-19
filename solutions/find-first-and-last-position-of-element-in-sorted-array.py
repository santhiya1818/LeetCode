class Solution(object):
    def searchRange(self, nums, target):
        l = []
        for i in range(len(nums)):
            if target == nums[i]:
                l.append(i)
            if target not in nums:
                l.append(-1)
                l.append(-1)
        if target in nums:
            return [l[0],l[len(l)-1]]
        elif(len(l) == 0):
            return [-1,-1]
        else:
            return [l[0],l[len(l)-1]]
        