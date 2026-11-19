class Solution(object):
    def capitalizeTitle(self, title):
        t = title.split(' ')
        s = []
        for i in t:
            if len(i) <= 2:
                s.append(i.lower())
            else:
                s.append(i.capitalize())
        return " ".join(s)