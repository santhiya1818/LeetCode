from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        f = 0
        count = Counter(nums)
        for i in count:
            if(count[i] >= 2):
                f+=1
        if(f >=1):
            return True
        else:
            return False

        