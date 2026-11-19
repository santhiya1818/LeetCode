class Solution(object):
    def largestInteger(self, num):
        s = list(str(num))
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                ft = int(s[i])
                sd = int(s[j])
                if (ft %2 == 0 and sd %2 == 0 and sd > ft):
                    s[i], s[j] = s[j] , s[i]
                elif (ft %2 != 0 and sd %2 != 0 and sd > ft):
                    s[i], s[j] = s[j] , s[i]
        res = "".join(s)
        r1 = int(res)
        return r1