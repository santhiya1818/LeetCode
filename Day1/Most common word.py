class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        for i in ".!'$:?,;":
            paragraph = paragraph.replace(i," ")
        paragraph = paragraph.lower()
        words = paragraph.split()
        f_para = []
        for i in words:
            if i not in banned:
                f_para.append(i)
        res = 0
        l = []
        for i in f_para:
            c = f_para.count(i)
            l.append(c)
        m = max(l)
        for i in range(len(l)):
            if l[i] == m:
                res = i
        return f_para[res]