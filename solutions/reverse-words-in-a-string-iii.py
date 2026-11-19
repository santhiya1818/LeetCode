class Solution(object):
    def reverseWords(self, s):
        st = []
        t = s.split(' ')
        for i in t:
            st.append(i[::-1])
        return " ".join(st)
        