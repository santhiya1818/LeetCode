class Solution(object):
    def maxRatings(self, units):
        """
        :type units: List[List[int]]
        :rtype: int
        """

        base = 0
        second = []
        global_min = float('inf')

        for row in units:
            row.sort()

            base += row[0]
            global_min = min(global_min, row[0])

            if len(row) == 1:
                second.append(0)
            else:
                second.append(row[1])

        transfer_ans = sum(second) - min(second) + global_min

        return max(base, transfer_ans)