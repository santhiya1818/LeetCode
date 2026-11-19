from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)
        INF = 10**30

        # dp[i] = min cost to repair first i robots using factories processed so far
        dp = [0] + [INF] * n

        for pos, limit in factory:
            new_dp = dp[:]  # option: assign 0 robots to this factory

            for i in range(1, n + 1):
                cost = 0
                # Try assigning t robots ending at robot i-1 to this factory
                for t in range(1, min(limit, i) + 1):
                    cost += abs(robot[i - t] - pos)
                    if dp[i - t] + cost < new_dp[i]:
                        new_dp[i] = dp[i - t] + cost

            dp = new_dp

        return dp[n]