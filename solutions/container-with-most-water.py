class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0

        while True:
            # the least number is the multiplier
            multipler = height[left] if height[left] < height[right] else height[right]

            #calculate the water contained and update 
            tmp_water = (right-left) * multipler
            if tmp_water > water: water = tmp_water

            if(height[left] < height[right]): left += 1
            else: right -= 1

            if(left >= right): break
    
        return water