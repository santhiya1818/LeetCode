class Solution(object):

    def maxBuilding(self, n, restrictions):
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()
        m = len(restrictions)
        for i in range(1, m):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, h1 + (id2 - id1))
        for i in range(m - 2, -1, -1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i + 1]
            restrictions[i][1] = min(h1, h2 + (id2 - id1))
        max_height = 0
        for i in range(1, m):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            peak = (h1 + h2 + (id2 - id1)) // 2
            max_height = max(max_height, peak)
        return max_height
