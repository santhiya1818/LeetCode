class Solution(object):
    def findKthSmallest(self, coins, k):
        # A simple, universal GCD function that replaces math.gcd
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # 1. Helper function to count numbers <= guess divisible by coins
        def count_multiples(guess):
            count = 0
            n = len(coins)
            
            # Checks all combinations of coins to eliminate duplicate overlaps
            for i in range(1, 1 << n):
                lcm_val = 1
                elements_count = 0
                for j in range(n):
                    if (i >> j) & 1:
                        # Replaced math.gcd with our custom get_gcd function
                        lcm_val = (lcm_val * coins[j]) // get_gcd(lcm_val, coins[j])
                        elements_count += 1
                
                # Inclusion-Exclusion principle
                if elements_count % 2 == 1:
                    count += guess // lcm_val
                else:
                    count -= guess // lcm_val
            return count

        # 2. Binary Search implementation
        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2   # Make a guess
            
            if count_multiples(mid) >= k:
                ans = mid             # Guess is valid, but check for a smaller working number
                high = mid - 1
            else:
                low = mid + 1         # Guess is too small, look higher
                
        return ans
