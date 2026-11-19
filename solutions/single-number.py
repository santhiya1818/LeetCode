from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        for i in count:
            if count[i] == 1:
                return i
        
        