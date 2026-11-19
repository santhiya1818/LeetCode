class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        # This acts as our "memory"
        seen = {} 
        
        for i, num in enumerate(nums):
            # 1. Have we seen this number before?
            # 2. Is the gap between current index 'i' and 'seen[num]' <= k?
            if num in seen and i - seen[num] <= k:
                return True
            
            # Record/Update the latest index of this number
            seen[num] = i
            
        return False
