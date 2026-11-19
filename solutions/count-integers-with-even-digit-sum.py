class Solution(object):
    def countEven(self, num):
        d = 0
        for i in range(1,num+1):
            d1 = 0
            s = str(i)
            for j in s:
                d1 += int(j)
            if(d1%2==0):
                d+=1
        return d
        