class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)- (len(needle) - 1)):
            f = 0
            while f < len(needle) and haystack[i+f] == needle[f]:
                f = f+1
            if f == len(needle):
                    return i
        return -1
        