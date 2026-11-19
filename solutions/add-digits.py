class Solution(object):
    def addDigits(self, num):
        n = num
        while(num >= 10):
            s = str(num)
            n = 0
            for i in s:
                n += int(i)
                num = n
        return num
