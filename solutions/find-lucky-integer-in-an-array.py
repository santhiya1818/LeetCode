class Solution(object):
    def findLucky(self, arr):
        f = 0
        l = []
        for i in range(len(arr)):
            if arr[i] == arr.count(arr[i]):
                l.append(arr.count(arr[i]))
        if len(l) != 0:
            return max(l)
        else:
            return -1
        