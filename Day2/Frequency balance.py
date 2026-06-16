class Solution(object):
    def getLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        ans = 1

        for left in range(n):
            freq = {}
            freq_count = {}

            for right in range(left, n):
                x = nums[right]

                old = freq.get(x, 0)

                if old > 0:
                    freq_count[old] -= 1
                    if freq_count[old] == 0:
                        del freq_count[old]

                freq[x] = old + 1
                new = old + 1

                freq_count[new] = freq_count.get(new, 0) + 1

                # Only one distinct value
                if len(freq) == 1:
                    ans = max(ans, right - left + 1)

                # Exactly two frequencies: f and 2f
                elif len(freq_count) == 2:
                    f1, f2 = sorted(freq_count.keys())

                    if f2 == 2 * f1:
                        ans = max(ans, right - left + 1)

        return ans