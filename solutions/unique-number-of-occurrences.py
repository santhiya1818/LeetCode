class Solution(object):
    def uniqueOccurrences(self, arr):
        s = sorted(set(arr))
        l = []
        for i in s:
            l.append(arr.count(i))
        if len(l) == len(sorted(set(l))):
            return True
        else:
            return False
        