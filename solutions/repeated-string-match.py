class Solution(object):
    def repeatedStringMatch(self, a, b):
        f = 0
        st = ""
        limit = ceil(len(b)//len(a)) + 2
        while(f <= limit):
            st += a
            f+=1
            if b in st:
                return f
        return -1

        