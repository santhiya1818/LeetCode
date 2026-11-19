class Solution(object):
    def intersect(self, nums1, nums2):
        dup = list(nums2)
        l = []
        for i in range(len(nums1)):
            if nums1[i] in dup:
                l.append(nums1[i])
                dup.remove(nums1[i])
        return l

        