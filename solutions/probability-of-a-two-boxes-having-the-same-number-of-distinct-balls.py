class Solution(object):
    def getProbability(self, balls):
        from math import factorial
        k = len(balls)
        total_balls = sum(balls)
        half = total_balls // 2
        fact = [1] * (total_balls + 1)
        for i in range(1, total_balls + 1):
            fact[i] = fact[i-1] * i
        def comb(n, r):
            return fact[n] // (fact[r] * fact[n - r])
        total_ways = [0]
        valid_ways = [0]
        def backtrack(i, box1_count, box2_count, box1_distinct, box2_distinct, ways):
            if i == k:
                if box1_count == half and box2_count == half:
                    total_ways[0] += ways
                    if box1_distinct == box2_distinct:
                        valid_ways[0] += ways
                return
            for x in range(balls[i] + 1):
                y = balls[i] - x
                if box1_count + x > half or box2_count + y > half:
                    continue
                new_ways = ways * comb(balls[i], x)
                backtrack(
                    i + 1,
                    box1_count + x,
                    box2_count + y,
                    box1_distinct + (1 if x > 0 else 0),
                    box2_distinct + (1 if y > 0 else 0),
                    new_ways
                )
        backtrack(0, 0, 0, 0, 0, 1)
        return float(valid_ways[0]) / total_ways[0]
