
class Solution(object):
    def frequencySort(self, nums):
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        nums.sort(key = lambda x :(count[x], -x))
        return nums
        