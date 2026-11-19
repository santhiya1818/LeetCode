class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(0,len(nums)):
            if nums[i] == target:
                return i            
            elif(nums[i] > target ): 
                return i
        if(nums[0] >= target):
            return 0
        return len(nums)
        