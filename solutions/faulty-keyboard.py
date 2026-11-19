class Solution(object):
    def finalString(self, s):
        st = ""
        for i in range(len(s)):
            if s[i] == "i":
                st = st[::-1]
            else:
                st += s[i]
        return st