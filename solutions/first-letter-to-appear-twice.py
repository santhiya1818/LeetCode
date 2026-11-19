class Solution(object):
    def repeatedCharacter(self, s):
        st = set()
        for i in s:
            if i in st:
                return i
            else:
                st.add(i)
        