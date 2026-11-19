class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        s1 = "".join(word1)
        s2 = "".join(word2)
        if s1 == s2:
            return True
        else:
            return False
        