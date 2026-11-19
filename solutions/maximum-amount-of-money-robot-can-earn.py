from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG = float('-inf')

        # dp[k][j] = best profit for current row at column j using k neutralizations
        # k = 0, 1, 2
        dp = [[NEG] * n for _ in range(3)]

        for i in range(m):
            new_dp = [[NEG] * n for _ in range(3)]

            for j in range(n):
                val = coins[i][j]

                for k in range(3):
                    best = NEG

                    # from top or left
                    if i == 0 and j == 0:
                        best = 0
                    else:
                        if i > 0:
                            best = max(best, dp[k][j])
                        if j > 0:
                            best = max(best, new_dp[k][j - 1])

                    if best == NEG:
                        continue

                    # take cell value normally
                    new_dp[k][j] = max(new_dp[k][j], best + val)

                    # neutralize if this is a robber cell and we still have uses
                    if val < 0 and k < 2:
                        new_dp[k + 1][j] = max(new_dp[k + 1][j], best)

            dp = new_dp

        return max(dp[k][n - 1] for k in range(3))