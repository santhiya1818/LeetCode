class Solution(object):
    def findKthPositive(self, arr, k):
        l = []
        for i in range(10000):
            if i not in arr:
                l.append(i)
        return l[k]

        