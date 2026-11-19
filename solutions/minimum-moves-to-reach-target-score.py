class Solution(object):
    def minMoves(self, target, maxDoubles):
        m = 0
        while(target > 1):
            if(maxDoubles == 0):
                m = m + (target-1)
                break
            elif(target % 2 == 0 and maxDoubles > 0):
                target //= 2
                maxDoubles-=1
                m+=1
            else:
                target-=1
                m+=1
        return m        
        