class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # first index goes to until we choose start of second sub. 
        # then we need to pick k - 2 elements from nums[j ... j + dist]
        # idea is: for each possible choice of j, what are the k - 2 smallest numbers in nums[j: j + dist]
        # so should keep a sorted list of numbers 
        # we should keep track of their sum, 
        # at each step, remove the previous number at [j] add that at j + dist 
        # when removing, check if it was part of the running sum. 
        
        base = nums[0]
        N = len(nums)
        if k  == N:
            return sum(nums)
        best = inf
        SL = SortedList() # will keep track of the k - 2 smallest within the desired distance
        # we need to initially populate it 
        for i, x in enumerate(nums[1 : dist + 1], start=1):
            SL.add(x)
        cur_sum = sum(x for x in SL[:k-2])

        # Main loop, try all starting index for 2nd array
        for j in range(1, N - k + 2): 
            
            # remove j
            x = nums[j]
            if SL.bisect_left(x) <= k - 3: # first k - 2 pos are 0, 1, ... k - 
                cur_sum -= x
                if len(SL) >= k - 1:
                    cur_sum += SL[k - 2] # what new element if any took its place? 
            SL.remove(x)
        
            # add the j + dist if its in bounds
            if j + dist < N:
                x = nums[j + dist]
                SL.add(x)
                if SL.bisect_left(x) <= k - 3: # new value affects cur_sum
                    cur_sum += x
                    if len(SL) >= k - 1: # check if it ejected something
                        cur_sum -= SL[k - 2]
              
            best = min(best, base + nums[j] + cur_sum)
        return best