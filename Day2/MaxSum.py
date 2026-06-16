class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        n = len(nums)

        # Fast case: no swaps allowed
        if k == 0:
            best = cur = nums[0]

            for i in range(1, n):
                cur = max(nums[i], cur + nums[i])
                best = max(best, cur)

            return best

        ans = max(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for l in range(n):
            for r in range(l, n):

                cur_sum = prefix[r + 1] - prefix[l]

                inside = nums[l:r + 1]
                outside = nums[:l] + nums[r + 1:]

                inside.sort()                 # smallest first
                outside.sort(reverse=True)   # largest first

                new_sum = cur_sum

                t = min(k, len(inside), len(outside))

                for i in range(t):
                    gain = outside[i] - inside[i]

                    if gain > 0:
                        new_sum += gain
                    else:
                        break

                ans = max(ans, new_sum)

        return ans