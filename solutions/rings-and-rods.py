class Solution(object):
    def countPoints(self, rings):
        curr = 0
        for i in range(100):
            rod = str(i)
            if ("B" + rod) in rings and ("G" + rod) in rings and ("R" + rod) in rings:
                curr += 1
        return curr
