class Solution(object):
    def numSteps(self, s):
        de = int(s,2)
        f = 0
        while (de != 1):
            if(de % 2 == 0):
                de = abs(de / 2)
                f+=1
            else:
                de = de + 1
                f+=1
        return f
        