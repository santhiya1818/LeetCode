class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if n != nums[i]:
                i += 1
                nums[i] = n
        return i + 1
