class Solution(object):
    def countNegatives(self, grid):
        count = 0
        for m in grid:
            for n in m:
                if n < 0:
                    count = count + 1
        return count
