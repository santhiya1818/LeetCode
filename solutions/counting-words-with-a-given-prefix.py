class Solution(object):
    def prefixCount(self, words, pref):
        res = 0
        for i in range(len(words)):
            if words[i].startswith(pref):
                res +=1
        if res != 0:
            return res
        else:
            return 0 
        