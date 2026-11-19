class Solution(object):
    def thirdMax(self, nums):
        l = sorted(set(nums),reverse = True)
        if len(set(nums)) >= 3:
            return l[2]
        elif len(set(nums)) == 2:
            return l[0]
        else:
            return l[0]