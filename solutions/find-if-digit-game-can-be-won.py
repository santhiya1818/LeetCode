class Solution(object):
    def canAliceWin(self, nums):
        count1 = 0
        count2 = 0
        for i in nums:
            s = str(i)
            if len(s) == 2:
                count2 += int(s)
            else:
                count1+= int(s)
        if count1 == count2:
            return False
        else:
            return True
        